import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

start_time = time.time()
# Чтение ссылок из файла
with open('LinkForLinks.txt', 'r', encoding='utf-8') as file:
    links = file.read().splitlines()

webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service)

geo_location_url = "https://business.sbermarket.ru/multisearch?q=Молоко%203%2C2%25%20ультрапастеризованное%201%20л%20ЭкоНива&sid=85&vertical=all"
driver.get(geo_location_url)
time.sleep(100)

results = []

for link in links:
    driver.get(link)
    print(link)
    time.sleep(1)

    # Цикл для каждого клика
    tag_counter = 0
    while True:
        stores = driver.find_elements(By.CSS_SELECTOR, 'li.Carousel_slide__Wg4C_ button.StoresItemCard_root__XjrcM')
        if tag_counter >= len(stores):
            break

        store = stores[tag_counter]

        time.sleep(1)
        new_page_soup = BeautifulSoup(driver.page_source, 'html.parser')
        city = new_page_soup.find('div', class_='AddressSelector_text__XB1ag').text.strip()
        print("Город:", city)

        # Получение первого тега
        sellers = new_page_soup.find_all('div', class_='StoresItemOrderProductsNumber_wrapper__fxcNc')
        if len(sellers) > tag_counter:
            seller = sellers[tag_counter]
            imgTag = seller.find('img') if seller else None
            imgalt = imgTag['alt'] if imgTag else None
            print("Первый тег:", imgalt)
        else:
            print("Больше нет тегов")
        if imgalt == "ЛЕНТА" or imgalt == "METRO":
            for product in new_page_soup.find('div', class_='MultiSearchProductsGrid_root__ye_kY MultiSearch_productGrid__ZXhdl').find_all('li'):
                product_info = {}
                try:
                    name = product.find('h3', class_="ProductCard_title__iB_Dr").text.strip()
                    print(name)
                except AttributeError:
                    name = None
                product_info['name'] = name if name else ""

                try:
                    price_one = product.find('div', class_='ProductCardPrice_price__zSwp0').text.strip()
                    print(price_one)
                except AttributeError:
                    price_one = None
                try:
                    price_two = product.find('div', class_='ProductCardPrice_vatInfo__sn9fH').text.strip()
                    print(price_two)
                except AttributeError:
                    price_two = None

                product_info['price_one'] = price_one
                product_info['price_two'] = price_two
                product_info['date'] = datetime.datetime.now().strftime("%d.%m.%Y")
                product_info['imgalt'] = imgalt if imgalt else ""
                product_info['city'] = city

                with open('SberFoodParsing.csv', 'a', newline='', encoding='utf-8') as csvfile:
                    fieldnames = ['name', 'price_one', 'price_two', 'city', 'date', 'imgalt']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow(product_info)

            driver.execute_script("arguments[0].click();", store)
            time.sleep(5)
            tag_counter += 1
        else:
            tag_counter += 20

end_time = time.time()
execution_time = (end_time - start_time) / 60
print(f"Время выполнения: {execution_time} минут")

data = pd.read_csv('SberFoodParsing.csv')
data.drop_duplicates(inplace=True)
data.to_csv('SberFoodParsing.csv', index=False)
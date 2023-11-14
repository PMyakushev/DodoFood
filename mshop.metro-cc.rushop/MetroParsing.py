from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

# Список логинов и паролей
print("Что бы выбрать СПБ нажимте - 1 \nЧто бы выбрать САМАРА нажимте - 2 \nЧто бы выбрать УФА нажимте - 3\nЧто бы выбрать ПЕНЗА нажимте - 4"
      "\nЧто бы выбрать КУРСК нажимте - 5\nЧто бы выбрать НОВГОРОД нажимте - 6\nЧто бы выбрать ОРЕНБУРГ нажимте - 7\nЧто бы выбрать НОВОКУЗНЕЦК нажимте - 8"
      "\nЧто бы выбрать КЕМЕРОВО нажимте - 9\nЧто бы выбрать МАГНИТОГОРСК нажимте - 10\nЧто бы выбрать ВОЛГОГРАД нажимте - 11\nЧто бы выбрать ДОМОДЕДОВО нажимте - 12"
      "\nЧто бы выбрать МОСКВА нажимте - 13\nЧто бы выбрать КОПЕЙСК нажимте - 14\nЧто бы выбрать ПЫШМА нажимте - 15\nЧто бы выбрать ТАГИЛ нажимте - 16"
      "\nЧто бы выбрать КРАСНОЯРСК нажимте - 17\nЧто бы выбрать БАЛАКОВО нажимте - 18\nЧто бы выбрать ТОЛЬЯТТИ нажимте - 19\nЧто бы выбрать КСТОВО нажимте - 20")
choice = input("Введите цифру вашего города: ")
if choice == "1":
    print("Вы выбрали СПБ")
    credentials = [
        {"login": "spbplyus", "password": "12345678"},
        {"login": "dodo.pitstza", "password": "12345678"},
        {"login": "pizzavo01", "password": "metro12345"},
    ]
elif choice == "2":
    print("Вы выбрали Самара")
    credentials = [
        {"login": "Oz15.dodo@gmail.com", "password": "Oz15.dodo@gmail.com"},
        {"login": "oz120.dodo", "password": "oz120.dodo"},
        {"login": "oz25.dodo", "password": "oz25.dodo"},
        {"login": "DODOPRTSS", "password": "DODOPRTSS"},
    ]
elif choice == "3":
    print("Вы выбрали УФА")
    credentials = [
        {"login": "dodo.ufa1@gmail.com", "password": "dodo.ufa1@gmail.com"},
        {"login": "ufa2.dodo@gmail.com", "password": "ufa2.dodo@gmail.com"},
        {"login": "troshindodo@gmail.com", "password": "troshindodo@gmail.com"},
        {"login": "egmasl@yandex.ru", "password": "egmasl@yandex.ru"},
    ]
elif choice == "4":
    print("Вы выбрали ПЕНЗА")
    credentials = [
        {"login": "DODOPENZA", "password": "DODOPENZA"},
    ]
elif choice == "5":
    print("Вы выбрали КУРСК")
    credentials = [
        {"login": "DODOKURSK", "password": "DODOKURSK"},
    ]
elif choice == "6":
    print("Вы выбрали НОВГОРОД")
    credentials = [
        {"login": "DODONOVGOROD", "password": "DODOKSTOVO"},
    ]
elif choice == "7":
    print("Вы выбрали ОРЕНБУРГ")
    credentials = [
        {"login": "e.maslennikova.dodo@gmail.com", "password": "metro12345"},
        {"login": "ORENDODO", "password": "ORENDODO"},
    ]
elif choice == "8":
    print("Вы выбрали НОВОКУЗНЕЦК")
    credentials = [
        {"login": "Picca2021", "password": "Picca2021"},
    ]
elif choice == "9":
    print("Вы выбрали КЕМЕРОВО")
    credentials = [
        {"login": "Dodopizzasibir", "password": "dodopizza1709"},
    ]
elif choice == "10":
    print("Вы выбрали МАГНИТОГОРСК")
    credentials = [
        {"login": "metromgn.dodo@gmail.com", "password": "METRO123"},
    ]
elif choice == "11":
    print("Вы выбрали ВОЛГОГРАД")
    credentials = [
        {"login": "egmaslennikova@yandex.ru", "password": "123456789"},
    ]
elif choice == "12":
    print("Вы выбрали ДОМОДЕДОВО")
    credentials = [
        {"login": "oz3.dodo@gmail.com", "password": "123456789"},
    ]
elif choice == "13":
    print("Вы выбрали МОСКВА")
    credentials = [
        {"login": "kolesnikov.dodopizza@gmail.com", "password": "Metro123"},
    ]
elif choice == "14":
    print("Вы выбрали КОПЕЙСК")
    credentials = [
        {"login": "dodo5555", "password": "dodo5555"},
    ]
elif choice == "15":
    print("Вы выбрали ПЫШМА")
    credentials = [
        {"login": "v.pishma.dodo@gmail.com", "password": "Dodopizza21"},
    ]
elif choice == "16":
    print("Вы выбрали ТАГИЛ")
    credentials = [
        {"login": "n.tagil.dodo@gmail.com", "password": "Dodopizza21"},
    ]
elif choice == "17":
    print("Вы выбрали КРАСНОЯРСК")
    credentials = [
        {"login": "Krasnoyarsk-dodo", "password": "zZ12345!"},
    ]
elif choice == "18":
    print("Вы выбрали БАЛАКОВО")
    credentials = [
        {"login": "i.belyanskiy.dodo@gmail.com", "password": "dodo2022"},
    ]
elif choice == "19":
    print("Вы выбрали ТОЛЬЯТТИ")
    credentials = [
        {"login": "oz12.dodo", "password": "oz12.dodo"},
    ]
elif choice == "20":
    print("Вы выбрали КСТОВО")
    credentials = [
        {"login": "rp.kstovo.ms@gmail.com", "password": "metro123"},
    ]
else:
    print("Вы ввели что-то, не то")

# Установка веб-драйвера Chrome
webdriver_service = Service(ChromeDriverManager().install())
options = Options()
options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.931 YaBrowser/23.9.3.931 Yowser/2.5 Safari/537.36")

# Цикл для входа с разными учетными данными и перехода по ссылкам
for credential in credentials:
    driver = webdriver.Chrome(service=webdriver_service, options=options)


    def login(username, password):
        # Открытие страницы авторизации
        url = "https://idam.metro-cc.ru/web/Signin?response_mode=query&state=e976299a02ef47f3b8e44a6bcccc8f87&scope=openid+clnt%3DBTEX&locale_id=ru-RU&redirect_uri=https%3A%2F%2Fmshop.metro-cc.ru%2Fshop%2F%3FidamRedirect%3D1&client_id=BTEX&country_code=RU&realm_id=SSO_CUST_RU&user_type=CUST&DR-Trace-ID=idam-trace-id&code_challenge=uYKuBs5aVqSQhn888IyWA0G6Wls90uvOtHlbgs2nY9Q&code_challenge_method=S256&response_type=code"
        driver.get(url)

        time.sleep(10)

        # Ввод логина
        username_input = driver.find_element(By.ID, "user_id")
        username_input.clear()
        username_input.send_keys(username)

        # Ввод пароля
        password_input = driver.find_element(By.ID, "password")
        password_input.clear()
        password_input.send_keys(password)

        time.sleep(5)

        # Клик на кнопку "Войти"
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(15)


    def logout():
        # Добавьте здесь код для разлогина

        time.sleep(5)


    def click_button():

        wait = WebDriverWait(driver, 10)
        try:
            button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "test-select-address-button")))
            button.click()

        except TimeoutException:
            print("Тайм-аут: кнопка не найдена. Продолжаем выполнение кода без клика.")

        time.sleep(10)

        links = []
        elements = driver.find_elements(By.CLASS_NAME, "col-lg-3.col-md-4.col-sm-6.col-xs-12")
        if elements:
            for element in elements:
                link = element.get_attribute("href")
                if link:
                    links.append(link)
        else:
            print('Кнопка не найдена. Продолжаем выполнение кода без получения ссылок.')

        for link in links:
            driver.get(link)

        data = []
        with open('LinksForMetro.txt', "r", encoding="utf-8") as file:
            links = file.readlines()
            for link in links:
                link = link.strip()
                driver.get(link)
                time.sleep(5)

                elements = driver.find_elements(By.CLASS_NAME, "well-sm.well")

                for element in elements:
                    data.append(element.text)

                time.sleep(5)

        with open('MetroFoodHTML.html', "a", encoding="utf-8") as html_file:
            html_file.write('<html>\n')
            html_file.write('<body>\n')
            html_file.write('<h2>Сессии:</h2>\n')
            html_file.write(f'<p>Логин: {credential["login"]}, Пароль: {credential["password"]}</p>\n')
            html_file.write('<hr>\n')

            html_file.write('<h2>Данные:</h2>\n')
            html_file.write('<ul>\n')
            for item in data:
                html_file.write(f'<li>{item}</li>\n')
            html_file.write('</ul>\n')
            html_file.write('</body>\n')
            html_file.write('</html>\n')


    login(credential["login"], credential["password"])
    click_button()

    # Добавить код разлогина по окончании сессии
    logout()

    driver.quit()

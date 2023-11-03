import csv
from bs4 import BeautifulSoup
import datetime

# Открытие файла
with open('data.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Создание объекта BeautifulSoup для парсинга HTML
soup = BeautifulSoup(html, 'html.parser')

# Создание списка для хранения данных
data_list = []

# Извлечение данных из HTML
all_data = soup.find_all('body')
for el in all_data:
    login = el.find('p').get_text()
    data = el.find_all('li')
    for item in data:
        info = item.get_text().split('\n')
        info = [i.strip() for i in info if i.strip()]
        if info:
            info = [i for i in info if i not in ["Недавно заказанные", "Начните искать и добавлять в корзину товар. Ваша корзина продуктов будет отображена здесь", "Ваша корзина пока пустая", "+1 больше", "за кг"]]
            date = datetime.datetime.now().strftime("%d.%m.%Y")
            data_list.append([login, info, date])

# Запись данных в файл CSV
with open('MetroFoodCSV.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Login', 'Info', 'Date'])  # Запись заголовков столбцов
    writer.writerows(data_list)  # Запись данных

print("Данные успешно записаны в файл output.csv и обработаны")


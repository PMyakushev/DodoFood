import time
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv
from concurrent.futures import ThreadPoolExecutor
import datetime
# Cookie = ("qrator_jsr=1698997102.233.o3ZYRXRufOdWaqoy-eogu6nau6o28evf82gpha7pu4vs69094-00; qrator_jsid=1698997102.233.o3ZYRXRufOdWaqoy-22c1aor4tl2t21pcfjin1qth5b6bdhv1; cookiesession1=678A3F62AE0723F739D6493042B614EB; qrator_ssid=1698997103.933.WMWjnmTJkMFffHZg-veluo9gd4oua7v7bl7oq3iv0ooo147nv; JSESSIONID=50c50191-373f-47a5-b360-e685e0b676af.hybris5p.komus.net; USER_ID=980504408; USER_ID=980504408; rxVisitor=1698997104777B71AD6JEO5EN2J39TQ3ERI129POAPPIH; dtSa=-; _gid=GA1.2.213689805.1698997105; uxs_uid=f9d81e20-7a1b-11ee-8abf-3de58a4ef977; dtCookie=v_4_srv_3_sn_C204FE76D282471439FC1FBBC0482EEC_app-3A40c41a8250581be2_1_ol_0_perc_100000_mul_1_rcs-3Acss_0; _ym_uid=1698997107349342884; _ym_d=1698997107; tmr_lvid=589dd55d0679795014dd94c2d6ec8424; tmr_lvidTS=1698997107279; mindboxDeviceUUID=c9baf068-c626-4e9a-9b12-87384a056308; directCrm-session=%7B%22deviceGuid%22%3A%22c9baf068-c626-4e9a-9b12-87384a056308%22%7D; _ym_isad=2; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; tmr_detect=0%7C1698997195964; CURRENT_REGION=31; CONFIRMED_REGION=31; _ga_RGNJLEG36H=GS1.1.1698997107.1.1.1698997260.0.0.0; _ga=GA1.2.374145486.1698997105; rxvt=1698999061752|1698997104780; dtPC=3$397260278_577h9vTRBSIPBJGFQAUPFAGVKAAMRBOMRHTKBH-0e0")

Cookie = input(str("Введите Cookie: "))



def parse_link(link):
    print(link)
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "Content-Length": "0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": Cookie,
        "Origin": "https://www.komus.ru",
        "Referer": "https://www.komus.ru/katalog/otraslevye-predlozheniya/tovary-dlya-torgovli/pakety/pakety-majka/paket-majka-pnd-15-mkm-belyj-30-18kh55-sm-100-shtuk-v-upakovke-/p/57602/?tabId=specifications&text=57602&qid=9912693462",
        "Sec-Ch-Ua": '"Chromium";v="118","Google Chrome";v="118","Not=A?Brand";v="99"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "X-Dtpc": "4$589805044_630h4vFFSCBDKVOJERMWNWVPLHPKKAAGEQPVPU-0e0",
        "X-Kl-Kfa-Ajax-Request": "Ajax_Request",
        "X-Requested-With": "XMLHttpRequest"
    }

    response = requests.get(link, headers=headers)
    response.raise_for_status()
    data = []
    data.append(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    city = soup.find('span', 'b-enterAccount__link b-enterAccount__link--arrow').text.strip()
    data.append(city)
    print(city)
    name = soup.find('h1', 'product-details-page__title').text.strip()
    data.append(name)
    print(name)
    articl = soup.find('span', 'qa-vendor-code').text.strip()
    data.append(articl)
    print(articl)
    data_time = datetime.datetime.now().strftime("%d.%m.%Y")
    data.append(data_time)
    print(data_time)
    try:
        prices = soup.find('a', 'product-price__current-price js-coins')
        price = prices.find('span', class_="").text.strip()
        print(price)
    except:
        price = ""
    data.append(price)

    with open('dateInfo.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Чтение ссылок для парсинга из файла
with open("LinksForParsing.txt", "r", encoding='utf-8') as file:
    links = file.read().splitlines()

# Создание пула потоков для параллельного выполнения
with ThreadPoolExecutor(max_workers=10) as executor:
    # Отправка каждой ссылки на обработку в отдельном потоке
    executor.map(parse_link, links)
# Парсер сайта с данными о восходах,
# закатах и длительности светового дня

from bs4 import BeautifulSoup
import requests
import lxml
from pprint import pprint
import rich
from rich import console
import time
import csv


cons = console.Console()
id_city = '497927' # id сегежи


year = [
        'январь', 'февраль', 'март',
        'апрель', 'май', 'июнь',
        'июль', 'август', 'сентябрь',
        'октябрь', 'ноябрь', 'декабрь',
    ]

sunrise_data = []
for month in range(12):
    url = f'https://dateandtime.info/ru/citysunrisesunset.php?id={id_city}&month={month+1}&year=2022'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")

    res = soup.find_all('table', attrs={'class':'sunrise_table'})
    tbody = res[1].find('tbody')
    tr = tbody.find_all('tr')
    print(f'Получение данных за {year[month]}')
    for _tr in tr:
        temp_data = {}
        td = _tr.find_all('td')
        day = td[0].text.strip().split()[1]
        sunrise = td[1].find('span', attrs={'class':'short24hm'}).text
        sunset = td[2].find('span', attrs={'class':'short24hm'}).text
        daylight_hours = td[4].text.strip()
        temp_data['day'] = day
        temp_data['month'] = month+1
        temp_data['sunrise'] = sunrise
        temp_data['sunset'] = sunset
        temp_data['dlh'] = daylight_hours
        sunrise_data.append(temp_data)
    print(f'\Данные за {year[month]} успешно получены')
    print('='*40)



if sunrise_data:
    with open('sunrise_data.csv', 'w', newline='') as f:
        cons.print("\n Запись данных в файл...")
        fieldnames = ['day', 'month', 'sunrise', 'sunset', 'dlh']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for data in sunrise_data:
            writer.writerow(data)
        cons.print("\n Данные сохранены...")

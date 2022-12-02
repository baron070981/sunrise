from datetime import datetime
from datetime import timedelta
import pandas as pd
from typing import Tuple

# загрузка данных из файла
# в файле обязательны столбцы: day, month, sunrise, sunset, dlh
data = pd.read_csv('sunrise_data.csv', sep=',')


# поиск похожего дня в загруженных данных
def get_similar_day(day: int, month: int, column_name: str):
    # 1 <= day <= 31
    # 1 <= month <= 12
    # column_name - sunrise, sunset или dlh
    # возвращает датафрейм на выбранную дату и series на найденную
    template_time = '%H:%M:%S' if column_name == 'dlh' else '%H:%M'
    
    current_data = data.query('day == @day & month == @month')
    min_dif = timedelta(hours=23, minutes=59)
    
    # если дата 21 июня, возвращаются данные за этот же день
    if month == 6 and day == 21:
        df = data[(data['day']==day)&(data['month']==month)]
        return current_data, current_data
    
    # если дата 21 или 22 декабря, возвращаются данные за этот же день
    elif month == 12 and day in [21, 22]:
        df = data[(data['day']==day)&(data['month']==month)]
        return current_data, current_data
    
    # получение данных с 22 июня по 20 декабря включительно
    elif (month < 6) or (month == 6 and day < 21) or (month == 12 and day > 21):
        df = data.query('month == 6 & day > 21 | month > 6 & month < 12 | month == 12 & day < 21')
    
    # получение данных с 23 декабря по 20 июня включительно
    elif (month > 6) or (month == 6 and day > 21) or (month == 12 and day < 21):
        df = data.query('month == 6 & day < 21 | month < 6  | month == 12 & day > 22')
    
    res_data = None
    current = current_data[column_name].values[0]
    current = datetime.strptime(current.strip(), template_time)
    # перебор строк из полученного датафрейма и поиск минимальной
    # разницы времени между временем в выбранной дате и временами 
    # в полученном датафрейме
    for i, row in df.iterrows():
        str_t = row[column_name]
        t = datetime.strptime(str_t.strip(), template_time)
        if min_dif > (abs(t - current)):
            min_dif = abs(t - current)
            res_data = row
    return current_data, res_data
    




if __name__ == '__main__':
    
    day = 15
    month = 8
    a, b = get_similar_day(day, month, 'sunrise')
    a = a.append(b)
    a = a.append(b)
    a = a.append(b)
    print(a)


















# получение и обработка данных из дата фрейма
# получение датафрейма из файла

from datetime import datetime
from datetime import timedelta
import pandas as pd


data = pd.read_csv('sunrise_data.csv', sep=',')

def get_similar_day(day, month, column_name):
    template_time = '%H:%M:%S' if column_name == 'dlh' else '%H:%M'
    
    current_data = data.query('day == @day & month == @month')
    min_dif = timedelta(hours=23, minutes=59)
    
    if month == 6 and day == 21:
        df = data[(data['day']==day)&(data['month']==month)]
        return current_data, current_data
    
    elif month == 12 and day in [21, 22]:
        df = data[(data['day']==day)&(data['month']==month)]
        return current_data, current_data
    
    elif (month < 6) or (month == 6 and day < 21) or (month == 12 and day > 21):
        df = data.query('month == 6 & day > 21 | month > 6 & month < 12 | month == 12 & day < 21')
    
    elif (month > 6) or (month == 6 and day > 21) or (month == 12 and day < 21):
        df = data.query('month == 6 & day < 21 | month < 6  | month == 12 & day > 22')
    
    res_data = None
    current = current_data[column_name].values[0]
    current = datetime.strptime(current.strip(), template_time)
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


















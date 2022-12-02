from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivymd.uix.picker import MDDatePicker
from kivy.clock import Clock
from datetime import datetime


import sunrisedata




class MainLayout(Screen):
    '''
    Главный экран приложения
    '''
    
    param_list = ['dlh', 'sunrise', 'sunset']
    idx = ['current', 'dlh', 'sunrise', 'sunset']
    params = ', '.join(param_list)
    information = ListProperty([])
    dinfo = StringProperty()
    tinfo = StringProperty()
    dataframe = None
    
    month_names_ru = {
        1:'января', 2:'февраля', 3:'марта',
        4:'апреля', 5:'мая', 6:'июня',
        7:'июля', 8:'августа', 9:'сентября',
        10:'октября', 11:'ноября', 12:'декабря',
    }
    
    
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
    
    
    def on_pre_enter(self):
        # запуск часов при создании экрана
        self.c = Clock.schedule_interval(self.update, 1)
    
    
    def on_pre_leave(self):
        # остановка часов при переходе на другой экран
        self.c.cancel()
    
    
    def update(self, *args):
        # обновление часов и даты в виджете
        d = datetime.today()
        day = d.day
        month = d.month
        year = d.year
        day = str(day) if day >= 10 else '0'+str(day)
        month = MainLayout.month_names_ru.get(month, month)
        h = str(d.hour) if d.hour >= 10 else '0'+str(d.hour)
        m = str(d.minute)  if d.minute >= 10 else '0'+str(d.minute)
        s = str(d.second)  if d.second >= 10 else '0'+str(d.second)
        
        dmy = f'{day} {month} {year}'
        dt = f'{h}:{m}:{s}'
        MDApp.get_running_app().root.ids.mainlayout.ids.time_info.text = dt
        MDApp.get_running_app().root.ids.mainlayout.ids.date_info.text = dmy
    
    
    def on_save(self, instance, value, date_range):
        # получение данных на выбранную дату в виджете календаря
        month, day = value.month, value.day
        current, data = sunrisedata.get_similar_day(day, month, MainLayout.param_list[0])
        alldata = current.append(data)
        for i in range(1, len(MainLayout.param_list)):
            _, data = sunrisedata.get_similar_day(day, month, MainLayout.param_list[i])
            alldata = alldata.append(data)
        alldata.index = MainLayout.idx
        MainLayout.dataframe = alldata
        # переход на следующий экран(активити)
        MDApp.get_running_app().root.current = 'infoscreen'
    
    
    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
    
    
    def show_date_picker(self):
        date_dialog = MDDatePicker(title="Выберите дату",
                                   min_year=2022, max_year=2022)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
    
    
    def today_data(self):
        # получение данных на текущую дату
        today = datetime.today()
        day = today.day
        month = today.month
        current, data = sunrisedata.get_similar_day(day, month, MainLayout.param_list[0])
        alldata = current.append(data)
        for i in range(1, len(MainLayout.param_list)):
            _, data = sunrisedata.get_similar_day(day, month, MainLayout.param_list[i])
            alldata = alldata.append(data)
        alldata.index = MainLayout.idx
        MainLayout.dataframe = alldata
        MDApp.get_running_app().root.current = 'infoscreen'
    
 
    
    
    
    



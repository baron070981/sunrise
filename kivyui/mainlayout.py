from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivy.clock import Clock
import pandas as pd
from datetime import datetime
import time


import sunrisedata

import rich
from rich import inspect



class MainLayout(Screen):
    
    
    param_list = ['dlh', 'sunrise', 'sunset']
    idx = ['current', 'dlh', 'sunrise', 'sunset']
    params = ', '.join(param_list)
    information = ListProperty([])
    dinfo = StringProperty()
    tinfo = StringProperty()
    dataframe = None
    
    
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        MainLayout.dinfo, MainLayout.tinfo = self.__get_today()
    
    
    def on_pre_enter(self):
        self.c = Clock.schedule_interval(self.update, 1)
        # c.cancel()
    
    
    def on_pre_leave(self):
        self.c.cancel()
    
    
    def update(self, *args):
        d = datetime.today()
        h = str(d.hour) if d.hour >= 10 else '0'+str(d.hour)
        m = str(d.minute)  if d.minute >= 10 else '0'+str(d.minute)
        s = str(d.second)  if d.second >= 10 else '0'+str(d.second)
        
        dt = f'{h}:{m}:{s}'
        MDApp.get_running_app().root.ids.mainlayout.ids.time_info.text = dt
        
    
    
    def __get_today(self):
        month_names = {
            1:'января', 2:'февраля', 3:'марта',
            4:'апреля', 5:'мая', 6:'июня',
            7:'июля', 8:'августа', 9:'сентября',
            10:'октября', 11:'ноября', 12:'декабря',
        }
        td = datetime.today()
        d_text = f'{td.day}  {month_names[td.month]}  {td.year}'
        t_text = f'{td.hour} : {td.minute}'
        return d_text, t_text
    
    
    def on_save(self, instance, value, date_range):
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
    
    
    def new_txt(self):
        MDApp.get_running_app().root.ids.time_info.text = "new text"
    
    
    
    
    
    



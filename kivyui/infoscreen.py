from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty

from kivyui import mainlayout




class InfoScreen(Screen):
    
    infoparam = StringProperty()
    infodata = StringProperty()
    information = ListProperty([])
    
    def on_pre_enter(self):
        
        df = MDApp.get_running_app().root.ids.mainlayout.dataframe
        print(df)
        c_d = self.str_align(str(df.loc["current"]["day"]))
        c_m = self.str_align(str(df.loc["current"]["month"]))
        
        dlh_d = self.str_align(str(df.loc["dlh"]["day"]))
        dlh_m = self.str_align(str(df.loc["dlh"]["month"]))
        
        sr_d = self.str_align(str(df.loc["sunrise"]["day"]))
        sr_m = self.str_align(str(df.loc["sunrise"]["month"]))
        
        ss_d = self.str_align(str(df.loc["sunset"]["day"]))
        ss_m = self.str_align(str(df.loc["sunset"]["month"]))
        
        text = f'''{"Выбранная дата: ".ljust(25, '.')} {c_d}.{c_m}
{'Долгота дня: '.ljust(29, '.')} {df.loc["current"]["dlh"]}
{'Восход: '.ljust(34, '.')} {df.loc["current"]["sunrise"]}
{'Закат: '.ljust(36, '.')} {df.loc["current"]["sunset"]}

{'Дата по долготе дня: '.ljust(22, '.')} {dlh_d}.{dlh_m}
{'Долгота дня: '.ljust(29, '.')} {df.loc["dlh"]["dlh"]}
{'Восход: '.ljust(34, '.')} {df.loc["dlh"]["sunrise"]}
{'Закат: '.ljust(36, '.')} {df.loc["dlh"]["sunset"]}

{'Дата по рассвету: '.ljust(25, '.')} {sr_d}.{sr_m}
{'Долгота дня: '.ljust(29, '.')} {df.loc["sunrise"]["dlh"]}
{'Восход: '.ljust(34, '.')} {df.loc["sunrise"]["sunrise"]}
{'Закат: '.ljust(36, '.')} {df.loc["sunrise"]["sunset"]}

{'Дата по закату: '.ljust(27, '.')} {ss_d}.{ss_m}
{'Долгота дня: '.ljust(29, '.')} {df.loc["sunset"]["dlh"]}
{'Восход: '.ljust(34, '.')} {df.loc["sunset"]["sunrise"]}
{'Закат: '.ljust(36, '.')} {df.loc["sunset"]["sunset"]}'''
        
        self.infodata = text
    
    
    def step_back(self):
        MDApp.get_running_app().root.current = 'mainlayout'
    
    
    def str_align(self, string):
        return string if len(string) > 1 else '0'+string
    
    
    
    
    

    
    
    
    
    
    
    
    






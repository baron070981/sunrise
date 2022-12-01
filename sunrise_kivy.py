import pandas as pd

from kivy.config import Config
Config.set('graphics','width','900')
Config.set('graphics','height','720')

from kivymd.app import MDApp
from kivymd.app import App
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDIconButton
from kivymd.theming import ThemeManager as tm
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivymd.uix.picker import MDDatePicker
from pathlib import Path


from kivyui import mainlayout as ml
from kivyui import infoscreen as inf
import sunrisedata


colors = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue',
          'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 
          'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']


class Manager(ScreenManager):
    mainlayout = ObjectProperty(None)
    infoscreen = ObjectProperty(None)


class SunriseApp(MDApp):
    
    current_dir = Path(__file__).resolve().parent
    image_dir = current_dir / 'src/images'
    kivyui_dir = current_dir / 'kivyui'
    
    
    def __init__(self, *kwargs):
        super(SunriseApp, self).__init__(*kwargs)
    
    def build(self):
        self.theme_cls.primary_palette =  "Blue"
        self.theme_cls.primary_hue =  "700"
        self.theme_cls.theme_style = "Dark" 
        return Manager()
    
    
    



if __name__ == '__main__':
    SunriseApp().run()














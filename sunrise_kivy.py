from kivy.config import Config
Config.set('graphics','width','900')
Config.set('graphics','height','720')

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty
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
    
    # корень проекта
    current_dir = Path(__file__).resolve().parent
    # папка для изображений
    image_dir = current_dir / 'src/images'
    # папка для kivy
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














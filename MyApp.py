from kivy import Config
from KvString import *
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivymd.uix.picker import MDDatePicker,MDThemePicker
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from datetime import date
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.core.text import Label as CoreLabel
import math
import kivy
from kivy.graphics import Ellipse, Color, Rectangle
from kivy.vector import Vector
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
#from math import atan2, sqrt, pow, degrees, sin, cos, radians
import random
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, TwoLineListItem
from kivymd.uix.list import OneLineListItem, TwoLineIconListItem, IconLeftWidget,TwoLineAvatarIconListItem,IconRightWidget
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition, NoTransition, FallOutTransition
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine, MDExpansionPanelThreeLine
from kivy.app import App
#Config.set('graphics','resizable',0)
Window.size=(400,600)

class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


class Content2(MDBoxLayout):
    pass
class Content3(MDBoxLayout):
    pass

class Content4(MDBoxLayout):
    pass
class Warning(MDBoxLayout):
    pass
class Warning1(MDBoxLayout):
    pass
class Content1(MDBoxLayout):
    name = ObjectProperty(None)
    cost = ObjectProperty(None)

class Add(MDBoxLayout):
    name = ObjectProperty(None)
    cost = ObjectProperty(None)


class Content(MDBoxLayout):
    name = ObjectProperty(None)
    cost = ObjectProperty(None)


class help(MDBoxLayout):
    pass
class helpTrack(MDBoxLayout):
    pass
class helpOverview(MDBoxLayout):
    pass
class helpSave(MDBoxLayout):
    pass
class viewAll(Screen):
    pass


class Existing(MDBoxLayout):
    pass

class Content5(MDBoxLayout):
    pass
class Bar(Screen):
    pass




# Create the screen manager
sm = ScreenManager(transition=FadeTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))
sm.add_widget(Bar(name="Bar"))


class MyApp(MDApp):


    def build(self):

        self.screen = Builder.load_string(screenHelp)
        self.scrollSearch=ScrollView(pos_hint= {"center_y":0.3}, size_hint_y=0.4)
        self.listView=MDList()
        self.HasBeenSearched=False
        self.list1=OneLineListItem(text="hello")
        self.list2=OneLineListItem(text="hello")
        self.list3=OneLineListItem(text="hello")
        self.list4=OneLineListItem(text="hello")
        self.statLabel=MDLabel(text="General statistics", font_style="H5",pos_hint= {"center_x":0.6, "center_y": 0.6})
        self.listView.add_widget(self.list1)
        self.listView.add_widget(self.list2)
        self.listView.add_widget(self.list3)
        self.listView.add_widget(self.list4)
        self.scrollSearch.add_widget(self.listView)
        self.searchBar=MDTextField()
        #self.testbtn=MDRectangleFlatButton(text="Test",pos_hint={"center_x":0.3,"center_y":0.5})#on_release=self.test )

        #Rida


        return self.screen
    def search(self):
        self.screen.search.add_widget(self.scrollSearch)
        self.screen.search.add_widget(self.statLabel)
        self.HasBeenSearched=True



    def tab_switchView(self):
        self.screen.ids.panel.current=("Favorites")
        self.Blayout=MDBoxLayout()
    def tab_switchSave(self):
        self.screen.ids.panel.current=("save")
    def tab_switchTrack(self):
        self.screen.ids.panel.current=("track")
    def tab_switchRecur(self):
        self.screen.ids.panel.current=("search")
    def changeScreen(self):
        self.screen.ids.panel.switch_tab("search")
    def ready(self):
        pass


MyApp().run()
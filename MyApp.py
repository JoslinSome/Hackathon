from kivy import Config
from KvString import *
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivymd.app import MDApp
#from webScraperFile import webScrape
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivymd.uix.card import MDCardSwipe
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
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from webScraperFile import webScrape

SizeList=[]
Clock.max_iteration = 10
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
        self.textField= Builder.load_string(dialogBox1)
       # self.screen.ids.panel.current=("Favorites")
        self.HasBeenSearched=False
        self.BeginningLabel=MDLabel(text="Search a major in search tab to obtain result output",font_style="H5", halign="center",text_color= (0, 0, 1, 1))
        self.addedlist = []
        self.favlistList=[]
        self.searchBar=MDTextField()
        self.theme_cls.primary_palette = "Orange"
        self.trackTrashList=[]
        self.favLists=[]
        #self.testbtn=MDRectangleFlatButton(text="Test",pos_hint={"center_x":0.3,"center_y":0.5})#on_release=self.test )
        self.CurricScroll=ScrollView(pos_hint= {"center_y":0.4}, size_hint_y=0.6)
        self.CurriclsView=MDList()
        self.screen.curriculum.add_widget(self.CurricScroll)
        self.screen.search.add_widget(self.textField)
        self.tempLabel=MDLabel(text="Searching please wait",pos_hint={"center_x":0.5,"center_y":0.8},font_style="H5")
        self.tempLabel1=MDLabel(text="General Curriculum:",pos_hint= {"center_x":0.5,"center_y":0.8},font_style="H5")
        self.CoursesList=[]
        #Rida
        # self.screen.fav.add_widget(self.favbar)
        self.favscroll = ScrollView(pos_hint= {"center_y":0.2}, size_hint_y=0.7)
        self.favlistview = MDList()
        self.favscroll.add_widget(self.favlistview)
        self.emptyfav = MDLabel(text = "Enter a major into the search bar", font_style = "Button",pos_hint= {"center_x":0.66, "center_y": 0.7})
        self.screen.fav.add_widget(self.favscroll)
        self.HasBeenClicked=False

        return self.screen
    def search(self):
         if self.HasBeenSearched:

            for course in self.CoursesList:
                self.CurriclsView.remove_widget(course)
            self.CoursesList=[]

         self.screen.search.add_widget(self.tempLabel)
         user_input1 = self.textField.searchbar.text
         self.start_program = webScrape()
         program_runs = self.start_program.search_major(user_input1)
         if not program_runs:
             print("Could not find major, please re-enter")
         webScrape.search_major(webScrape, self.textField.searchbar.text)
         self.screen.search.remove_widget(self.tempLabel)

         print(self.start_program.reqs_list)
         if not self.HasBeenSearched:
            self.screen.curriculum.add_widget(self.tempLabel1)
            self.CurricScroll.add_widget(self.CurriclsView)
            self.textField.searchbar.text
            self.screen.curriculum.remove_widget(self.BeginningLabel)
         self.HasBeenSearched=True

         for course in self.start_program.reqs_list:
             print(course)
             self.tempLs=OneLineListItem(text=course)
             self.CurriclsView.add_widget(self.tempLs)
             self.CoursesList.append(self.tempLs)

    def addlist(self):
        if self.textField.searchbar.text == "":
            self.screen.fav.add_widget(self.emptyfav)
        else:
            if self.textField.searchbar.text not in self.addedlist:
                icon2 = IconLeftWidget(icon="heart-outline")
                icon = IconRightWidget(icon="trash-can-outline",on_release=self.Delete)
                self.favlist = TwoLineAvatarIconListItem(text = self.textField.searchbar.text,on_touch_up=self.searchFav)
                self.favlistList.append(self.favlist)
                self.trackTrashList.append(icon)
                self.favlist.add_widget(icon2)
                self.favlist.add_widget(icon)
                self.favlistview.add_widget(self.favlist)
                self.addedlist.append(self.textField.searchbar.text)
                self.screen.fav.remove_widget(self.emptyfav)
    def searchFav(self,touch,obj):
        print(touch.text)
        for i in range(len(self.favlistList)):

            if self.favlistList[i].text==touch.text and not self.HasBeenClicked:
                #print(touch.text, " ", self.favlistList[i].text, " ", i)
                self.HasBeenClicked=True
                self.textField.searchbar.text=touch.text
                self.search()
                break
    def Delete(self, touch):
        for i in range(len(self.trackTrashList)):
            if self.trackTrashList[i]==touch:
                self.favlistview.remove_widget(self.favlistList[i])
                del self.trackTrashList[i]
                del self.favlistList[i]
                del self.addedlist[i]
                break
    def tab_switchView(self):
        self.screen.ids.panel.current=("Favorites")
        self.Blayout=MDBoxLayout()
    def tab_switchSave(self):
        self.screen.ids.panel.current=("save")
        self.HasBeenClicked=False
    def tab_switchTrack(self):
        self.screen.ids.panel.current=("track")
        self.HasBeenClicked=False
        if not self.HasBeenSearched:
            self.screen.curriculum.add_widget(self.BeginningLabel)

    def tab_switchRecur(self):
        self.screen.ids.panel.current=("search")
        self.HasBeenClicked=False

    def changeScreen(self):
        self.screen.ids.panel.switch_tab("search")
    def ready(self):
        pass


MyApp().run()



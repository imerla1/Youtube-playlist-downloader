from bs4 import BeautifulSoup
import requests
import re
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.progressbar import ProgressBar
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import os
from bs4 import BeautifulSoup
from pytube import YouTube


def make_subdir(): # This will make subdirectory Where Downloaded Songs will be stored
    path = os.getcwd()
    try:
        subdir = os.mkdir(os.mkdir(path+'\Playlist'))
    except:
        pass

make_subdir()
Window.fullscreen = False
Window.clearcolor = (1, 1, 1, 1)

class YoutubeDownloader(Widget):
    urls_input = ObjectProperty()
    urllist_ = []  # This list stores Every Url from playlist

    def valid_url(self, *args):
        """This function Checks If user Playlist Input is Valid
            Return True if it is valid, Else False"""
        url = self.urls_input.text
        text = 'https://www.youtube.com'
        if text in url:
            return True
        return False

    @property
    def parse_html(self):
        """This function Parse Each Video Link from Playlist"""
        url_ = self.urls_input.text
        req = requests.get(url_)
        soup = BeautifulSoup(req.text, 'html.parser')
        pattern = re.compile(r'href=./watch.+index=[0-9]+').findall(str(soup))


        for i in pattern:
            self.urllist_.append(i.replace('href="', 'youtube.com'))



    def download(self, *args): # With this function we Download Musics
        if self.valid_url():
            self.urllist_ = []
            self.parse_html
            print(self.urllist_)


        else:
            show = YoutubeDownloader()
            popwind = Popup(
                title='Error!', content=Label(
                    text='Please Enter Valid Url'), size_hint=(
                    0.8, 0.2))
            popwind.open()





class BuildApp(App):

    def build(self):
        return YoutubeDownloader()

if __name__ == '__main__':
    BuildApp().run()

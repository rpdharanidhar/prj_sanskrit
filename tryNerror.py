from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Line,Color,InstructionGroup
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.core.audio import SoundLoader
from random import random
from kivy.config import Config
import os

from nltk import app

kv1 = Builder.load_file('tryNerror.kv')

def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if self.ism.focus and keycode == 'enter':
            app.puko()


class MyApp(App):
    def build(self):
        return kv1

if __name__ == "__main__":
    MyApp().run()
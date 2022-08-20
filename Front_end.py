from self import self
from translate import Translator as Tr, translate
import linkgen,sel
import kivy
import cv2
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import word_lib
import fontstyle
import tts
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import auto_stop as sp
import time
import linkgen,sel
import speech_recognition as sr
import cv2
import word_lib
from googletrans import Translator
import pyttsx3 as tts
import tts
import sqlite3


translator = Translator()
# create the recognizer
r = sr.Recognizer()
class MainWindow(Screen):
    m = 0
    def release(self):

        SecondWindow.start(self)

class SecondWindow(Screen):
    #result = "Start"
    def start(self):

        mic = sr.Microphone(device_index=0)
        with mic as source:
            print("start now")
            audio = r.listen(source)
            # print("stop now")

        # speech recognition

        result = r.recognize_google(audio)

        # export the result
        print(result)
        f = open("Lang.txt", "w+")
        f.write(result)
        f.close()

        # ThirdWindow.proper(self)

    # def StopRec(self):
    #     ThirdWindow.enters(self)
    #     print(result)
class ThirdWindow(Screen):
    #a = SecondWindow.result

    # proper(self)
    def proper(self):
        # self.ids.field1.text = "Start to speak..."
        f = open("lang.txt", 'r')
        a = f.readlines()

        for i in a:
            b = a[0]
        print(b)
        self.ids.field1.text  = b

    def translate(self):
        to_trans = self.ids.field1.text
        link = linkgen. link(to_trans)
        sele = sel.sel(link)
        print(sele)
        # text = "भवतः दिवसः अस्ति"
        # rr = text.decode("utf-8"),font_name = 'SANSKRIT.ttf',x = 57

        self.ids.field2.text =sele

    def eng_speak(self):
        tts.text_to_speech(self.ids.field1.text)

    def san_speak(self, fonts1=word_lib):
        sansglish = word_lib.words_change(self.ids.field2.text)
        print(sansglish)
        tts.text_to_speech(sansglish)
        fonts1.print(sansglish)




class WindowManager(ScreenManager):
    pass


kv1 = Builder.load_file('Speech_to_text.kv')
class MyApp(App):
    def build(self):
        return kv1

if __name__ == "__main__":
    MyApp().run()

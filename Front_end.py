from translate import Translator as Tr, translate
import kivy
from kivy.uix.label import Label
from kivy.uix.popup import Popup
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
translator = Translator()
# create the recognizer
r = sr.Recognizer()
class MainWindow(Screen):
    '''def Change(self):
        sp.main()

    def release(self):
        self.ids.mnm.text = "Start to speak..."'''
class SecondWindow(Screen):
    mic = sr.Microphone(device_index=0)
    with mic as source:
        print("start now")
        audio = r.listen(source, phrase_time_limit=10)
        print("stop now")

    try:
        result = r.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        exit("API is unreachable")
    # except KeyboardInterrupt:
    #     print("Audio Recorded")
    except sr.UnknownValueError:
        # speech was unintelligible
        exit("Unable to recognize speech! Were you speaking")

    # speech recognition
    result = r.recognize_google(audio)

    # export the result
    print(result)

    def StopRec(self):
        pass

class ThirdWindow(Screen):
    def translate_to(self, lang, content):
        field = self.root.ids['field2']
        translator = Tr(to_lang=lang)
        translation = translator.translate(content)
        field.text = translation

    def hello_on(self):
        self.ids.field1.text = 'helo'

class WindowManager(ScreenManager):
    pass


kv1 = Builder.load_file('Speech_to_text.kv')
class MyApp(App):
    def build(self):
        return kv1

if __name__ == "__main__":
    MyApp().run()
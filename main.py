import pyttsx3
from plyer import tts
from translate import Translator as Tr, translate
import content as content
import kivy
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.lang.builder import Builder
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen


kvio = Builder.load_file("tnn.kv")
class MyApp(App):
    def build(self):
        Window.size = [1200,600]
        return kvio

    def translate_to(self, lang, content):
        field = self.root.ids['field2']
        translator = Tr(to_lang=lang)
        translation = translator.translate(content)
        field.text = translation
    


class FloatLayout(Widget):
    def hello_on(self):
        self.ids.field1.text = 'helo'











if __name__ == "__main__":
    app = MyApp()
    app.run()

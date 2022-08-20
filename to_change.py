from pyttsx3 import voice

import linkgen,sel
import speech_recognition as sr
import cv2
import word_lib
from googletrans import Translator
import pyttsx3 as tts
import tts
translator = Translator()

link=linkgen.link()
sel=sel.sel(link)
print(sel)
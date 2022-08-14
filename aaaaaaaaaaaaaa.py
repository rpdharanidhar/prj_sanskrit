from pyttsx3 import voice
import multiprocessing
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

# define the microphone
mic = sr.Microphone(device_index=0)


kk=''
kk2=''
def process1():
    kk=r.recognize_google(audio)
    print("hgfgf",kk)
def process2():
    audio2 = r.record(source, duration=4)
# record your speech
with mic as source:
    print("Start speaking")
    audio= r.record(source, duration=4)
    t1 = multiprocessing.Process(target=process1)
   # time.sleep(1)

    t2 = multiprocessing.Process(target=process2)
    t1.start()
    t2.start()

    print("stop now")

print(kk,kk2)
# print(r.recognize_google(audio))
print(1)
# print(r.recognize_google(audio2))
'''try:
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
print(result)'''
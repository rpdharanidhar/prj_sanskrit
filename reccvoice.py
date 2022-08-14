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



# record your speech
with mic as source:
    print("Start speaking")
    audio = r.record(source,duration = 4)
    print(r.recognize_google(audio))
    audio2 = r.record(source,duration = 4)
    print("stop now")
print(r.recognize_google(audio))
print(r.recognize_google(audio2))

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
import fontstyle
import speech_recognition as sr
from googletrans import Translator

import linkgen
import sel
import tts
import word_lib
import cv2

translator = Translator()
# create the recognizer
r = sr.Recognizer()

# define the microphone
mic = sr.Microphone(device_index=0)

print("Start speaking")

# record your speech
with mic as source:
    print("start now")
    audio = r.listen(source,phrase_time_limit=10)
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
with open('my_speech.txt', mode='w') as file:
    file.write(result)

print("The audio has been stored.")

link=linkgen.link(result)
sel=sel.sel(link)
print(sel)
sansglish = word_lib.words_change(sel)
print(sansglish)
tts.text_to_speech(sansglish)
fontstyle.print(sansglish)

#translator.detect(sel)
#playsound in sanskrit

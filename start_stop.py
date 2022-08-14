import cv2
import speech_recognition as sr
def main():

    r=sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something")
        audio = r.listen(source)

        k = cv2.waitKey(1)

        print("U said : \n " +r.recognize_google(audio))



if __name__ == "__main__":
    main()
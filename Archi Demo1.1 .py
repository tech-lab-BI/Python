import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change the voice to the second one

# For audio excute 
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# for wish 
def wish():

    speak("Hi i am Archie")

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning")
    elif hour > 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("How can I help you ??")


# for taking intraction 
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query =  r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except sr.RequestError as e:
            speak("Tell me again, please...")
            return None
#
if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()
        # ... (rest of the code remains the same)
        if "exit" in query:
            break
      
#logic building for tasks

        if "open notepad" in query:
            npath ="C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "open whatsapp" in query:
            wpath = "C:\\Users\\bisha\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(wpath)

        elif "open c plus plus" in query:
            qpath ="C:\\Program Files (x86)\\Embarcadero\\Dev-Cpp\\devcpp.exe"
            os.startfile(qpath)

        elif "open cmd" in query:
            os.system("start cmd")
        
        elif "open webcam" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret , img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif "open chrome" in query:
            cpath = "C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"
            os.startfile(cpath)

        elif "open youtube" in query:   
            ypath = "C:\\Users\\bisha\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\chrome_proxy.exe"
            os.startfile(ypath)

        elif "open photoshop" in query:
            ppath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2023\\Photoshop.exe"
            os.startfile(ppath)

        elif "time" in query:
            speak("The current time is " + datetime.datetime.now().strftime("%H:%M %p"))

        elif "date" in query:
            speak("Today's date is " + datetime.datetime.now().strftime("%d"))
        else :
            speak("Sorry, I didn't get that")
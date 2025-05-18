import speech_recognition as sr
import webbrowser
import musicLibrary
import pyttsx3

#pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(f"Speaking: {text}")
    
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print(f"Received command: {c}") 
    c = c.lower()
    if "google" in c:
        webbrowser.open("https://google.com")
    elif "facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "inkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1] # list ma convert karke 1 means song play song
        link = musicLibrary.music[song]
        webbrowser.open(link)
    else:
        speak("i didnt understand the command")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
       # listen for the wake word "Jarvis"
       #obtain audio from microphone 
       r = sr.Recognizer()
       
        # recognize speech using google
       print("recognizing")
       try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            
                word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

       except Exception as e:
           print("Error; {0}".format(e))


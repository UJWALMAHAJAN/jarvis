import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print(f"Received command: {c}")  # Debugging
    c = c.lower()
    if "google" in c:
        webbrowser.open("https://google.com")
    elif "facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "linkedin" in c:
        webbrowser.open("https://linkedin.com")
    else:
        speak("Sorry, I didn't understand the command.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                wake_word = recognizer.recognize_google(audio)

                if "jarvis" in wake_word.lower():
                    speak("Yes?")
                    print("Jarvis Active...")
                    
                    # Listen for command
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        print(f"Recognized command: {command}")
                        processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand the audio. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")

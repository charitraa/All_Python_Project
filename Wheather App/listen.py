import speech_recognition as sr
import speak

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak.say("Sir, i am Listening tell me the city")
        print("Sir, i am Listening")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"{query}\n")

    except Exception as e:
        print(e)
        speak.say("Say that again please Sir...")
        return "None"
    return query
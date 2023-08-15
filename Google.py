import pywhatkit
import wikipedia
import pyttsx3


def Talk(text):
    rabi = pyttsx3.init('sapi5')
    rime = rabi.getProperty('voices')
    rabi.setProperty('voices', rime[0].id)
    print(text)
    rabi.say(text)
    rabi.runAndWait()


def System():
    search = input('Enter the Query: ')
    pywhatkit.search(search)
    data = wikipedia.summary(search, 2)
    Talk(data)


while True:
    System()

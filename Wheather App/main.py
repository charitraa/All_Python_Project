import json
import requests
import speak
import listen

city = ("hello i am weather API, Please tell me the name of city to know the weather of it")
speak.say(city)
while True:
    
    name = listen.takeCommand().lower()
    if "today" in name:
        speak.say("Ok Sir") 
        break
    else:
        url = f"https://api.weatherapi.com/v1/current.json?key=81b8b97ef83d43fdb8c162524232508&q={name}"
        r = requests.get(url)
        weather = json.loads(r.text)

        celcius = weather["current"]["temp_c"]
        place = weather["location"]["name"]
        fahrenheit=  weather["current"]["temp_f"]
        print("")
        tell = f"temperature of {place} city is {celcius} in celcius and {fahrenheit} in fahrenheit\n"
        print(tell)
        speak.say(tell)
    
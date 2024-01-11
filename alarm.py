from datetime import datetime

from playsound import playsound
# for mp3  #  from playsound import sound

def alarm(time):
    # print("alarm is going to ring")
    alarmTime = str(time)

    while True:
        currentTime = datetime.now().strftime('%I:%M')
        print(currentTime)
        if str(currentTime) == str(alarmTime):
            playsound("C:\\Users\\Lenovo\\Downloads\\alarm.wav")
            
            #sound.playsound("file.mp3")
        elif str(currentTime) > str(alarmTime):
            break


set = input("At what time you want to set alarm: ")

alarm(set)

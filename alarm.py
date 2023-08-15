from datetime import datetime

from playsound import playsound


def alarm(time):
    # print("alarm is going to ring")
    alarmTime = str(time)

    while True:
        currentTime = datetime.now().strftime('%I:%M')
        print(currentTime)
        if str(currentTime) == str(alarmTime):
            playsound("C:\\Users\\Lenovo\\Downloads\\alarm.wav")
        elif str(currentTime) > str(alarmTime):
            break


set = input("At what time you want to set alarm: ")

alarm(set)

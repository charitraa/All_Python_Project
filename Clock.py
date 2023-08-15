from datetime import datetime


def TIme():
    time = datetime.now().strftime("%H:%M:%S")
    print(time)


TIme()

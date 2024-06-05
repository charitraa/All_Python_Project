#making digital watch for my friend

from tkinter import *
from tkinter import ttk
import time


class digitalWatch(Tk):
    def __init__(self):
        super().__init__()


        self.title(' python watch')
        self.resizable(0, 0)
        self.geometry('300x80')
        self['bg'] = 'white'


        self.style = ttk.Style(self)
        self.style.configure(
            'TLabel',
            background = 'white',
            foreground = 'black'
        )

        self.label1 = Label(
            self,
            text=self.time_string(),        
            font=('Digital-7', 40)
        )


        self.label1.pack(expand=True)

        self.label1.after(1000, self.update)

    def time_string(self):
        return time.strftime('%H:%M:%S')

    def update(self):
        """ update the label every 1 second """

        self.label1.configure(text=self.time_string())

        self.label1.after(1000, self.update)


if __name__ == "__main__":
    ws = digitalWatch()
    ws.mainloop()
       

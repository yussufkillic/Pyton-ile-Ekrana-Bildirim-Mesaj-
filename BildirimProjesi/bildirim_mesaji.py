import time
from tkinter import *

hour = int(input("Saat: "))
minute = int (input("Dakika: "))
writing = input("Yazıyı giriniz: ")

while True:
    notification = time.localtime(time.time())

    if hour == notification.tm_hour and minute == notification.tm_min :
        screen = Tk()
        screen.title("Bildirim Ekranı")
        screen.geometry("250x125+1000+500")
        tag = Label(text = writing , font = "Wide 30")
        tag.pack()
        screen.resizable(0,0)
        screen.mainloop()
        break
    else :
        pass
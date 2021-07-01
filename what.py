import tkinter as tk
from tkinter import *
import pywhatkit
import datetime

window = tk.Tk()
window.title('Watsup_message')
window.geometry('600x300')
window['bg'] = 'light grey'

def send_message():
    number = entry1.get()
    mess = text.get("1.0","end")
    x = datetime.datetime.now()
    Hr = int(x.strftime("%H"))
    Mit = int(x.strftime("%M"))
    pywhatkit.sendwhatmsg(number, mess, Hr, Mit+1)


l = Label(window,text='Whatsup Automated Message',bg='red',font=40,height=2)
l.pack(ipadx=20,pady=10)
entry1 = Entry(window,text = 'Number')
entry1.pack(ipadx=20,pady=10)
text = Text(window,width=40,height=3,bg = 'yellow')
text.pack()
button = Button(window, text='Send',command = send_message)
button.pack(ipadx=20,pady=10)


window.mainloop()
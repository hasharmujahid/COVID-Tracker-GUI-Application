"""IMPORT LIBRARIES """
import requests
from tkinter import *

from PIL import Image,ImageTk

""" Creating the Canvas """
root=Tk()
root.geometry("460x570")

root.iconbitmap('icon.ico')
root.title("COVID 19 Tracker")
load = Image.open("background1.jfif")
render = ImageTk.PhotoImage(load)
img = Label(root,image=render)
img.image = render
img.place(x=0, y=0)
"""Add lables"""
welcome=Label(root,text="Hi! Welcome to Covid-19 Tracker",bg='black',fg='white',font=("Roboto 15 italic underline"))
welcome.place(relx=0.1,rely=0.1)
class Data:

    @staticmethod
    def global_stats():
        response = requests.get('https://api.covid19api.com/summary')
        response.raise_for_status()
        data = response.json()['Global']

        print(
            f"New Confirmed : {data['NewConfirmed']} \nTotal Confirmed Cases : {data['TotalConfirmed']} \nNew Deaths : {data['NewDeaths']} \nTotal Deaths : {data['TotalDeaths']} \nDate : {data['Date']}")





button_global=Button(text="Proceed", padx=30, pady=15, fg='black', bg="grey", font=("Consolas 10 bold"),
                             command=Data.global_stats)
button_global.place(relx=0.30, rely=0.45, anchor=CENTER)


root.mainloop()

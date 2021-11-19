"""IMPORT LIBRARIES """
import sys

import requests
from tkinter import *

from PIL import Image, ImageTk

""" Creating the Canvas """
root = Tk()
root.geometry("460x570")

root.iconbitmap('icon.ico')
root.title("COVID 19 Tracker")
load = Image.open("background1.jfif")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.image = render
img.place(x=0, y=0)
"""Add lables"""
welcome = Label(root, text="Hi! Welcome to Covid-19 Tracker", bg='black', fg='white',
                font=("Roboto 15 italic underline"))
welcome.place(relx=0.1, rely=0.1)


class Data:

    @staticmethod
    def global_stats():
        response = requests.get('https://api.covid19api.com/summary')
        response.raise_for_status()
        data = response.json()['Global']
        root2 = Tk()
        root2.geometry("400x300")
        root2.configure(background='black')
        root2.title("Global Statistics")
        root2.iconbitmap('icon.ico')
        lable = Label(root2, text="Covid-19 Global Stats are : ", bg='black', fg='white',
                      font=("Roboto 15 italic underline"))
        lable.place(relx=0.0, rely=0.1)
        lable2 = Label(root2,
                       text=f"New Confirmed : {data['NewConfirmed']} \nTotal Confirmed Cases : {data['TotalConfirmed']} \nNew Deaths : {data['NewDeaths']} \nTotal Deaths : {data['TotalDeaths']} \nDate : {data['Date']}",
                       bg='black', fg='white', font=("Roboto 15 italic underline"))
        lable2.place(relx=0.1, rely=0.28)
        exit_button = Button(root2, text="Exit", padx=30, pady=15, fg='White', bg="grey", font=("Consolas 10 bold"),
                             command=sys.exit)
        exit_button.place(relx=0.35, rely=0.86, anchor='w')

    @staticmethod
    def Countries():
        response = requests.get('https://api.covid19api.com/summary')
        response.raise_for_status()
        root2 = Tk()
        root2.geometry("600x400")
        root2.configure(background='black')
        root2.title("Global Statistics")
        root2.iconbitmap('icon.ico')
        Label_countries = Label(root2, text='Enter Country Name', fg='White', bg='black')
        Label_countries.place(relx=0.4, rely=0.37, anchor=CENTER)
        Country_name = Entry(root2, width=35, borderwidth=4)
        Country_name.place(relx=0.5, rely=0.46, anchor=CENTER)

        def proceed():
            root2.geometry('600x400')
            country_demand = str(Country_name.get())
            Label_countries.destroy()
            Country_name.destroy()
            Proceed.destroy()

            data = response.json()["Countries"]
            for i in data:
                if i['Country'] == str(country_demand):
                    # print(f"Country Name : {i['Country']} \nCountry Code : {i['CountryCode']}  \nCountry ID : {i['ID']}     \nNew Confirmed : {i['NewConfirmed']} \nTotal Confirmed Cases : {i['TotalConfirmed']} \nNew Deaths : {i['NewDeaths']} \nTotal Deaths : {i['TotalDeaths']} \nDate : {i['Date']}")
                    Lable_country = Label(root2,
                                          text=f"Country Name : {i['Country']} \nCountry Code : {i['CountryCode']}  \nCountry ID : {i['ID']}     \nNew Confirmed : {i['NewConfirmed']} \nTotal Confirmed Cases : {i['TotalConfirmed']} \nNew Deaths : {i['NewDeaths']} \nTotal Deaths : {i['TotalDeaths']} \nDate : {i['Date']}",
                                          bg='black', fg='white', font=("Roboto 15 italic underline"))
                    Lable_country.place(relx=0.05, rely=0.15)
            exit_button = Button(root2, text="Exit", padx=30, pady=15, fg='White', bg="grey", font=("Consolas 10 bold"),
                                 command=sys.exit)
            exit_button.place(relx=0.4, rely=0.86, anchor='w')

        Proceed = Button(root2, text="Proceed", padx=30, pady=15, fg='black', bg="grey", font=("Consolas 10 bold"),
                         command=proceed)
        Proceed.place(relx=0.4, rely=0.8)


button_global = Button(text="Global Stats", padx=30, pady=15, fg='black', bg="grey", font=("Consolas 10 bold"),
                       command=Data.global_stats)
button_global.place(relx=0.18, rely=0.4, anchor=CENTER)
button_countries = Button(text="Stats by Countries", padx=30, pady=15, fg='black', bg="grey", font=("Consolas 10 bold"),
                          command=Data.Countries)
button_countries.place(relx=0.78, rely=0.4, anchor=CENTER)

root.mainloop()

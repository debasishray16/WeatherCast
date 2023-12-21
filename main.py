from tkinter import *
import tkinter as tk
from geopy.geocoders import Photon
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime

import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)


def getWeather():
    try:
        city=textfield.get()
    
        geolocator=Photon(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
    
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="Current Time")
    
        # weather
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=0093a72c975dfd0abc2d43dd629f209c"

        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']
    
        t.config(text=(temp,"°"))
        c.config(text=(condition, "|", "Feels", "Like", temp, "°"))
    
        w.config(text=(wind,"kn"))
        h.config(text=(humidity,"%"))
        d.config(text=description)
        p.config(text=(pressure,"mB"))

    
        
    except Exception as e:
        messagebox.showerror("Weather App:","Invalid Entry!!")

# search box
search_image=PhotoImage(file="images/search.png")
my_image=Label(image=search_image)
my_image.place(x=45,y=20)


textfield=tk.Entry(root,justify="left",width=13,font=("poppins",25,"bold"),
                bg="#404040",border=0,fg="white")
textfield.place(x=150,y=35)
# to bring search box inside image.
textfield.focus()


search_icon=PhotoImage(file="images/search_icon.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",
                bg="#404040",command=getWeather)
myimage_icon.place(x=420,y=34)


# logo
logo_image=PhotoImage(file="images/icon_new.png")
logo=Label(image=logo_image,bg="#ffffff")
logo.place(x=300,y=100)


# bottom box
Frame_image=PhotoImage(file="images/box.png")
frame_image=Label(image=Frame_image)
frame_image.pack(padx=5,pady=5,side=BOTTOM)


# time
name=Label(root,font=("Mukta",15,"bold"))
name.place(x=35,y=105)
# clock
clock=Label(root,font=("Hevlvetica",25,"bold"))
clock.place(x=30,y=140)


# Label
label1=Label(root,text="WIND",font=("Ubuntu",13,"bold"),
            fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Ubuntu",13,"bold"),
            fg="white",bg="#1ab5ef")
label2.place(x=255,y=400)

label3=Label(root,text="DESCRIPTION",font=("Ubuntu",13,"bold"),
            fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4 = Label(root, text="PRESSURE", font=("Ubuntu", 13, "bold"), 
            fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

# Corner Data
t=Label(font=("arial",65,"bold"),fg="#ee666d")
t.place(x=600,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=600,y=250)

# Wind data
w=Label(text="...",font=("Ubuntu",16,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)

# Humidity data
h=Label(text="...",font=("Ubuntu",16,"bold"),bg="#1ab5ef")
h.place(x=265,y=430)

# Description data
d=Label(text="...",font=("Ubuntu",16,"bold"),bg="#1ab5ef")
d.place(x=440,y=430)

# Pressure data
p = Label(text="...", font=("Ubuntu", 16, "bold"), bg="#1ab5ef")
p.place(x=660, y=430)


label11=Label(text="Created by: Debasish Ray")
label11.pack(padx=1, pady=1)


root.mainloop()
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
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
    city=textfield.get()
    
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    print(result)



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
logo_image=PhotoImage(file="images/logo.png")
logo=Label(image=logo_image)
logo.place(x=250,y=100)


# bottom box
Frame_image=PhotoImage(file="images/box.png")
frame_image=Label(image=Frame_image)
frame_image.pack(padx=5,pady=5,side=BOTTOM)



# Label
label1=Label(root,text="WIND",font=("Ubuntu",13,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Ubuntu",13,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=245,y=400)

label3=Label(root,text="DESCRIPTION",font=("Ubuntu",13,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4 = Label(root, text="PRESSURE", font=("Ubuntu", 13, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="...",font=("Ubuntu",16,"bold"),bg="#1ab5ef")
w.place(x=130,y=430)

h=Label(text="...",font=("Ubuntu",16,"bold"),bg="#1ab5ef")
h.place(x=265,y=430)

f=Label(text="...",font=("Ubuntu",16,"bold"),bg="#1ab5ef")
f.place(x=450,y=430)

l = Label(text="...", font=("Ubuntu", 16, "bold"), bg="#1ab5ef")
l.place(x=670, y=430)















root.mainloop()
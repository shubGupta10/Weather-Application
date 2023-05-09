# here we imported our package
import tkinter as tk
import requests
from tkinter import font

HEIGHT = 600
WIDTH = 850


def test_function(entry):
    print("This is the Entry", entry)


# 9552b5db143d8dfb4ea47a49cfc4aaba
# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nCondition: %s \nTemperature (C): %s' % (name, desc, temp)
    except:
        final_str = "There is a problem retrieving that data.\n You should try again!!"

    return final_str


def get_weather(city):
    weather_key = '9552b5db143d8dfb4ea47a49cfc4aaba'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)

# relwidth = Relative Width, relheight = Relative height, relx = relative x in cartegsian plane, rely = relative y in plane
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, bg='White', font=40)
entry.pack()
entry.place(relwidth=0.65, relheight=1)

# here we are creating button
# we are putting out button in root , it's like a container
button = tk.Button(frame, text="Search", bg='White', font=('Courier', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.30, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font= ('Courier', 20))
label.place(relwidth=1, relheight=1)

root.mainloop()

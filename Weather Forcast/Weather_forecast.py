from tkinter import *
import datetime as dt
import requests

class Password_Generator:
    def __init__(self,root):
        self.root = root
        self.root.title("Weather Forecast")
        self.root.geometry("370x300")
        self.root.configure(bg = "bisque")

        self.enter_city = Label(self.root, text="Enter City:", font="Arial, 15 bold", fg="black", bjg = "bisque")
        self.enter_city.place(x=20, y=10)

        self.city_name_input = Entry(self.root, font="Arial, 10 bold",bg = "azure", width = 20)
        self.city_name_input.place(x=20, y=40)

        self.generate_button = Button(self.root, text="Generate Weather Forecast", command=self.weather_forecast, width=23, font="Arial, 10 bold",fg = "white", bg = "red3")
        self.generate_button.place(relx=0.5, rely=0.3, anchor="center")

        self.generated_weather_forecast = Label(self.root, text="", font="Arial, 12 bold", fg="red3", bg = "bisque", justify = "left")
        self.generated_weather_forecast.place(x=20, y=130)

    def weather_forecast(self):
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = self.city_name_input.get()
        api_key = "d86c1fb3fffed4c920ec2faa2fe16941"

        url = base_url + "appid=" + api_key + "&q=" + city_name

        data = requests.get(url).json()

        def kelvin_to_celsius_fahrenheit(kelvin):
            celsius = kelvin - 273
            fahrenheit = celsius * (9/5) + 32
            return celsius, fahrenheit

        temp_kelvin = data['main']['temp']
        temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
        feels_like_kelvin = data['main']['feels_like']
        feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
        wind_speed = data['wind']['speed']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        sun_rise_time = dt.datetime.utcfromtimestamp(data['sys']['sunrise']+data['timezone'])
        sun_set_time = dt.datetime.utcfromtimestamp(data['sys']['sunset']+data['timezone'])

        forecast = f"""Temperature : {temp_celsius:.2f}'C or {temp_fahrenheit:.2f}'F
Feels Like : {feels_like_celsius:.2f}'C or {feels_like_fahrenheit:.2f}'F
Wind Speed : {wind_speed}
Humidity : {humidity}
Description : {description}
Sun rise time : {sun_rise_time} local time
Sun set time : {sun_set_time} local time"""

        self.generated_weather_forecast.config(text=forecast)

if __name__ == "__main__":
    root = Tk()
    psword_generator = Password_Generator(root)
    root.mainloop()


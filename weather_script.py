# Fetch weather data from OpenWeatherMap API
# Code should include functionality for making API requests and processing retrieved data to display weathen information like temperature, humidity, and weather conditions.
import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = 'a527c9b43b6317387cb5086be0cf9d02'
# API_KEY = os.getenv('OPENWEATHER_API_KEY')  # Read API key from environment variable


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }
        return weagithub-cloudlabsuser-1306her
    except Exception as e:
        print("Error:", e)  # Add this line to see the error in the terminal
        return None

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        self.geometry("300x250")
        self.resizable(False, False)

        self.city_entry = tk.Entry(self, width=20, font=('Arial', 14))
        self.city_entry.pack(pady=10)

        self.search_btn = tk.Button(self, text="Get Weather", command=self.show_weather)
        self.search_btn.pack(pady=5)

        self.result_label = tk.Label(self, text="", font=('Arial', 12))
        self.result_label.pack(pady=10)

    def show_weather(self):
        city = self.city_entry.get()
        weather = get_weather(city)
        if weather:
            result = (
                f"City: {weather['city']}\n"
                f"Temperature: {weather['temperature']}°C\n"
                f"Humidity: {weather['humidity']}%\n"
                f"Condition: {weather['description'].title()}"
            )
            self.result_label.config(text=result)
        else:
            messagebox.showerror("Error", "Could not retrieve weather data.")

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
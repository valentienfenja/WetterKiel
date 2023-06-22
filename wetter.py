import requests
from bs4 import BeautifulSoup
import tkinter as tk
from datetime import datetime

temp = 0 

def get_weather_data():
    url = "https://www.wetteronline.de/wetter/kiel"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        current_weather = soup.find("div", id="nowcast-content")
        
        forecast_data = []
        #forecast_elements = soup.find_all("div", class_="dayForecast")
        #forecast_elements = soup.find_all("div", class_="leftflowheadline-wrappervisible")
        #forecast_elements = soup.find_all("div", class_="forecastvisible")

       
        day = datetime.today().strftime('%A')
        temperature = soup.find("div", class_="value").get_text()
        print(temperature)
        forecast_data.append({"day": day, "temperature": temperature})


        return current_weather, forecast_data

    return None, None

def show_weather():
    current_weather, forecast_data = get_weather_data()

    if current_weather and forecast_data:
        weather_window = tk.Toplevel()
        weather_window.title("WetterKiel")

        current_weather_label = tk.Label(weather_window, text=f"Aktuelles Wetter in Kiel: {current_weather}")
        current_weather_label.pack()

        forecast_label = tk.Label(weather_window, text="Vorhersage für die nächsten Tage:")
        forecast_label.pack()

        for forecast in forecast_data:
            day_label = tk.Label(weather_window, text=f"{forecast['day']}: {forecast['temperature']}")
            day_label.pack()

    else:
        error_label = tk.Label(root, text="Fehler beim Abrufen der Wetterdaten")
        error_label.pack()

root = tk.Tk()
root.title("Wetterdaten abrufen")

get_weather_button = tk.Button(root, text="Wetter anzeigen", command=show_weather)
get_weather_button.pack()

root.mainloop()

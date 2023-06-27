import requests
from fastapi import HTTPException
from datetime import datetime as dt


def weather_data(city: str):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "785ccfbcc45da84b26fd5b66eec48b29"

    url = f"{base_url}appid={api_key}&q={city}&units=metric"
    response = requests.get(url)

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Invalid city name")
    response = response.json()

    return {
        "sunrise": dt.fromtimestamp(response["sys"]["sunrise"]),
        "sunset": dt.fromtimestamp(response["sys"]["sunset"]),
        "temperature": response["main"]["temp"],
        "pressure": response["main"]["pressure"],
        "humidity": response["main"]["humidity"],
        "clouds": response["clouds"]["all"],
        "wind_speed": response["wind"]["speed"],
        "rain": response.get("rain", {}).get("1h", 0),
        "snow": response.get("snow", {}).get("1h", 0)
    }

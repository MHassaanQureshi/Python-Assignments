import streamlit as st  
import requests


st.set_page_config(page_title="Weather App", layout="wide")
API_KEY = "d1c85ecd0c46471fa8d103956252702"
BASE_URL = "https://api.weatherapi.com/v1/current.json"
def get_weather(city):
    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "no"
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

st.title("🌤️ Weather App")

city_name = st.text_input("Enter city name:", "")

if st.button("Get Weather"):
    if city_name:
        weather_data = get_weather(city_name)
        
        if weather_data:
            location = weather_data["location"]["name"]
            country = weather_data["location"]["country"]
            temp_c = weather_data["current"]["temp_c"]
            condition = weather_data["current"]["condition"]["text"]
            humidity = weather_data["current"]["humidity"]
            wind_kph = weather_data["current"]["wind_kph"]
            icon_url = "https:" + weather_data["current"]["condition"]["icon"]

            
            st.subheader(f"Weather in {location}, {country}")
            st.image(icon_url, width=80)
            st.write(f"🌡️ **Temperature:** {temp_c}°C")
            st.write(f"☁️ **Condition:** {condition}")
            st.write(f"💧 **Humidity:** {humidity}%")
            st.write(f"💨 **Wind Speed:** {wind_kph} km/h")

        else:
            st.error("❌ Could not fetch weather data. Check city name or try again later.")
    else:
        st.warning("⚠️ Please enter a city name.")


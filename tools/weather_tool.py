"""Weather tool for fetching weather information."""
import requests
from smolagents import tool
from config.settings import OPENWEATHER_API_KEY


@tool
def get_weather(data: dict, ctx: dict) -> dict:
    """
    Fetch current weather from OpenWeatherMap and update context.

    Args:
        data (dict): Contains 'location' with 'lat' and 'lon'.
        ctx (dict): User context to update.

    Returns:
        dict: Weather info including 'city', 'temp', 'condition', and 'wind_kph'.
    """
    loc = data.get('location', {})
    lat = loc.get('lat')
    lon = loc.get('lon')
    
    if lat is None or lon is None:
        return {"error": "Location not provided"}
    
    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"lat": lat, "lon": lon, "units": "metric", "appid": OPENWEATHER_API_KEY},
            timeout=5
        )
        response.raise_for_status()
        data = response.json()
        
        info = {
            "city": data.get("name", ""),
            "temp": data["main"]["temp"],
            "condition": data["weather"][0]["description"],
            "wind_kph": round(data["wind"]["speed"] * 3.6, 1)
        }
        ctx['weather'] = info
        return info
        
    except Exception as e:
        return {"error": str(e)}
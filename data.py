import json
import urllib.request

def fetch_weather_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=60.9827&longitude=25.6612&current=temperature_2m"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

            current_temp = data["current"]["temperature_2m"]
            temp_unit = data["current_units"]["temperature_2m"]

            print("Well Done. Data Fetched")
            print(f"Current Temparature of Lahti is :{current_temp}{temp_unit}") 

    except Exception as e:
        print (f"Error fetching data: {e}")


if __name__ == "__main__":
     fetch_weather_data()
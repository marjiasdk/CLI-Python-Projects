"""

This is a simple CLI weather forecast application that uses the OpenWeatherMap API to retrieve weather data for a given city.
The user can input the following: city name and units of measurement.
The application will return the following: city name, country code, current temperature, minimum temperature, maximum temperature, and weather description.

Example Input: python cli_weather_forecast.py London metric
Example Output: City: London
                Country code: GB
                Current temperature: 10.01
                Minimum temperature: 8.89
                Maximum temperature: 11.67
                Weather description: overcast clouds
                * The dictionary will be printed to a text file called weather_forecast.txt

"""

with open('api_key.txt', 'r') as f:
    api_key = f.read()
    
# requests module allows you to send HTTP requests using Python
import requests
# argparse module makes it easy to write user-friendly command-line interfaces
import argparse

# Create parser object
parser = argparse.ArgumentParser()
parser.add_argument('city', type=str, help='City name')
parser.add_argument('units', type=str, help='Units of measurement')
args = parser.parse_args()

# API call to OpenWeatherMap
url = f'http://api.openweathermap.org/data/2.5/weather?q={args.city},&units={args.units}&appid={api_key}'    
response = requests.get(url)

# Convert JSON data to Python dictionary
data = response.json()
# I want to print the dictionary to a text file
# I do not want it to be rewritten when I run the program again
with open('weather_forecast.txt', 'a') as f:
    f.write(str(data))
    f.write('\n')
# I want to print the city name
print(f'City: {data["name"]}')
# I want to print the country code
print(f'Country code: {data["sys"]["country"]}')
# I want to print the current temperature
print(f'Current temperature: {data["main"]["temp"]}')
# I want to print the minimum temperature
print(f'Minimum temperature: {data["main"]["temp_min"]}')
# I want to print the maximum temperature
print(f'Maximum temperature: {data["main"]["temp_max"]}')
# I want to print the weather description
print(f'Weather description: {data["weather"][0]["description"]}')
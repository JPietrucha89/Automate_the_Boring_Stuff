# Overall, the program does the following:
#   Downloads JSON weather data from OpenWeatherMap.org
#   Converts the string of JSON data to a Python data structure
#   Prints the weather for today and the next two days

# So the code will need to do the following:
# Call requests.get() to download the weather data.
# Call json.loads() to convert the JSON data to a Python data structure.
# Print the weather forecast.

import json
import requests
import credentials
# print(credentials.APP_ID)

print('Podaj lokalizację zgodnie z konwencją "CITY, XX" gdzie XX to 2 znakowy kod kraju (np. PL):')
#location = input()
location = 'Wilanów, PL'
cityName = location.strip()
cnt = 5  # number of sets of weather information

# Download JSON weather data from OpenWeatherMap.org
# Call requests.get() to download the weather data.
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={cityName}&cnt={cnt}&appid={credentials.APP_ID}'
response = requests.get(URL)
response.raise_for_status()
# See the raw JSON text:
# print(response.text)

# Convert the string of JSON data to a Python data structure
# Call json.loads() to convert the JSON data to a Python data structure.
weatherData = json.loads(response.text)
# print(weatherData)

# used to create list of dictionaries because weatherData has key 'list'
w = weatherData['list']
# w[0], w[1], and w[2] to retrieve the dictionaries for first, second, and third set of weather info

# Print the weather for all sets of weather information
for i in range(cnt):
    print(f'Pogoda w {location} o godzinie ' + w[i]['dt_txt'] + ':')
    print('\t' + w[i]['weather'][0]['main'], '-', w[i]['weather'][0]
          ['description'], '- temperatura wynosi: ', round(w[i]['main']['temp']-273.15, 2))

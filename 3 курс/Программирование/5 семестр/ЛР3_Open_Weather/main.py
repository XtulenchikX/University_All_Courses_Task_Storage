import os

from getweatherdata import get_weather_data

def main():
  API = os.environ['API']

  city = "Moscow"
  city1 = "Чикаго"
  city2 = "Санкт-Петербург"
  city3 = "Дакка"

  print(get_weather_data(city, API))
  print(get_weather_data(city1, API))
  print(get_weather_data(city2, API))
  print(get_weather_data(city3, API))

if __name__ == '__main__':
  main()
  
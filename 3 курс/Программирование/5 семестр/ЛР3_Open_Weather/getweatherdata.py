def get_weather_data(city, api_key=None):
  """
  Получает данные о погоде для заданного города, используя API OpenWeatherMap.

  Parameters
  ----------
  city : str
      Город, для которого нужно получить данные о погоде.

  api_key : str, optional
      Ключ API OpenWeatherMap (по умолчанию None).

  Returns
  -------
  str or None
      Если запрос выполнен успешно, данные о погоде в формате JSON будут возвращены в виде строки. В случае ошибки, функция вернет None и выведет сообщение об ошибке.
  """
  
  import requests
  import json

  try:
    res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    )
    res.raise_for_status()
    data = res.json()
    weather_data = {
        "name": data['name'],
        "coord": data['coord'],
        "country": data['sys']['country'],
        "feels_like": data['main']['feels_like'],
        'timezone': f'UTC{int(data["timezone"] / 3600):+d}'
    }
    return json.dumps(weather_data, indent=2, ensure_ascii=False)

  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    return None

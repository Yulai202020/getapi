from pprint import pprint
import requests

data = requests.get(f"https://icanhazdadjoke.com/",headers = {"Accept": "application/json"}).json()
pprint(data)

# https://www.cbr-xml-daily.ru/daily_json.js стоимость валют
# https://namaztimes.kz/ru/country?type=json список стран
# https://api.adviceslip.com/advice рандомные советы
# https://icanhazdadjoke.com/ 

# https://developer.marvel.com/ комиксы
# https://developer.marvel.com/documentation/getting_started документация

# https://covid-19.dataflowkit.com/v1/world короновирус
# или https://covid-19.dataflowkit.com/v1/{название страны}


# https://funtranslations.com/ документация
# https://deckofcardsapi.com/ документация
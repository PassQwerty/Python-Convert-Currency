# https://dtf.ru/flood/1151637-parsing-kursov-valyut

import requests
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

print(data['Valute']['USD']['Value'])
print(data['Valute']['USD']['Value'])

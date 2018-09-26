import requests
import json
import settings

s = requests.get("https://api-metrika.yandex.ru/stat/v1/data?dimensions=ym:s:searchEngineName&metrics=ym:s:visits,ym:s:users&filters=ym:s:trafficSourceName=='Переходы из поисковых систем'&id=48348170&oauth_token=AQAAAAAUZLkVAAU3cWSo3bRtVURQrKLg0QzFVL8")
data = s.json()
print(data)
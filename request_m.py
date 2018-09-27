import requests
import json
import settings

s = requests.get("https://api-metrika.yandex.ru/stat/v1/data?dimensions=ym:s:lastSearchEngine,ym:s:startURL&metrics=ym:s:visits&filters=ym:s:startURL=@%27keune%27&id=48348170&oauth_token=AQAAAAAUZLkVAAU3cWSo3bRtVURQrKLg0QzFVL8&pretty=true")
data = s.json()
print(data)

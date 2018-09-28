import requests
import json

s = requests.get("https://api-metrika.yandex.ru/stat/v1/data?dimensions=ym:s:lastSearchEngineRoot&metrics=ym:s:visits&filters=ym:s:startURL=@%27keune%27+AND+ym:s:lastSearchEngineRoot==%27yandex%27&id=48348170&oauth_token=AQAAAAAUZLkVAAU3cWSo3bRtVURQrKLg0QzFVL8&pretty=true")
data = s.json()
print('Трафик за неделю с Яндекса - {} визитов'.format(int(data["data"][0]['metrics'][0])))
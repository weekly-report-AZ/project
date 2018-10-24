# -*- coding: utf-8 -*-
import requests
import ym_const


def main_ym(key):
    url = 'https://api-metrika.yandex.ru/stat/v1/data?dimensions=ym:s:lastSearchEngineRoot&metrics=ym:s:visits' \
          '&filters=ym:s:startURL=@%27{0}%27+AND+ym:s:lastSearchEngineRoot==%27yandex%27&id=48348170&' \
          'oauth_token={1}&pretty=true'.format(key, ym_const.TOKEN)
    s = requests.get(url)
    data = s.json()
    if not data['data']:
        k = 0
    else:
        k = int(data["data"][0]['metrics'][0])
    return k


if __name__ == '__main__':
    main = main_ym('keune')
    print(main)

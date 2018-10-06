# -*- coding: utf-8 -*-
import csv
import datetime
import request_ga
import request_ym

#запись в переменную сегодняшней даты в формате год/месяц/день
now = datetime.datetime.today().strftime('%d.%m.%Y %H:%M')
with open('brand.txt', 'r', encoding='utf-8') as r:
    for line in r:
        line = line.replace('\n', '')
        print(line, request_ga.main_ga(line))
        print(line, request_ym.main_ym(line))
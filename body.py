#!/Users/azuev/projects/weekly_report/env/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime
import csv
import os
import request_ga
import request_ym

begin = datetime.today()
dict_res_y = {'date': begin}
dict_res_g = {'date': begin}
fields = ['date']
# чтение файла
with open('brand.txt', 'r', encoding='utf-8') as r:
    for line in r:
        line = line.replace('\n', '')
        # добавление в список нового ключа
        fields.append(line)
        # запрос к api ga
        g = request_ga.main_ga(line)
        print(line, 'g:', g)
        # запись в словарь названия шаблона url и соответствующего значения по траифику из google за неделю
        dict_res_g[line] = g
        # запрос к api ям
        y = request_ym.main_ym(line)
        print(line, 'y:', y)
        # запись в словарь названия шаблона url и соответствующего значения по траифику из yandex за неделю
        dict_res_y[line] = y
print(fields)
print(dict_res_y)
print(dict_res_g)
if os.path.isfile('/Users/azuev/projects/weekly_report/report_g.csv') == False:
    with open('report_g.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        writer.writerow(dict_res_g)
else:
    with open('report_g.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writerow(dict_res_g)
if os.path.isfile('/Users/azuev/projects/weekly_report/report_y.csv') == False:
    with open('report_y.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        writer.writerow(dict_res_y)
else:
    with open('report_y.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writerow(dict_res_y)
end = datetime.today()
delta = end - begin
print('время работы скрипта {0} минут {1} секунд'.format(delta.seconds // 60, delta.seconds % 60))

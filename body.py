# -*- coding: utf-8 -*-
import csv
import datetime
import request_ga
import request_ym

# запись в переменную сегодняшней даты в формате год/месяц/день
begin = str(datetime.datetime.today().strftime('%d.%m.%Y %H:%M'))
print(begin)
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
with open('report_g.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    writer.writerow(dict_res_g)
with open('report_y.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    writer.writerow(dict_res_y)
end = str(datetime.datetime.today().strftime('%d.%m.%Y %H:%M'))
print(end)

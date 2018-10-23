#!/Users/azuev/projects/weekly_report/env/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime
from multiprocessing import Pool
import os

import openpyxl

import request_ga
import request_ym

begin = datetime.today()
# время запуска скрипта
date = begin.strftime('%d.%m.%Y %H:%M')
print(date)
# добавление времени запуска скрипта в словарь с результатами
dict_res_y = {'date': date}
dict_res_g = {'date': date}
list_all = ['date']
# чтение файла с url
with open('brand.txt', 'r', encoding='utf-8') as r:
    content = r.read()
    list_url = content.split('\n')
    print(list_url)
    # создание объекта Pool на несколько процессов
    pool = Pool(processes=10)
    # запрос к api ga с учетом мультипроцессинга
    g = pool.map(request_ga.main_ga, list_url)
    for url_idx, url in enumerate(list_url):
        # запись в словарь названия шаблона url и соответствующего значения по траифику из google за неделю
        dict_res_g[url] = g[url_idx]
        print(list_url[url_idx], 'g:', g[url_idx])
    pool = Pool(processes=10)
    # запрос к api ям с учетом мультипроцессинга
    y = pool.map(request_ym.main_ym, list_url)
    for url_idx, url in enumerate(list_url):
        # запись в словарь названия шаблона url и соответствующего значения по трафику из yandex за неделю
        dict_res_y[url] = y[url_idx]
        print(list_url[url_idx], 'y:', y[url_idx])
print(dict_res_y)
print(dict_res_g)
# формирования списка полей из шаблонов url и даты запуска
list_all = list_all + list_url
len_list = len(list_all)
# если файл отчета еще не существует, то создаем report.xlsx записываем результаты в 2 вкладки
if os.path.isfile('/Users/azuev/projects/weekly_report/report.xlsx') is False:
    workbook = openpyxl.Workbook()
    worksheet_y = workbook.active
    worksheet_y.title = 'Yandex'
    worksheet_g = workbook.create_sheet(title='Google')
    i = 0
    for i in range(1, len_list + 1):
        worksheet_y.cell(row=1, column=i).value = list_all[i - 1]
        worksheet_y.cell(row=2, column=i).value = dict_res_y[list_all[i - 1]]
        worksheet_g.cell(row=1, column=i).value = list_all[i - 1]
        worksheet_g.cell(row=2, column=i).value = dict_res_g[list_all[i - 1]]
        workbook.save('report.xlsx')
# если файл отчета уже существует, то дозаписываем в него новые данные
else:
    workbook = openpyxl.load_workbook('report.xlsx')
    worksheet_y = workbook['Yandex']
    worksheet_g = workbook['Google']
    row_y = []
    row_g = []
    for i in range(1, len_list + 1):
        row_y.append(dict_res_y[list_all[i - 1]])
        row_g.append(dict_res_g[list_all[i - 1]])
    worksheet_y.append(row_y)
    worksheet_g.append(row_g)
    workbook.save('report.xlsx')
# время окончания работы скрипта
end = datetime.today()
date_2 = end.strftime('%d.%m.%Y %H:%M')
print(date_2)
delta = end - begin
# вывод длительности работы скрипта
print('время работы скрипта {0} минут {1} секунд'.format(delta.seconds // 60, delta.seconds % 60))

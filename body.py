#!/Users/azuev/projects/weekly_report/env/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime
import csv
from multiprocessing import Pool
import os
import request_ga
import request_ym

begin = datetime.today()
date = begin.strftime('%d.%m.%Y %H:%M')
print(date)
dict_res_y = {'date': date}
dict_res_g = {'date': date}
list_all = ['date']
# чтение файла
with open('brand.txt', 'r', encoding='utf-8') as r:
    content = r.read()
    list_url = content.split()
    print(list_url)
    pool = Pool(processes=10)
    # запрос к api ga
    g = pool.map(request_ga.main_ga, list_url)
    for url_idx, url in enumerate(list_url):
        # запись в словарь названия шаблона url и соответствующего значения по траифику из google за неделю
        dict_res_g[url] = g[url_idx]
        print(list_url[url_idx], 'g:', g[url_idx])
    pool = Pool(processes=10)
    # запрос к api ям
    y = pool.map(request_ym.main_ym, list_url)
    for url_idx, url in enumerate(list_url):
        # запись в словарь названия шаблона url и соответствующего значения по траифику из yandex за неделю
        dict_res_y[url] = y[url_idx]
        print(list_url[url_idx], 'y:', y[url_idx])
print(dict_res_y)
print(dict_res_g)
list_all = list_all + list_url
if os.path.isfile('/Users/azuev/projects/weekly_report/report_g.csv') is False:
    with open('report_g.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, list_all, delimiter=';')
        writer.writeheader()
        writer.writerow(dict_res_g)
else:
    with open('report_g.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, list_all, delimiter=';')
        writer.writerow(dict_res_g)
if os.path.isfile('/Users/azuev/projects/weekly_report/report_y.csv') is False:
    with open('report_y.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, list_all, delimiter=';')
        writer.writeheader()
        writer.writerow(dict_res_y)
else:
    with open('report_y.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, list_all, delimiter=';')
        writer.writerow(dict_res_y)
end = datetime.today()
date_2 = end.strftime('%d.%m.%Y %H:%M')
print(date_2)
delta = end - begin
print('время работы скрипта {0} минут {1} секунд'.format(delta.seconds // 60, delta.seconds % 60))

error: failed to push some refs to 'https://github.com/weekly-report-AZ/project.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details

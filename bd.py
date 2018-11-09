import sqlite3

from settings import DB_NAME


def check_or_create_db():
    with sqlite3.connect(DB_NAME) as conn:
        # Создаем таблицы для Yandex и Google
        tables = ['yandex', 'google']

        for table in tables:
            conn.cursor().execute(("""CREATE TABLE IF NOT EXISTS {}
                                  (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                   date text,
                                   url_id int,
                                   traffic int)""".format(table)
                                   ))

        # Создаем таблицу для URL

        conn.cursor().execute(("""CREATE TABLE IF NOT EXISTS urls
                                          (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                           url text)"""
                               ))

# Проверяем на наличие URL или добавляем новый в БД
def check_or_add_url(url_name, conn):
    url = conn.cursor().execute('SELECT url FROM urls WHERE url = ? ', (url_name,)).fetchone()
    if not url:
        conn.cursor().execute("INSERT INTO urls (url)   VALUES (?)",
                              (url_name,))

# Записываем данные в таблицу
def add_data_to_db(data, table):

    # "Вырезаем" дату из данных
    data = data.copy()
    date = data['date']
    del data['date']

    # Записываем остальные данные в таблицу
    with sqlite3.connect(DB_NAME) as conn:
        for url in data.keys():
            check_or_add_url(url_name=url, conn=conn)
            url_id = conn.cursor().execute('SELECT id FROM urls WHERE url = ? ', (url,)).fetchone()[0]
            conn.cursor().execute("INSERT INTO {} (date, url_id, traffic)   VALUES (?,?,?)".format(table),
                                  (date, url_id, data[url]))
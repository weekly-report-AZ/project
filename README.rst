WeeklyReport
============

WeeklyReport - это скрипт для получения по почте отчета с показателеми органического трафика Яндекс и Google за неделю
для масок URL сайта записаных в файл.

Установка
---------

Создайте виртуальное окружение и активируйте его. Потом в виртуальном окружении выполните:

.. code-block:: text

    pip install -r requirements.txt


Настройка
---------

* Положите в директорию файл c URL url.txt, каждая маска URL хранится в отдельной строке.

* Получите доступ к api и токен авторизации приложения Яндекс метрика. Документация https://tech.yandex.ru/metrika/

* Получите доступ к api и токен авторизации для Google Analitics. Сохраните файл ключа в директории. Документация https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py

* Создайте файл settings.py и добавьте туда следующие настройки:

.. code-block:: python

    ADDR_FROM = 'почта отправителя'

    ADDR_TO = ['почта получателя1', 'почта получателя1']

    PASSWORD = 'пароль'

    FILEPATH = 'report.xlsx'

    TOKEN = 'отладочный токен Яндекс Метрики'

Запуск
------

1. В активированном виртуальном окружении выполните:

.. code-block:: text

    python3 body.py

2. При необходимости создайте файл crontab для еженедельного запуска по расписанию при помощи команды crontab -e в консоле


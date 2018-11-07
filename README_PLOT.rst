Plot
======

Plot это скрипт для визуализации данных с результатами работы основного скрипта.
Показатели органического трафика по Яндекс и Google отображаются на отдельных графиках.
Можно выбрать те маски URL, для которых вы хотите построить графики, по умолчанию графики строятся для всех масок.


Установка дополнительных пакетов
--------------------------------

.. code-block:: text

   pip install dash==0.28.5
   pip install dash-html-components==0.13.2
   pip install dash-core-components==0.34.0
   pip install xlrd

Запуск скрипта
--------------

    python plot.py

.. code-block:: text

    * Serving Flask app "plot" (lazy loading)
    * Environment: production
      WARNING: Do not use the development server in a production environment.
      Use a production WSGI server instead.
    * Debug mode: on
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 549-150-689
    * Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)

Использование
-------------

    В браузере перейти по адресу:

    http://127.0.0.1:8050/

    При нажатии Update построение графиков осуществляеется заново

Завершение работы скрипта:
--------------------------

    CTRL + C

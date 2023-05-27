# Лабораторная работа. Тестирование

__Автор:__ Стецук Максим 2гр.1п.гр.

__NEW: Добавлено тестирование для функций считывания и записи в файл: "Test_write_log.py" и "Test_read_params.py".__

*__Информация о калькуляторе:__*

'+' : сложение

'-' : вычитание

'*' : умножение

'/' : деление

'//' : целочисленное деление

'%' : остаток от деления

'std_dev' : стандартное отклонение

'batch_calc' : вычисление выражений из файла

__Запуск тестов (производится введением команды в Shell):__

*unittest:*

python Test_calculate.py

python Test_convert_precision.py

python Test_std_dev.py

*pytest:*

python -m pytest Test_calculate.py

python -m pytest Test_convert_precision.py

python -m pytest Test_std_dev.py
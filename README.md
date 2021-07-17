## Решение [домашнего задания](https://github.com/netology-code/py-homeworks-advanced/tree/master/1.Import.Module.Package) к лекции «Import. Module. Package»
  1. "При вызове функций модуля [main.py](https://github.com/headsoft-mikhail/adpy_01/blob/main/imports/main.py) выводить текущую дату" - вывожу дату и время в выбранном формате
  1. 4 пункт не совсем понял, но в [dirty_main.py](https://github.com/headsoft-mikhail/adpy_01/blob/main/imports/dirty_main.py) попробовал сделать импорт с помощью конструкции from packages import * и файл [\_\_init__.py](https://github.com/headsoft-mikhail/adpy_01/blob/main/imports/application/__init__.py)
  1. Чтобы загрузить пустую директорию на GitHub, создал в ней временный пустой файл
  
## Решение [домашнего задания](https://github.com/netology-code/py-homeworks-advanced/tree/master/5.Regexp) к лекции «Regular expressions»
  1. Код для чтения данных из файла и записи в файл был вынесен в функции read_list_from_csv и save_list_to_csv. Для записи добавлен параметр newline='' для удаления пустых строк в сохраненном файле.
  2. Исправление формата ФИО и телефонных номеров решено с помощью регулярных выражений в функциях fix_names и fix_phone_numbers, которые принимают на вход список данных (кроме первой строки - шапки таблицы)
  3. Как применить регулярные выражения в борьбе с дубликатами не придумал, поэтому решил через группировку (groupby) и циклы в функции fix_repeats
  4. Сохраненный файл: "[phonebook.csv](https://github.com/headsoft-mikhail/adpy_01/blob/main/reg_exp/phonebook.csv)"
  5. Файл с кодом: "[regular_expressions.py](https://github.com/headsoft-mikhail/adpy_01/blob/main/reg_exp/regular_expressions.py)" 
  
## Решение [домашнего задания](https://github.com/netology-code/py-homeworks-advanced/tree/master/2.Iterators.Generators.Yield) к лекции «Iterators. Generators. Yield»
  1. Файлы, относящиеся к заданию по итераторам и генераторам [здесь](https://github.com/headsoft-mikhail/adpy_01/tree/main/iterators_generators)
  1. Класс итератора реализован в файле [iterator.py](https://github.com/headsoft-mikhail/adpy_01/blob/main/iterators_generators/iterator.py). При создании экземпляра можно указать (а можно не указывать) начальный и/или конечный элемент по которому итерироваться. Результат (название страны+ссылка wikipedia) записываются в файл [countries.txt](https://github.com/headsoft-mikhail/adpy_01/blob/main/iterators_generators/countries.txt). Создание экземпляра итератор и само итерирование  - в файле [main.py](https://github.com/headsoft-mikhail/adpy_01/blob/main/iterators_generators/main.py) 
  1. Там же, в [main.py](https://github.com/headsoft-mikhail/adpy_01/blob/main/iterators_generators/main.py) реализована функция-генератор hash_generator(file_path)

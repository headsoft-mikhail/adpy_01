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

## Решение [домашнего задания](https://github.com/netology-code/py-homeworks-advanced/tree/master/4.Tests) к лекции «Tests»
  Файлы, относящиеся к заданию по тестированию [здесь](https://github.com/headsoft-mikhail/adpy_01/tree/main/testing)
  ###  Проверка приложения secretary
   За основу приложения secretary был взят предложенный файл [app.py](https://github.com/netology-code/py-homeworks-advanced/blob/master/4.Tests/src/app.py).  
   В моем проекте он называется [secretary.py](https://github.com/headsoft-mikhail/adpy_01/blob/main/testing/secretary.py).  
   Файл с тестами - [testing_secretary.py](https://github.com/headsoft-mikhail/adpy_01/blob/main/testing/testing_secretary.py). 
  * remove_doc_from_shelf - если существует возможность нахождения одного документа в нескольких папках, то удалится первая найденная запись, а вторая останется
  * delete_doc - если пользователь попытается удалить несуществующий документ, функция вернет не кортеж doc_number, deleted_state, а None, что вызовет ошибку, или потребует проверки if not None. Правильнее было бы возвращать кортеж doc_number, False
  * get_doc_shelf
    -  выводит название полки если документ не существует, хотя есть отметка о размещении его в директории, При этом нужно определить, как должен вести себя данный метод: в идеале - исправлять это, т.е. удалять эту отметку, либо выводить сообщение об обнаруженном несоответствии, либо если работать "в лоб" (что наверное неправильно) то все-таки выводить номер полки
    - если документ может находиться сразу в нескольких директориях, а в текущей реализации append_doc_to_shelf позволяет это, то метод get_doc_shelf должен возвращать все директории в виде списка или множества, а не только первую найденную
  * append_doc_to_shelf
    - несоответствие происходит при добавлении документа в директорию, если он уже находился в какой-то директории наверное, предполагается что документ не может находиться сразу в нескольких директориях данный метод используется в программе только внутри других методов, что исключает эту ошибку при выполнении кода (там выполняются проверки), но при расширении функционала программы эта ошибка может помешать корректной работе
    - предыдущий кейс относится также и если пользователь добавляет документ в директорию, в которой он и так находится, запись о нахождении документа в директории продублируется
  * move_doc_to_shelf - несуществующий документ может перемещается в директорию
  * add_new_doc - нет возможности создать документ, не помещая его в определенную директорию
  ###  Проверка создания папки на Яндекс.Диске
  1. Фрагмент курсовой работы, где выполнялось копирование файлов на яндекс диск - [ya.py](https://github.com/headsoft-mikhail/adpy_01/blob/main/testing/ya.py)
  2. файл с тестами - [testing_ya.py](https://github.com/headsoft-mikhail/adpy_01/blob/main/testing/testing_ya.py)
  3. Токен должен находиться в файле tokens.py: YANDEX_TOKEN
  ###  Тест авторизации в Яндекс.Паспорте
  1. Файл с тестами - [testing_yandex_passport_login.py](https://github.com/headsoft-mikhail/adpy_01/blob/main/testing/testing_yandex_passport_login.py)
  2. Правильный пароль и логин должны находиться в файле tokens.py: PASSPORT_LOGIN, PASSPORT_PASSWORD
  3. При правильном вводе пароля, требуется ввод кода из смс от Яндекс или последних 4 цифр звонящего абонента. Для прохождения проверки - сделан ввод этих данных через input.

## Решение [домашнего задания](https://github.com/netology-code/py-homeworks-advanced/tree/master/7.Interview) к лекции «Подготовка к собеседованию»
  1. Все файлы, относящиеся к заданию "подготовка к собеседованию" [здесь](https://github.com/headsoft-mikhail/adpy_01/tree/main/interview)
  1. Класс Stack, содержащий все указанные в задании мемтоды реализован в [stack.py](https://github.com/headsoft-mikhail/adpy_01/blob/main/interview/stack.py)
  1. Решение задачи со скобками - [check_balance.py](https://github.com/headsoft-mikhail/adpy_01/blob/main/interview/check_balance.py)
  1. Также были написаны тесты для методов класса Stack [(здесь)](https://github.com/headsoft-mikhail/adpy_01/blob/main/interview/test_stack.py) и check_balance [(здесь)](https://github.com/headsoft-mikhail/adpy_01/blob/main/interview/test_check_balance.py)
  1. [Решение](https://github.com/headsoft-mikhail/adpy_01/blob/main/interview/code_refactoring.py) задания с рефакторингом кода. При создании экземпляра класса для работы с почтой настройки протоколов SMTP и IMAP используются по умолчанию (те, которые были захардкожены в исходном коде). Изменить их можно, вызовом методов set_imap и set_smtp. При вызове receive_message есть возможность выбрать другую папку кроме inbox и задать фильтр-фразу для поиска в тексте письма (header)

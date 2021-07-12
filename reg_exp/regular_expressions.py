from pprint import pprint
from itertools import groupby
import csv
import re


def read_list_from_csv():
    # читаем адресную книгу в формате CSV в список contacts_list
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def save_list_to_csv(list_to_write, filename):
    # код для записи файла в формате CSV
    with open(filename + ".csv", "w", encoding="utf-8", newline='') as f:
        data_writer = csv.writer(f, delimiter=',')
        data_writer.writerows(list_to_write)


def fix_names(data_list):
    # исправляем формат ФИО
    pattern = re.compile(r"([А-Я][а-я]*)\W*([А-Я][а-я]*)\W*([А-Я][а-я]*)?\W*")
    for data in data_list:
        data[:3] = pattern.sub(r"\1 \2 \3", data[0]+data[1]+data[2]).split(" ")
    return data_list


def fix_phone_numbers(data_list):
    pattern = re.compile(
        r"(\+7|8)?[\s\-]*\(?(\d{3})\)?[\s\-]*(\d{3})[\s\-]*(\d{2})[\s\-]*(\d{2})[\s\-]*\(?(доб\.)?[\s]*(\d+)?\)?"
    )
    for data in data_list:
        data[5] = pattern.sub(r"+7(\2)\3-\4-\5 \6\7", data[5])
    return data_list


def fix_repeats(data_list):
    keyfunc = lambda x: x[0] + x[1]
    data_list = sorted(data_list, key=keyfunc)
    clean_data_list = []
    for grouper, data in groupby(data_list, key=keyfunc):
        data_variants = list(data)
        base_data = data_variants[0]
        if len(data_variants) > 1:
            for variant in data_variants[1:]:
                for i in range(0, len(base_data)):
                    if base_data[i] == "":
                        base_data[i] = variant[i]
        clean_data_list.append(base_data)
    return clean_data_list


if __name__ == "__main__":
    contacts_list = read_list_from_csv()
    contacts_list[1:] = fix_names(contacts_list[1:])
    contacts_list[1:] = fix_phone_numbers(contacts_list[1:])
    contacts_list[1:] = fix_repeats(contacts_list[1:])
    save_list_to_csv(contacts_list, "phonebook")

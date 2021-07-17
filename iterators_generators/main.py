import iterator
import hashlib

filename = 'countries.json'
countries_iterator = iterator.CountriesIterator(filename, start=0, stop=3)

filename = filename.replace('.json', '.txt')
with open(filename, 'w', encoding='utf-8') as write_file:
    for item in countries_iterator:
        write_file.writelines(item + '\n')
        print(item)


def hash_generator(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield hashlib.md5(line.encode()).hexdigest()


for item in hash_generator(filename):
    print(item)

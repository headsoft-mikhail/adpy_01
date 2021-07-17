import json

def link(name):
    return 'https://en.wikipedia.org/wiki/' + name.replace(' ', '_')

class CountriesIterator:
    def __init__(self, filename, start=0, stop=None, ):
        with open(filename, 'r') as read_file:
            self.data = json.load(read_file)
        self.index = 0
        self.start = start
        if stop is not None:
            self.stop = stop
        else:
            self.stop = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.stop:
            raise StopIteration
        name = self.data[self.start]['name']['common']
        url = link(name)
        self.start += 1
        return f'{name} {url}'



# task1
import itertools


def with_index(iterable, start=0):
    for i, x in enumerate(iterable, 1):
        yield i, x


my_car1= ["BMW", "Toyota", "Mercedes", "ZAZ"]
s = with_index(my_car1)
print(next(s))
print(next(s))

# task2

my_car2= ["BMW", "Toyota", "Mercedes", "ZAZ", "Mazda", "Nissan", "Volvo"]

def in_range(start, end, step):
    for i in range(start, end, step):
        print(f'Your car in the future will be {my_car2[i]}')

y = in_range(1, len(my_car2), 3)
print(y)

#task3


class MyIterable:
    def __init__(self, data):
        self._data = data
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._data):
            raise StopIteration
        else:
            value = self._data[self._index]
            self._index += 1
            return value

    def __getitem__(self, key):
        return self._data[key]


xy = MyIterable(my_car2)
for i in xy:
    print(i)

for i in enumerate(my_car2):
    print(i)

for i in range(1, len(my_car2)):
    print(i)



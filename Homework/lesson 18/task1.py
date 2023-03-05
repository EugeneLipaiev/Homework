# task1
import re
from functools import wraps


class MyClass:

    def __init__(self, email):
        self.email = email
        self.validate(email)

    @classmethod
    def validate(cls, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address")


mail = MyClass("123@345.com")
print(mail.email)


# mail = MyClass("123a345.email")

# task2


class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers

    def add_worker(self, worker):
        if not isinstance(worker, Worker):
            raise TypeError("Can only add instances of Worker class to the workers list")
        self._workers.append(worker)


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if not isinstance(new_boss, Boss):
            raise TypeError("A worker's boss must be an instance of the Boss class")
        if self._boss is not None:
            self._boss.workers.remove(self)
        self._boss = new_boss
        new_boss.add_worker(self)


# create some bosses and workers
boss1 = Boss(12, "Terry", "Harbour Foundation")
boss2 = Boss(115, "Mark", "Uber")
worker1 = Worker(11, "Tom", "Harbour Foundation", boss1)
worker2 = Worker(1, "Mary", "Uber", boss2)


# task3

class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return int(func(*args, **kwargs))

        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return str(func(*args, **kwargs))

        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return bool(func(*args, **kwargs))

        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return float(func(*args, **kwargs))

        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


@TypeDecorators.to_float
def do_someone(string: str):
    return string


@TypeDecorators.to_str
def do_did(string: int):
    return string

assert do_nothing('25') == 25

assert do_something("True") is True

assert do_someone('25.5') == 25.5

assert do_did(25) == "25"



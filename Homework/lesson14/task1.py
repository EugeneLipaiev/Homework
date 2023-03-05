# task1
def hello(func):
    print("Hi welcome to program, lets do it")
    func()
    return hello


def count(func):
    def wrap(*args, **kwargs):
        return func

    return wrap


@count
def example(x, y):
    return x + y


example(2, 3)


# task2

def stop_words(words: list):
    def wrap(*args, **kwargs):
        return stop_words

    return wrap


@stop_words(["pepsi", "BMW"])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan(["Steve drinks pepsi in his brand new BMW!"]) == stop_words


# task3
def arg_rules(type_: type, max_length: int, contains: list):
    pass


def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

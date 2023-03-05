import random


# task1
class Person:
    def __init__(self, name: str, lastname: str, age: int):
        self.name = name
        self.lastname = lastname
        self.age = 23

    def talk(self):
        print(f"Hello, my name {self.name} {self.lastname} and I’m {self.age} years old”")


if __name__ == "__main__":
    introduce = Person(name="Carl", lastname="Jonson", age=26)
    introduce.talk()


# task2
class Dog:
    def __init__(self):
        self.age_factor = 7

    def human_age(self, age):
        self.age = age * self.age_factor
        print(self.age)


total = Dog()
total.human_age(5)


# task3
class TVControler:
    def __init__(self, tv_status="off", channels=["BBC", "Discovery", "TV1000"]):
        self.TV_status = tv_status
        self.channels = channels

    def first_channel(self):
        print(self.channels[0])

    def last_channel(self):
        print(self.channels[2])

    def random_channel(self):
        print(random.choice(self.channels))

    def next_channel(self):
        if self.channels[0]:
            print(self.channels[1])
        elif self.channels[1]:
            print(self.channels[2])
        else:
            print(self.channels[0])

    def previous_channel(self):
        if self.channels[0]:
            print(self.channels[2])
        elif self.channels[2]:
            print(self.channels[1])
        else:
            print(self.channels[0])


if __name__ == "__main__":
    controller = TVControler(tv_status="off", channels=["BBC", "Discovery", "TV1000"])
    controller.first_channel()

    print("""
    		-----------TV System-----------
    		I have 3 channels:
    		1. "BBC"
    		2. "Discovery"
    		3. "TV1000"
    		4. "Random channel"
    		5. "Return channel"
    		""")

    while True:

        command = input("Press the button: ")

        if command == "5":
            controller.previous_channel()
            break

        elif command == "1":
            controller.first_channel()

        elif command == "2":
            controller.next_channel()

        elif command == "3":
            controller.last_channel()

        elif command == "4":
            controller.random_channel()

        else:
            print("Unknown Command!")

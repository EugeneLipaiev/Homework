# task1
import math
from pprint import pprint
import calendar
from typing import List, Any


# class Person:
#     def __init__(self, name: object, last_name: object, age: object, address: object):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#         self.address = address
#
#     def yourself(self):
#         self.name = input("Print your name ")
#         return self.name
#
#     def yourself_last(self):
#         self.last_name = input("Print your lastname ")
#         return self.last_name
#
#     def yourself_age(self):
#         self.age = input("Print your age ")
#         return self.age
#
#     def yourself_address(self):
#         self.address = input("Print your address ")
#         return self.address
#
#
# class Student(Person):
#
#     def __init__(self, school: object, favorite_subject: object, scholarship: object):
#         Person.__init__(self, name=str, last_name=str, age=int, address=str)
#         self.school = school
#         self.favorite_subject = favorite_subject
#         self.scholarship = scholarship
#
#     def study(self):
#         self.school = input("Where you study? ")
#         return self.school
#
#     def subject(self):
#         self.favorite_subject = input("What is your favorite_subject? ")
#         print(f"My favorite_subject is {self.favorite_subject}")
#
#     def money(self):
#         self.scholarship = input("How much money do you get? ")
#         print(self.scholarship)
#
#
# class Teacher(Student, Person):
#
#     def __init__(self, work_school: object, salary: object, address: object):
#         Person.__init__(self, name=str, last_name=str, age=int, address=str)
#         Student.__init__(self, school=object, favorite_subject=object, scholarship=int)
#         self.work_school = work_school
#         self.scholarship = salary
#         self.address = address
#
#
# if __name__ == "__main__":
#     human = Person(name=str, last_name=str, age=int, address=str)
#     guy = Student(school=object, favorite_subject=object, scholarship=int)
#     adults = Teacher
#
#     guy.yourself()
#     guy.yourself_last()
#     guy.yourself_age()
#     guy.yourself_address()
#     guy.study()
#     guy.subject()
#     guy.money()


# task2


class Mathematician():
    def __init__(self):
        print()

    def __int__(self):
        return int

    @staticmethod
    def square_nums(nums):
        x = []
        for i in nums:
            i = i ** 2
            x.append(i)
        x = list(x)
        return x

    @staticmethod
    def remove_positives(nums):
        x = []
        for i in nums:
            if i < 0:
                x.append(i)
        x = list(x)  # як робити по іншому, бо виглядає не дуже. Як повертати у нормальний список?
        return x

    @staticmethod
    def filter_leaps(nums):
        x = []
        for i in nums:
            if calendar.isleap(i):
                x.append(i)
        x = list(x)
        return x


if __name__ == "__main__":
    m = Mathematician()
    m.square_nums([7, 11, 5, 4])
    m.remove_positives([26, -11, -8, 13, -90])
    m.filter_leaps([2001, 1884, 1995, 2003, 2020])

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]


# task3

class Product:
    def __init__(self, product_type, name, price):
        self.type = product_type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = {}

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Invalid product")
        if product.name in self.products:
            self.products[product.name]['amount'] += amount
        else:
            self.products[product.name] = {'product': product, 'amount': amount}

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type == 'name':
            if identifier not in self.products:
                raise ValueError("Product not found")
            self.products[identifier]['product'].price *= (100 - percent) / 100
        elif identifier_type == 'type':
            for product in self.products.values():
                if product['product'].type == identifier:
                    product['product'].price *= (100 - percent) / 100
        else:
            raise ValueError("Invalid identifier type")

    def sell_product(self, product_name, amount):
        if product_name not in self.products:
            raise ValueError("Product not found")
        if self.products[product_name]['amount'] < amount:
            raise ValueError("Not enough products in stock")
        self.products[product_name]['amount'] -= amount
        self.income += amount * self.products[product_name]['product'].price

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [product_info['product'] for product_info in self.products.values()]

    def get_product_info(self, product_name):
        if product_name not in self.products:
            raise ValueError("Product not found")
        return self.products[product_name]['product'].name, self.products[product_name]['amount']


if __name__ == "__main":
    p = Product('Sport', 'Football T-Shirt', 100)
    p2 = Product('Food', 'Ramen', 1.5)
    s = ProductStore()
    s.add(p, 10)
    s.add(p2, 300)
    s.sell_product('Ramen', 10)
    assert s.get_product_info('Ramen') == ('Ramen', 290)


# task4
class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open("logs.txt.", "w") as file:
            file.read(msg + "\n")
            super.__init__(msg)





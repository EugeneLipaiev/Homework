# # task1
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         raise NotImplementedError("Give me animal")
#
#
# class Cat(Animal):
#     def talk(self):
#         print("Meow")
#
#
# class Dog(Animal):
#     def talk(self):
#         print("Gaw, Gaw")
#
#
# def make_animal_talk(animals):
#     animals.talk(Animal)
#
#
# dog = Dog("Ali")
# cat = Cat("Tyson")
#
# make_animal_talk(Dog)
# make_animal_talk(Cat)
#
# animals = [Cat("Tyson"), Dog("Ali")]
# for animal in animals: animal.talk()


# task2
class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: 'Author') -> 'Book':
        book = Book(name, year, author)
        self.books.append(book)
        self.authors.append(author)
        return book

    def group_by_author(self, author):
        author_books = [book for book in self.books if book.author == author]
        return author_books

    def group_by_year(self, year: int) -> list:
        year_books = [book for book in self.books if book.year == year]
        return year_books

    def __str__(self):
        return f"Library({self.name}, books={self.books}, authors={self.authors})"

    def __repr__(self):
        return self.name


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self.author.books.append(self)
        Book.total_books += 1

    def __str__(self):
        return f"Library({self.name}, {self.year}, authors={self.author})"

    def __repr__(self):
        return self.name


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        return f"Library({self.name}, {self.country}, {self.birthday}, {self.books})"

    def __repr__(self):
        return self.name


if __name__ == "__main__":
    # Create some authors
    Dumas = Author("Alexandre Dumas ", "France", "24 July 1802")
    Shakespeare = Author("William Shakespeare", "English", "26 April 1564")

    # Create a library
    library = Library("Main Library")

    # Add some books to the library
    cristo = library.new_book("The Count of Monte Cristo", 1846, Dumas)
    tree_musk = library.new_book("The Three Musketeers", 1844, Dumas)
    rj = library.new_book("Romeo and Juliet", 1597, Shakespeare)
    lucrece  = library.new_book("The Rape of Lucrece", 1594, Shakespeare)

    # Group books by author
    dunas_books = library.group_by_author(Dumas)
    shakespeares_books = library.group_by_author(Shakespeare)

    # Group books by year
    the_count = library.group_by_year(1846)
    the_rape = library.group_by_year(1594)

    # Print out the results
    print(library)
    print(Dumas)
    print(Shakespeare)
    print(the_count)
    print(the_rape)


#task3
class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __eq__(self, other):
        if isinstance(other, Fraction):
            self.reduce()
            other.reduce()
            return self.numerator == other.numerator and self.denominator == other.denominator
        return False

    def __lt__(self, other):
        if isinstance(other, Fraction):
            self.reduce()
            other.reduce()
            return self.numerator * other.denominator < other.numerator * self.denominator
        return False

    def __add__(self, other):
        if isinstance(other, Fraction):
            numerator = self.numerator * other.denominator + self.denominator * other.numerator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        raise TypeError(f"Cannot add {type(self).__name__} and {type(other).__name__}")

    def __sub__(self, other):
        if isinstance(other, Fraction):
            numerator = self.numerator * other.denominator - self.denominator * other.numerator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        raise TypeError(f"Cannot subtract {type(self).__name__} and {type(other).__name__}")

    def __mul__(self, other):
        if isinstance(other, Fraction):
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        raise TypeError(f"Cannot multiply {type(self).__name__} and {type(other).__name__}")

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Fraction(numerator, denominator)
        raise TypeError(f"Cannot divide {type(self).__name__} and {type(other).__name__}")

    def reduce(self):
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def _gcd(self, a, b):
        if b == 0:
            return a
        return self._gcd(b, a % b)


num1 = Fraction(10,100)
num2 = Fraction(100,10)

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
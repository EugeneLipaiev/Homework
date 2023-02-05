#Task1
def favourite_movie(name):
    print("My favourite movie is " + name)

favourite_movie("Top Gun")

#Task2
def make_country(name_country, capital_country):
    geography = {name_country:capital_country}
    print(geography)

make_country("Ukraine","Kiev")

#Task3

def make_operation (*args):
    x = 0
    for y in args:
        x +=y
    return x
print(make_operation(3,4,5,6,7,4))

def make_operation (*args):
    x = 1
    for y in args:
        x *=y
    return x
print(make_operation(3,4,5,6,7,4))

#далі із відніманням та діленням не пішло, не все так просто видалось
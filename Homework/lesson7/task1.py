#Task1

a = str("The life in front of you is way more important than the life behind you")
a = a.split()
b = {}
for key in a:
    b[key] = b.get(key, 0) +1
print(b)


# Task2

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


sum = 0

for x in prices:
    total_price = stock[x] * prices[x]
    print(total_price)
    sum = total_price +sum
print(sum)


#Task3
list = tuple[("i","j")]
print(type(list))

list = [i ** 2 for i in range(1,10)]
print(list)

#Task4

Week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
Week_2 = {1:"Monday", 2:"Tuesday",3: "Wednesday",4: "Thursday",5: "Friday",6: "Saturday",7:"Sunday"}
for i in Week_2:
    print(Week_2[i],":", i)

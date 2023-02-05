#Task1
import random

list_ = [23,54,23,35,76,23,77,44,32,66]
max_1 = list_[0]

for i in range(10):
   if list_[i] > max_1:
       max_1 = list_[i]
print(max_1)

#Task3
a = [2,6,7,4,3,2,7,8,6,4]
b = [1,9,4,2,2,5,8,6,5,10]
c = list(set(a+b))
print(c)



#Task 3
list_ = [23,54,23,35,76,23,77,44,32,66,49,43,14,28]
list_2 = []
list_3 = []
for i in list_:
    if i %7 == 0:
        list_2.append(i)
    if i % 5 != 0:
        list_3.append(i)
print(list_2)
print(list_3)
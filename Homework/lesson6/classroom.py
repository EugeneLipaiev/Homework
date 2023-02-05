firs_element =  int(input())
summma = firs_element
max1 = firs_element
min1 = firs_element

for i in range(9):
    number = int(input())
    summma += number
    if number >= max1:
        max1 = number
    if min1 >= number:
        min1 == number

print(summma//10)
print(max1)
print(min1)
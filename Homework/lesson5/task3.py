import random
import string
exsample = str(input())
string.ascii_letters = exsample
print("".join(random.choice(exsample) for i in range(15)))
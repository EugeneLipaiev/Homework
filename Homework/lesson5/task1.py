import random

player= int(input("Take digits from 1 to 10"))
computer = random.randint(1, 10)

if player == computer:
        print("You win")
if player >= 11:
            print("use digits from 1 to 10")
if player <= 0:
            print("use digits from 1 to 10")
print(f'His choise was {computer}')









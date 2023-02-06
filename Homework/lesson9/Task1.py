from fruits import prices

weight = {"apple": 14,
        "bananas": 36,
        "avocado": 12,
        "orange": 53}


def total():
    for i in prices:
       print(i, ":", prices[i] * weight[i])

total()
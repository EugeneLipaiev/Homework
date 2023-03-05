import calendar


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

# if __name__ == "__main__":
#     m = Mathematician()
#     m.square_nums([7, 11, 5, 4])
#     m.remove_positives([26, -11, -8, 13, -90])
#     m.filter_leaps([2001, 1884, 1995, 2003, 2020])
#
# assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
# assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
# assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

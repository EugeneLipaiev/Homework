# task 1

def about_you():
    Name = str(input())
    Last_name = str(input())
    Birthday = int(input())


print(about_you.__code__.co_nlocals)

# TAsk3

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]


def choose_func(*args, **kwargs):
    def wrap(param, func1, func2):
        if param == "val_1":
            return func1

        if param == "val_2":
            return func2

        raise ValueError("invalid operation")

    return wrap


@choose_func
def square_nums(nums):
    return print(num ** 2 for num in nums1)


@choose_func
def remove_negatives(nums):
    return print(num for num in nums2 if num > 0)


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]

assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

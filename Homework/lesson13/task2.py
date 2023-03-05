def total_prices(func1):
    func1 = dict(
        apple=5,
        bananas=4.5,
        avocado=6,
        orange=6.5)

    def count(func2):
        func2 = dict(
            apple=14,
            bananas=36,
            avocado=12,
            orange=53,
        )
        return [lambda x: func1 * func2]

    return func1


total_prices(print)

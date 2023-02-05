from nadezhga import to_float, FloatCastingError

# Task2

def read_float(promt):
    while True:
        val = input(promt)
        try:
            return to_float(val)
        except FloatCastingError as e:
            print(str(e))

def fedor():
    a = read_float("Insert A value: ")
    b = read_float(">>>")

    try:
        print(f" {a ** 2} / {b} = {(a ** 2) / b}")
    #except ZeroDivisionError:
        #print("Zero division error")
    except ArithmeticError as e:
        print(f"Error: {e}")
    finally:
        print("\nCalculation completed successfully")

if __name__ == '__main__':
    try:
        fedor()
    except KeyboardInterrupt:
        print("\n!!! Interrupted")
    finally:
        print("goodbye")

















# task1
def oops():
    Life = ("The life in front of you is way more important than the life behind you")
    print(Life[101])


def oops_fix():
    try:
        oops()
    except IndexError:
        print("not finde index")








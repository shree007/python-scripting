def basic_exception():
    try:
        exception_generator_code = 10/0
    except:
        print("Not possible to divide with zero")
    finally:
        print("Execution failed because 0 can not divide")

def value_exception():
    try:
        number = int("hello")
    except ValueError as e:
        print(f"value error occurred{e}")

def multiple_exception():
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    except ValueError:
        print("Please enter a valid integer.")

def raise_exception():
    try:
        result = divide(10,0)
    except ValueError as e:
        print(f"Exception occurred: {e}")

def divide(a, b):
    if b == 0:
        raise ValueError(f"can not divide zero")
    return a/b


if __name__ == '__main__':
    print("basic exception handling")
    basic_exception()
    value_exception()
    multiple_exception()
    raise_exception()
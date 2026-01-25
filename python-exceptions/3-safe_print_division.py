#!/usr/bin/python3

def safe_print_division(a, b):
    result = ((int) or (None))
    try:
        result = a / b
    except (TypeError, ValueError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))


a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
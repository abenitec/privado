def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return None
print(divide(5,0))

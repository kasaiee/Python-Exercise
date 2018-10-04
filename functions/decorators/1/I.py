def corrective_div(func):
    def wrapper(soorat, makhraj):
        try:
            return soorat / makhraj
        except TypeError as e:
            return 'Enter a number. ' + str(e)
        except ZeroDivisionError as e:
            return 'b must not be 0. ' + str(e)
    return wrapper


@corrective_div
def div(a, b):
    return a / b


print(div(2, 'ali'))
print(div(2, 0))
print(div(2, 4))

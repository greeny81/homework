def is_prime(func):
    def wrapper(*args):
        number = func(*args)
        if number % 2 == 0 and number != 0:
            print("Составное")
        else:
            print("Простое")
        return number
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)


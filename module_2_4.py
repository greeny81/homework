numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers)):
    for j in range(numbers[i]):
        if i % j == 0:
            is_prime = True
        print(i, j)
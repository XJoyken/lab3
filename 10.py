def filter_prime(x):
    def isprime(i):
        if i < 2:
            return False
        else:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    return False
        return True
    listik = map(int, x.split())
    return [z for z in listik if isprime(z)]

x = "1 2 3 4 5 6 7 8 9 10 11 13 15 17 19 20 21 25 32 35 37"
print(filter_prime(x))
import math

def prime(x):
    if(x < 2):
        return False
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if(x % i == 0):
                return False
    return True

listik = [x for x in range(100)]

print(list(filter(lambda x : prime(x), listik)))
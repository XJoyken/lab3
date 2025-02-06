from itertools import permutations

def perm(s):
    x = permutations(s)
    for i in list(x):
        print("".join(i))

perm(input())
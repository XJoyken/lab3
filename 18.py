def histogram(x):
    for i in x:
        for j in range(i):
            print("*", end = "")
        print()

x = [4, 9, 7]
histogram(x)
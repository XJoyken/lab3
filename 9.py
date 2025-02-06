def solve(numheads, numlegs):
    for i in range(1, numheads + 1):
        if(i * 2 + (numheads - i) * 4 == numlegs):
            print(f"Quantity of chickens: {i}\nQuantity of rabbits: {numheads - i}")

solve(35, 94)
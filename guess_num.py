import random

def guess():
    name = input("Hello! What is your name?\n")
    guess_number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.\nTake a guess.")
    count = 0
    while(True):
        x = int(input())
        if(x < guess_number):
            count += 1
            print("\nYour guess is too low.\nTake a guess")
        elif(x > guess_number):
            count += 1
            print("\nYour guess is too high.\nTake a guess")
        else:
            count += 1
            print(f"\nGood job, {name}! You guessed my number in {count} guesses!")
            break

if __name__ == "__main__":
    guess()
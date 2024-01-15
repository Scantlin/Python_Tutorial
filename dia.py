import random

game = True
while game:
    guess = int(input("Enter your guess: "))
    x = random.randrange(1, 6)
    if guess == x:
        print("You won")
        break
    else:
        print(f"The answer is {x}")
        print("Try Again")

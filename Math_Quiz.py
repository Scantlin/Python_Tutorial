i = 3
while(i > 0):
    x = int(input("What is the sqaure root of 25: "))
    y = int(input("What is 0 * 6: "))
    we = int(input("What is 8 * 2: "))
    if x == 5 and y == 0 and we == 16:
        print("You got all the answers right\n" + "You Won")
        break
    elif x == 5 and y == 0:
        print("You got two correct answers item no. 1 and 2")
        i-=1
    elif y == 0 and we == 16:
        print("You got item no. 2 and 3 correct")
        i-=1
    elif x == 5 and we == 16:
        print("Got item no. 1 and 3 right")
        i-=1
    else:
        print("No correct answer")
        i-=1
    
    if i == 0:
        print("No chance\n" + "you lost")

x = input("What is the 5th planet in our solar system: ")
if x.casefold() == "jupiter":
    print("you got it right")

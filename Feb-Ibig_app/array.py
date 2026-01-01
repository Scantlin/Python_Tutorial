def info(name, Byear):
    age = 2024 - Byear
    Leapyear = Byear%4
    if Leapyear == 0:
        greet = f'hello, {name}! You are {age} this 2024. Your birth year is a leapyear'
    else:
        greet = f'hello, {name}! You are {age} this 2024. Your birth year is not a leapyear'

    return greet

name = input("Enter your name: ")
Birthyear = int(input("Enter your birthyear: "))

print(info(name, Birthyear))
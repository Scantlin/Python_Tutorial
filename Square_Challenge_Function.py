import math #square a number using a function
print("Function challenge")

numbers = int(input("Please enter the number: "))
def square(number):
    x = math.pow(number, 2)
    return x

print("The squared is: " + str(square(numbers)))

print("Lambda Challenge") #tripple a number using lamba function
s = lambda y:y *3
print(s(int(input("Enter a number: "))))
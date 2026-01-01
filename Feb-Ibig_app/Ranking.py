#Take input from the user
numbers = list(map(int, input("Enter the numbers separated by space: ").split()))
long = int(input("how many numbers needed to add in Fibonacci: "))


for i in range(long):
    x = numbers[-1] + numbers[-2] 
    numbers.append(x)
    print(numbers)
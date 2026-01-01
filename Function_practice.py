print("Grade Calculator")
x = int(input("Enter how many grades you will input: "))
summation = []

print("Enter grades")
for i in range(x):
    y = int(input())
    summation.insert(i, y)
    
sum = 0
for number in summation:
    sum = sum + number
    
print(f"The grade is {sum/x}")

if sum/x >= 98:
    print("With highest Honor")
elif sum/x >= 95:
    print("With high honor")
elif sum/x >= 90:
    print("With Honor")
else:
    print("Still Congratulations")
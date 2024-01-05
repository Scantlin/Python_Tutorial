print("Grade compute tools")
x = int(input("Enter how many number we add: "))
summation = []

print("Enter the numbers: ")

for i in range(x):
    m = int((input()))
    summation.insert(i, m)
    
print(summation)
def sum():
    sum = 0
    for number in summation:
        sum = sum + number
    return sum

grade = sum()/len(summation)
print(grade)

if (grade >= 98):
    print("With highest honors")
elif (grade >= 95): 
    print("With high honor")
elif(grade >= 90):
    print("With honor")
else:
    print("Invalid")


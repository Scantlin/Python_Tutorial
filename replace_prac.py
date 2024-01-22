number = [1, 3, 4, 5]
for i in range(len(number)):
    number[i] = 5
    
sum = 0
for x in number:
    sum = x + sum
 
print(f"The total is {sum}")
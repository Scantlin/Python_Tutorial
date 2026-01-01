x = int(input("Enter the number: "))

def odds(m):
    odd = []
    for i in range(1, x):
        if i % 3 == 0 or i % 5 == 0 and i < x:
            odd.append(i)

    sum = 0
    for xs in odd:
        sum = xs + sum
    return sum

print(odds(x))
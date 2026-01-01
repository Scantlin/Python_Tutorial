x = int(input("Enter how many number: "))
print("Enter the numbers")
bank = []
for i in range(1, x + 1):
    y = float(input(f"{i}. "))
    bank.append(y)

bank.sort(reverse=True)
print("Remarks and ranks")
count = 1
for m in range(len(bank)):
    if bank[m] >= 3.25:
        print(f"{count}. {bank[m]} = Strongly Agree")
    elif bank[m] >= 2.50:
        print(f"{count}. {bank[m]} = Agree")
    elif bank[m] >= 1.75:
        print(f"{count}. {bank[m]} = Disagree")
    elif bank[m] >= 1:
        print(f"{count}. {bank[m]} = Strongly Disgree")
    else:
        print("invalid")
    count += 1
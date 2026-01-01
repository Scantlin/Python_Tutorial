mx = int(input("Enter how many items: "))
def respond(responds):
    if responds == 1:
        return "Strongly Disagree"
    elif responds == 2:
        return "Disagree"
    elif responds == 3:
        return 'Agree'
    elif responds == 4:
        return "Strongly Agree"
    else:
        return "Invalid responds"

converts = []
print("Enter the numbers: ")
for i in range(1, mx+1):
    m = int(input())
    converts.append(f"{i}. {respond(m)}")

for mo in range(len(converts)):
    print(converts[mo])
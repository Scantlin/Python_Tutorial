go = True

while go:
    def arith(x, y):
        cd = x[1] - x[0]
        for i in range(y):
            last = x[-1] + cd
            x.append(last)
        return x
        
    lisA = []
    ia = int(input("Enter how many numbers in sequence excluding the missing: "))
    ea = int(input("Enter the number of missing: "))
    print("Enter all numbers in the sequence: ")
    
    for i in range(ia):
        m = int(input())
        lisA.insert(i, m)
        
    print(arith(lisA, ea))
        
    ck = input("\nDo you want to continue? Y/N: ").lower()
    if ck == 'y':
        go = True
    elif ck == 'n':
        go = False
    else:
        print("Invalid Command")
        ck = input("\nDo you want to continue? Y/N: ").lower()
        if ck == 'y':
            go = True
        elif ck == 'n':
            go = False
        else: 
            print("invalid Command")
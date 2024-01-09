<<<<<<< HEAD
go = True

while go:
    def geo(x, y):
        cd = x[1] / x[0]
        for i in range(y):
            last = x[-1] * int(cd)
            x.append(last)
        return x
        
    lisG = []
    ia = int(input("Enter how many numbers in sequence excluding the missing: "))
    ea = int(input("Enter the number of missing: "))
    print("Enter all numbers in the sequence: ")
    
    for i in range(ia):
        m = int(input())
        lisG.insert(i, m)
        
    print(geo(lisG, ea))
        
    ck = input("\nDo you want to continue? Y/N: ").lower()
    if ck == 'y':
        go = True
    elif ck == 'n':
        go = False
    else:
=======
go = True

while go:
    def geo(x, y):
        cd = x[1] / x[0]
        for i in range(y):
            last = x[-1] * int(cd)
            x.append(last)
        return x
        
    lisG = []
    ia = int(input("Enter how many numbers in sequence excluding the missing: "))
    ea = int(input("Enter the number of missing: "))
    print("Enter all numbers in the sequence: ")
    
    for i in range(ia):
        m = int(input())
        lisG.insert(i, m)
        
    print(geo(lisG, ea))
        
    ck = input("\nDo you want to continue? Y/N: ").lower()
    if ck == 'y':
        go = True
    elif ck == 'n':
        go = False
    else:
>>>>>>> 28ead49c0eb49ad2d09ad255055ad8a87ad59233
        print("Invalid Command")
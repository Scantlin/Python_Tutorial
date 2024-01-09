def fibo(x):
    fibo_list = fibo(x -1)
    
    while len(fibo_list) < x:
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    return fibo_list

print(fibo(int(input("Enter the length of fibonacci sequence: "))))
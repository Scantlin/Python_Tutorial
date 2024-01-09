<<<<<<< HEAD
def fibo(x):
    fibo_list = fibo(x -1)
    
    while len(fibo_list) < x:
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    return fibo_list

=======
def fibo(x):
    fibo_list = fibo(x -1)
    
    while len(fibo_list) < x:
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    return fibo_list

>>>>>>> 45fbc15429ada32ad1ab7b33349d791d39a50fdd
print(fibo(int(input("Enter the length of fibonacci sequence: "))))
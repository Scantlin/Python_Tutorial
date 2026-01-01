import time
#for practice of recursion,  a recursion is a function inside a function
"""def evennums(num):
    print(num)
    if num % 2 != 0:
        print("please enter an even number")
    elif num == 2:
        return num
    else:
        evennums(num - 2)

evennums(int(input("Enter a number: ")))"""

'''
def fibonacci(index):
    if index <= 1:
        return index
    else:
        return fibonacci(index-1) + fibonacci(index-2)

print("*** Recursion ***")
rec = time.time()        
print(fibonacci(8))
recs = time.time()-rec
print(f"speed is {recs}")


def fibo(idx):
    seq = [0,1]
    for i in range(idx - 1):
        seq.append(seq[-1] + seq[-2])
    return seq

print("*** Iteration ***")
it = time.time()
print(fibo(8))
its = time.time() - it
print(f"speed is {its}")

if recs > its:
    print("iteration is fastest")
else:
    print("Recursion is fastest")
'''
'''
# the second method to calculate the sum of list using Recursion
def sum_list(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum_list(list[1:])

print(sum_list([1,2,3,4,5]))
'''
#the first method to calculate the sum of list using Iteration
def sum_list(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum

def add(x):
    x 

if __name__ == "__main__":
    x = int(input("Enter how many numbers to be added: "))

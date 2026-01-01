import math
import sys
import platform
import datetime
import time
import heapq

for i in range(5):
    print(i - 1)

'''
n = [10,20,45,25,65]
x = heapq.nlargest(1, n)
for i in range(len(x)):
    print(x[i])
'''
'''
x = "scantlin"
print(x[:-3])
'''

# round keyword use to return the exact decimal point we want
# %- modulo is for the remainder, // - floor division is to  return the value without decimal point this is not rounded
'''
x1 = int(input('Enter num: '))
x2 = int(input('Enter 2nd num: '))
x = x1 // x2
y = (x1/x2)-x
if y >= 0.5:
    x = x + 1
print("Rounded: {0}".format(x))
'''
'''
m = int(input("Enter seconds: "))

while m != 0:
    seconds = m % 60
    minute = (m%3600) // 60
    hour = m // 3600
    print("{:02d}:{:02d}:{:02d}".format(hour,minute,seconds), end="\r")
    m -= 1
    time.sleep(1)
'''
'''
# ANSI escape code for changing text color to blue
blue_text = "\033[34m"
# ANSI escape code for resetting text color to default
reset_color = "\033[0m"

print(blue_text + "This text will be displayed in blue.", end="\r")
time.sleep(1)
print(reset_color + "This text will be displayed in the default color.")
'''

'''
x = [1, 2, 4]
b = "Scantlin"
c = "Scantlin"

print(f"/{id(x)}, {id(b)}, {id(c)}/")
x = [1, 2, 4]
b = "Scantlin"
c = "Scantlin"

print(f"/{id(x)}, {id(b)}, {id(c)}/")
print(b is c) 
'''
'''
print("finding the area of circle using radius")
def area_circle(radius):
    area = math.pi * math.pow(radius,2)
    return area
print(f'the area of circle is approximately {area_circle(float(input("Enter the radius: ")))}')
'''

'''
print(sys.version)
print(sys.version_info)

print(platform.python_version())
'''


#now = datetime.datetime.now()
#print("Current date and time:", now.strftime("%Y-%m-%d %H:%M"))

t = time.localtime()
print("Current time is", t)
print(time.strftime("%H:%M", t))

'''
print(reset_color)
idx = int(input("Enter a number: "))
for i in range(1, idx + 1):
    print(i, end="")
    if i < idx:
        print(end="\r")
        time.sleep(1)
'''

'''
blue_text = "\033[34m"
def count (num):
    for i in range(num):
        print(i, end="\r" + blue_text)
        time.sleep(1)

count(5)
'''
studentone = {
    "name": "none",
    "age": 0,
    "favorite color": "none"
    
}
m = 1
while m < len(studentone):
    studentone["name"] = input("Enter your name: ")
    studentone["age"] = int(input("Enter your age: "))
    studentone["favorite color"] = input("Enter your favorite color: ")
    print(len(studentone))
    m=m+4

studenttwo = {
    "name": "Nathaniel",
    "age": 18,
    "favorite color": "red"
}

y = 1
name = True
while name:
    x = input("What you want to know about student one: ")
    print(studentone[x.casefold()])
    xs = input("What you want to know about student two: ")
    print(studenttwo[xs.casefold()])
    y = y+1
    if y == 4:
        name = False    

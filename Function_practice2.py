class Math:
  def __init__(self, num1,num2,num3):
    self.num1 = num1
    self.num2 = num2
    self.num3 = num3
    
  def add(self):
    return self.num1 + self.num2 + self.num3
  
  def subtract(self):
    return self.num1 - self.num2 - self.num3
  
    
  
x = Math(int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: ")))
y = input("Enter operation: ")
if y.casefold == "add" or "addition" or "sum" or "plus":
  print(x.add())
elif y.casefold == "minus" or "subtract":
  print(x.subtract())

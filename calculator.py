#Calculator

#Addition

def add(a,b):
  return a+b

#Substraction

def sub(a,b):
  return a-b

#Multiplication

def multiply(a,b):
  return a*b

#Division

def divide(a,b):
  return a/b

print("Select an operation number: ")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
operation = float(input("Insert the number: "))
a = float(input("Insert the first number: "))
b = float(input("Insert the second number: "))
if operation == 1:
  print(f"The result of your operation is: {add(a,b)}")
elif operation == 2:
  print(f"The result of your operation is: {sub(a,b)}")
elif operation == 3:
  print(f"The result of your operation is: {multiply(a,b)}")
elif operation == 4:
  if b == 0:
    print("Division by zero is not possible")
  else:
    print(f"The result of your operation is: {divide(a,b)}")
else:
  print("Invalid operation")
print("\n ¡thanks for using my calculator! ")

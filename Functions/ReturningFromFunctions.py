#Functions can return values when called out. It can be performed through the return statement
def subraction(a,b):
  return a-b

print(subraction(2,0.3))

#Once the function hits return statment, it will not execute any other statements after it
def multiply(a,b):
  mul = a*b
  return mul
  print("This will not be printed")

print(multiply(4,7))

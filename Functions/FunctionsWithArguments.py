#Functions can be created with arguments. Creating a function with a single parameter below:
def SquareOf(n):
  print(float(n*n))

SquareOf(4)

#We can also create functions with more than one argument
def powerOf(a,b):
  print(float(a**b))

powerOf(4,3)

#Fuction arguments scope is within the fucntion and cannot be used outside.  If used, it will thown an error.
def cubeOf(a):
  print(int(a*a*a))

cubeOf(3)
print(a)

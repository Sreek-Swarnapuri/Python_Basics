#Comments are annotions which are used for making the code easier to understand
#Creating a variable x and assigning it a value of 2
x = 2
#Creating a varialbe y and assigning it a value of 4
y = 4

#Finding and printing the reminder when dividing y by x
print(y%x)
#print(x//y) 
#As you can see above comment will not be excuted
#Comments are not retained at runtime as they are ignored.

#Docstrings - Document strings, 
#Docstrings are similar to comments however, they are designed for explaing total code. For example of a function.
def add(a,b):
  """
  This function addes two numbers and returns the sum. 
  It takes two inputs and returns an output
  """
  return a+b

print(add(1,3))

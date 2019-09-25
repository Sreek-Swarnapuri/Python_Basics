#Functions are just like any other values. They can be assigned and re-assigned to another variables and then referenced.
def powOf(a,b):
  return a**b

p = powOf
print(p(2,3))

#Functions can also be passed as arguments to other functions.
def add(a,b):
  return a+b 

def twice(f,a,b):
  return f(f(a,b),f(a,b))

print(twice(add,1,2))

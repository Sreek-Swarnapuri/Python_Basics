#We have already used funcitons which are called pre-defined.
print("hello")
print(list(range(2,20)))
#We type the name of the function before paranthesis and values for the function in the paranthesis
print(list(range(2,10,3)))

#In addition to using pre-defined functions, we can also create custom funcitons
#creating a basic function without inputs or outputs
def func():
  print("1")
  print("2")
  print("3")
  print("4")

#Functions get executed only when they are called
func()

#We must define functions before they are called. In the same way we assign variables before using them.
#Following code will throw an error
Hello()

def Hello():
  print("spam")

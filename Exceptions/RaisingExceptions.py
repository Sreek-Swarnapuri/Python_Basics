#We can raise exceptions using the raise keyword
print(1)
raise ValueError
print(2)

#Exceptions can be raised with arguments that give detail about them
name = "123"
raise NameError("Invalid name")

#We can use raise in Except block to raise exceptions without knowing what exception it is
try:
  print(5/0)
except:
  print("An Error Occured")
  raise

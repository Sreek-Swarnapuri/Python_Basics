#We can write multiple excetions with multiple except keywords
try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError):
   print("Vaule error occured")
except (TypeError):
  print("Type Error occured")

#We can use finally statement which is set after the all the except blocks in order to execute any code which 
#we would want to run even if there are any exceptions or otherwise
try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")

   #Whatever happens code in finally will alwasys run at the end.

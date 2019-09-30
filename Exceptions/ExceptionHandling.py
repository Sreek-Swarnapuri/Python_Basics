#To handle exceptions we use try and except with the error definition

try:
  num1 = 19
  num2 = 0
  print(num1/num2)
except ZeroDivisionError:
  print("An error occured: Due to zero division error")

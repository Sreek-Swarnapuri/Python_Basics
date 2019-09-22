while True:
  print("Options:")
  print("Enter '+' or '-' or '*' or '/' for any operations.")
  print("Enter 'quit' to end the program")
  user_input = input(": ")
  print("Enter the first number")
  a = input(": ")
  print("Enter the second number")
  b = input(": ")
  if user_input == 'quit':
    break
  elif user_input == '+':
    print("Additing of the two numbers is ", a+b)
  elif user_input == '-':
    print("Subraction of the two numbers is ", a-b)
  elif user_input == '*':
    print("Multiplication of the two numbers is ", a*b)
  elif user_input == '/':
    print("First number divided by the second number is ", a/b)
  else:
    print("unknown input")

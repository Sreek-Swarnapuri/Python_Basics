while True:
  print("Options:")
  print("Enter '+' or '-' or '*' or '/' for any operations.")
  print("Enter 'quit' to end the program")
  user_input = input(": ")
  if user_input == 'quit':
    break
  print("Enter the first number")
  a = int(input(": "))
  print("Enter the second number")
  b = int(input(": "))
  if user_input == '+':
    output = a+b
    print("Additing of the two numbers is ", output)
  elif user_input == '-':
    output = a-b
    print("Subraction of the two numbers is ", output)
  elif user_input == '*':
    output = a*b
    print("Multiplication of the two numbers is ", output)
  elif user_input == '/':
    output = a/b
    print("First number divided by the second number is ", output )
  else:
    print("unknown input")

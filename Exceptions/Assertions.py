#Assertions are sanity checks in our program which assert whether a particular expression is true or not.
#If the assertion is true, the program will continue otherwise it will stop.

#Following code assersts that b should not be zero. It will fail as b is zero
a = 4
b = 0
assert b != 0

#We can pass another argument to assert to display information when assertion error is raised
a = 1 
b = 0
assert b!=-0,"B cannot be zero"

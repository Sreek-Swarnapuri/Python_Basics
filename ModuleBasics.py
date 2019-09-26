#Modules are codes written by other people for common tasks.
#Examples are generating random numbers, performing mathematical operations etc
#We use the keyword import to get the modules that were built already. 
#Import line should be at the top of the code so that we can use its features whenever required.

import random

for i in range(5):
  print(random.randint(1,6))

  #We can import only certain set of functions from modules. We use from 'module_name import var', var being the function
from math import pi
print(pi)

#We can import a module or object under a different name using 'as' keyword.
from math import sqrt as square_root

print(square_root(25))

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


"""
There are three main types of modules in Python:
1. Modules writting by us
2. Modules installed from external sources
3. Modules that are pre installed with Python.

The third type is called the Standard Library, and contains many useful modules.
Ex: String, re, datetime, math, random, os, multiprocessing, subprocess, socket, email, json, doctest,unittest, pdb, argparse and sys.

The Standard Library modules, some are written in Python and some are written in C.
Most are available on all platforms, but some are Windows or Unix specific.

Many third party Python modules are stored on the Python Package Index(PyPI).
The best way to install these is using a program called pip. This comes installed by default with modern distributions of Python.

We use it as 'pip install library_name' to install an external library.

It is important to enter pip commands at the command line, not at the Python interpreter.
"""


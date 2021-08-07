# Python Module example

def add(a, b):
   """This program adds two
   numbers and return the result"""

   result = a + b
   return result

# import statement example
# to import standard module math

import math
print("The value of pi is", math.pi)

# import module by renaming it

import math as m
print("The value of pi is", m.pi)

# import only pi from math module

from math import pi
print("The value of pi is", pi)

# import all names from the standard module math

from math import *
print("The value of pi is", pi)


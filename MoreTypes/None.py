"""
None Type
The None object is used to represent the absence of a value. 
It is similar to null in Other Programming languages. 
Like other "empty" values, such as 0, [] and the empty string, it is False when converted to a Boolean variable. 
When entered at a python console, it is displayed as an empty string.
"""

None == None
# Output: True

print(None)
# Output: None

## The None Object is returned by any function that does not explicitly return anything

def abc():
  print(123)

var = abc()
print(var)

#Output:
# 123
# None

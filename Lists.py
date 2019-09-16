#Creating simple lists in python.
words = ["Hello",'World','!']
print(words[0])
print(words[1])
print(words[2])

#Creating an empty list
emptyList = []
print(emptyList)

#Creating a list with only two values. Python will ignore if there is no data after the last comma in a list
lst = [1,"Second",]
print(lst)

#List can have sevaral data type elements in it. List can have another list as one of its items
multiList = ["This", 1, 1.5, 'is Awesome',[1,2,4]]
print(multiList[2])
print(multiList[4])

#Strings can be indexed like lists. Indexing strings behaves as though you are indexing a list containing each character as a separate item from the string.
str = "Hello"
print(str[1])
print(str[0])
print(str[4])

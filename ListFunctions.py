#Using append function to add items at the end
lst = [1,2,4]
lst.append(3)
print(lst)

#Use len method to print the number of items in a list
lst = [4,4,5,6,2,34,6]
print(len(lst))

#Insert method is used to insert an element into a list as oppsosed to at the end using append. insert method uses index as the first parameter for inserting an item
lst = [1,2,3,4,5]
lst.insert(2,5)
print(lst)
#If the index greater than the length of the list it will add it at the end of the list.
lst.insert(10,2)
print(lst)
print(len(lst))

#The index method find the first occurance of the item and returns its index value
lst = ['h','e','l','l','o','o']
print(lst.index('e'))
print(lst.index('o'))

#other useful methods
lst = [1,2,4,5,6,3,4,5,6,3,2,45]
print(max(lst))
print(min(lst))
print(lst.count(3))
lst.remove(1)
print(lst)
lst.reverse()
print(lst)

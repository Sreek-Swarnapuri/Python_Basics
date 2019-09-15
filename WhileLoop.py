#Basic While loop, looping through from 1 to 100
i = 1
while i<101:
  print(i)
  i+=1
  
#Infinite while loop
while 1==1:
  print("1")
  
#While loop with break statement
i = 1
while True:
  print(i)
  i = i + 1
  if i == 5: 
    break 

#While loop with continue statement
i = 5
while True:
  i = i - 1
  if i == 4:
    print("Skipping 4")
    continue
  if i == 0:
    print("breaking at 0")
    break
  print(i)

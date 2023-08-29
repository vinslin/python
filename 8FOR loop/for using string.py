n = input("enter the string")
b = input("enter the string")

for i in n :
    first = i
    for j in b:
      if (first==j):
         print(j,end='')
break
    
else:
    print("\nend of loop")

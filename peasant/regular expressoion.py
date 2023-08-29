import re#regular expression
txt ="hi guys i am looking for a python developer jobs"

x=re.search("python",txt)

print(x)

#x=re.search("java",txt)

print(x)
# user ta input vangura mathiri podanunum
if x:
    print("your wi=ord is there")

else:
    print("your wi=ord  not there")


#user input seaarch  word podanum

y=input("enter the searching word")

x=re.search(y,txt)
if x:
    print("your wi=ord is there")

else:
    print("your wi=ord  not there")


#f string use panni output kattanum

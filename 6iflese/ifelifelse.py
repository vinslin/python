x= int(input("enter the first subject mark:"))
y= int(input("enter the second subject mark:"))
z =(x+y)/2
if z>=90:
    print("grade is A")
elif z<90 and z>=80:
    print("grade is B")
elif z<80 and z>=70:
    print("grade is C")
elif z<60 and z>=35:
    print("grade is D")
else:
    print("grade is E")

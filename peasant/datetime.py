import datetime

x=datetime.datetime.now()
print(x)
#date show pannum
print(x.strftime("%A"))
print(x.strftime("%B"))#month show pannum

print(x.strftime("%H"))#hour kattum

print(x.strftime("%p"))#am or pm
print(x.strftime("%M"))#minute
print(x.strftime("%S"))#seconds
#bills generate panna use ahagum

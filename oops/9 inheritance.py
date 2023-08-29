#inheritance concept
#parent class
class employee:
    nope="ndiwbcowdj"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def work(self):
        print(self.name,"is in working and his age is",self.age)


class softwareengineer(employee):#child class
    pass

 

class designer(employee):#child of employee
    pass
 


se=softwareengineer("max",34)
print(se.name)

d=designer("nuke",42)
print(d.name,d.age)
print(designer.nope)#its also inherits class attributes
se.work()#function calling
d.work()#function calling

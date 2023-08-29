#extend concept and__override__ concept
#parent class
class employee:
    nope="ndiwbcowdj"
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def work(self):
        print(self.name,"is in working and his age is",self.age)


class softwareengineer(employee):#child class
    nope="123456789" #declaring second time for the concept of over ride
    def __init__(self,name,age,salary,level):#over ride the parent __init function
        super().__init__(name,age,salary)#use suoer() to initialize the parent __init
        self.level=level

    def work(self):
        print(self.name,"is in debugging and his age is",self.age)


class designer(employee):#child of employee
    def draw(self):
        print(f"{self.name} is drawing")
 


se=softwareengineer("max",34,3900129201123,"junior")
print(se.name)

d=designer("nuke",42,293900120111)
print(d.name,d.age)
print(designer.nope)#its also inherits class attributes
se.work()#function calling
d.work()#function calling

print(se.level)#child class arguments
d.draw()
se.work() #it runs the softwareengineer function
print(se.nope)# it overrides the claa instances

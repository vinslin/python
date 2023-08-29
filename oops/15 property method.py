#transform the function into method
class softwareengineer:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self._salary=None#protected object attribute it simply says that donnt access
        self._noofbugs=0#protected object attribute
   ##change the protected value in getter and setter mathod
    @property#method creating
    def salary(self):
        return self._salary

    @salary.setter#setting the method
    def salary(self,value):
        self._salary=value

    @salary.deleter  #delete the attribute
    def salary(self):
        del self._salary


se=softwareengineer("max",32)
print(se.name)
print(se.age)
print(se._salary)


se.salary=2899
print(se.salary)
del se.salary   #calling the deleting method
print(se.salary)



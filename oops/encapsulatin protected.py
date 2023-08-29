class softwareengineer:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self._salary=None#protected object attribute it simply says that donnt access
        self.__noofbugs=0#protected object attribute
   ##change the protected value in getter and setter mathod
    #getter method
    def get_salary(self):
        return self._salary

    #setter method
    def set_salary(self,value):
        self._salary=value


se=softwareengineer("max",32)
print(se.name)
print(se.age)
print(se._salary)


se.set_salary(2899)#change the value using setter
print(se.get_salary())#print the value using getter



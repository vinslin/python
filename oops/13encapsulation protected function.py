class softwareengineer:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self._salary=None#protected object attribute it simply says that donnt access
        self._noofbugs=0#protected object attribute

    def code(self):
        self._noofbugs+=1

    
   ##change the protected value in getter and setter mathod
    #getter method
    def get_salary(self):
        return self._salary

    #setter method
    def set_salary(self,value):
        self._salary=self._calculate_salary(value)

    def _calculate_salary(self,value):#protected function
        
        if self._noofbugs<10:
            return value
    
        if self._noofbugs<100:
            return value*2
         
        return value*3
    
    


se=softwareengineer("max",32)
print(se.name)
print(se.age)
print(se._salary)

for i in range(77):
    se.code()

print(se._noofbugs)
se.set_salary(1000000)
print(se.get_salary())





se1=["software engineer","max",20,"manager",5000000]
se2=["software engineer","duke",25,"junior",5000]
se3=["software engineer","duke",25,"junior",5000]



class softwareengineer:
    #class atributes write here
    nos="vibin"
    def __init__(self,name,age,position,salary):
        self.name=name
        self.age=age
        self.position=position
        self.salary=salary
    #string representaion
    def __str__(self):
        information=f"name ={self.name} /n age ={self.age}"
        return information

    

    



#object creation or __instance__ creation
se1=softwareengineer("max",20,"manager",5000000)
se2=softwareengineer("duke",25,"junior",5000)
se3=softwareengineer("kate",23,"junior",5000)

print(se1)#it prints memory address
print(se1.name)# it prints the object attribute
## call only the object it returns the string value
print(se1)
## other funtion return the me==mory adress of the variable or any


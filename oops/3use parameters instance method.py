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
    
    #use parameter instance method
    def code_in_language(self,language):
        print(f"{self.name} iss writing code in   {language}.....")




#object creation or __instance__ creation
se1=softwareengineer("max",20,"manager",5000000)
se2=softwareengineer("duke",25,"junior",5000)
se3=softwareengineer("kate",23,"junior",5000)

se1.code_in_language("c++")##function calling with one object

print(se1.name)##access the object name
none="dhidbs"
se1.name = none## we also change the object attributes in this way
print(se1.name)







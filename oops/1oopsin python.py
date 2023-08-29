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

    #assinging a variable for the function
    def information (self):

        information = "tguyadhsbihdxvk"

        return information
    

    



#object creation or __instance__ creation
se1=softwareengineer("max",20,"manager",5000000)
se2=softwareengineer("duke",25,"junior",5000)
se3=softwareengineer("kate",23,"junior",5000)

print(se1)#it prints memory address
print(se1.name)# it prints the object attribute

print(softwareengineer.nos)##calling the class attributes

print(se1.information)

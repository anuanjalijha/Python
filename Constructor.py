#Parameterized Constructor
class A:
    name2 ="anu"
    def __init__(self,age,name,address):
        print(age,name,address,self.name2)
    def show(self):
        print(self.name2)
        

obj = A(21,"Anjali","muz")
obj.show()

# Default Constructor
class A:
    name = "Anjali"
    age = 20
    def __init__(self):
        address = "Muz"
        print(self.name," ",address)
    def show(self):
        print(self.age)
obj = A() 
obj.show()
        
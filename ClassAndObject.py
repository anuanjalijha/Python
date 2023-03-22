class myClass:
    x = 5
p1 = myClass()
print(p1.x)

class person:
 def __init__(self,age,name):
        self.age = age
        self.name = name
p1 = person(36,"John")
print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.n = name
    self.a = age
  

  def __str__(self):
        return f"{self.n}({self.a})"
p1 = Person("John", 36)

print(p1)


class Person:
  def __init__(self, name, age):
    self.n = name
    self.a = age
  

  def myName(self):
        print("My name is " +self.n)
p1 = Person("Anjali", 36)

p1.myName()

class Person:
  def __init__(myobj, name, age):
    myobj.n = name
    myobj.a = age
  

  def myName(myname):
        print("My name is " +myname.n)
p1 = Person("Anjali", 36)

p1.myName()

class Person:
  def __init__(self, name, age):
    self.n = name
    self.a = age
  

  def myName(self):
        print("My name is " +self.n)
p1 = Person("Anjali", 36)

p1.age = 40
print(p1.age)

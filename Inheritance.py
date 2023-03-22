class person:
 def __init__(self,fname,lname):
    self.firstname = fname
    self.lastname = lname
 
 def fullName(self):
        print(self.firstname,self.lastname)
        
x = person("john","doe")
x.fullName()

class person:
 def __init__(self,fname,lname):
    self.firstname = fname
    self.lastname = lname
 
 def fullName(self):
        print(self.firstname,self.lastname)

class student(person):
    pass
        
x = student("john","doe")
x.fullName()

class person:
 def __init__(self,fname,lname):
    self.firstname = fname
    self.lastname = lname
 
 def fullName(self):
        print(self.firstname,self.lastname)

class student(person):
 def __init__(self,fname,lname):
    person.__init__(self,fname,lname)
    
        
x = student("john","doe")
x.fullName()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Anjali", "Kumari")
x.printname()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2010

x = Student("Mike", "Olsen")
print(x.graduationyear)

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname,year):
    super().__init__(fname, lname)
    self.graduationyear = year
  
  def welcome(self):
        print("Welcome", self.firstname,self.lastname,"to the class of",self.graduationyear)

x = Student("Anjali","Jha",2020)
x.welcome()

class harivanshraibachhan:
 def __init__(self,name):
    self.hname = name
 
 def writePoem(self):
        print(self.hname,"writes a poem")
        
class amitabhbachan(harivanshraibachhan):
 def __init__(self,name):
    super().__init__(name)
 
 def anchorQuizShow(self):
        print(self.hname,"hosts a show")
        
 def sing(self):
    print(self.hname,"sings a song")
 
 def dance(self):
    print(self.hname,"dances")
    
class abhishekbachhan(amitabhbachan):
 def __init__(self,name):
    super().__init__(name)
    
 def sing(self):
    print(self.hname,"singing")
    
x = abhishekbachhan("Abhishek Bachhan")
x.sing()

class harivanshraibachhan:
 def __init__(self,name):
    self.hname = name
 
 def writePoem(self):
        print(self.hname,"writes a poem")
        
class amitabhbachan(harivanshraibachhan):
 def __init__(self,name):
    super().__init__(name)
 
 def anchorQuizShow(self):
        print(self.hname,"hosts a show")
        
 def sing(self):
    print(self.hname,"sings a song")
 
 def dance(self):
    print(self.hname,"dances")
    
class abhishekbachhan(amitabhbachan):
 def __init__(self,name):
    super().__init__(name)
    
 
    
x = abhishekbachhan("Abhishek Bachhan")
x.sing()
x.writePoem()
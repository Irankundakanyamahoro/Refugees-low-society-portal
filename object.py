#class myclass:
 #   x = 5
#p1 =myclass()
#print(p1.x)

#class Person:
 # def __init__(self,name,age):
  #  self.name = name 
   # self.age = age

#p1 =Person("john", 36)

#print(p1.name)
#print(p1.age)  

class Person:
    def __init__(self,fname,lname):
      self.firstname = fname
      self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
x = Person("John" , "Deo") 
x.printname()      
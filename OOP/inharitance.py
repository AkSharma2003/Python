# what is inharitance:-  using inharitance we can use data and methoad of parnet class using his child class
# khud ka constructor hai toh parrent ka constructor call nahi hoga 
# khud ka construcot nahi hai toh parrent ka constructor call hoga 
# chile can't access private member of its parrent calss

# inhariutance summray
# A class can inharitance another class
# inharidtance improove code Reuse
# constructor, attribute, methoads, get inharitance to the child class
# the parrent has no access to the child class
# private property or variable can not be access in the child class
# chid calss can override the attribute or methoads. this is the child class overriding or methoad
# supper() is an inbult function which is used to invoke in parrent calss methoad or comstructor



# tyoe of inheritance
# 1. single inharitance 
# 2. multilevel inharitance
# 3. hirerichal inharitance
# 4. multiple inharitance(Dimond priblom)
# 5. hybrid inharitance

# single inharitance
# parrent
class phone:
    def __init__(self,price,brand,camra):
        print('inside the phone class')
        self.price=price
        self.brand=brand
        self.camra=camra
        
    def buy(self):
        print('phone is buying')
        
class smdaartPhone(phone):
    def __init__(self,os,ram):
        self.os=os
        self.ram=ram
        print('inside smart phone constructor')
    
    
s=smdaartPhone('android',2)

# multilavel
class product:
    def revew(self):
        print('product customer revew')
        
class items(product):
    def __init__(self,name ,price):
        print('inside the item constructor')
        self.name=name
        self.price=price
        
    def buy(self):
        print('Buying a phone')
        
s=items('phone',2000)
s.buy()
s.revew()


# hirerichal

class course:
    def __init__(self,price,name,compney):
        print('inside the course constructor')
        self.price=price
        self.name=name
        self.compney=compney
        
    def buy(self):
        print('i buy a new course')
        
class smartCourse(course):
    pass

class normalCourse(course):
    pass


smartCourse(10000,'dsa','abc')
normalCourse(5000,'web','pqr')


# the dimaond problum
class a:
    def somthing(self):
        print('print of a')
        
class b:
    def somthing(self):
        print('print b')
        
        
class c(a,b): 
    pass

obj=c()
obj.somthing() # print somthing of a becouse in the class c first inharit a 

class d(b,a):
    pass

o=d()
o.somthing() # here print somthing of b
    
 


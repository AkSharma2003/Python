
class person:
        
    # pass by refrance
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    
        

# outside of class is function but inside it colled methoad
def greet(person):
    print('Hi my name is',person.name,'And my gender is ',person.gender)
    person.name='Ankit'
    return person
    
# user efiend object is by default imutable    
p=person('Ap','female')
p1=greet(p)
print("id of p",id(p))
print("id of p1",id(p1))


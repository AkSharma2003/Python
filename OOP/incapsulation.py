
# refrance variable:- 
#     refracne variable holds the object 
#     we can create objects without refrance variable as well as
#     an object have multiple refrance variable 
#     Assigning new refrance variable to an existing object does not create a new object 


# object without a refrance

class person:
    def __init__(self):
        self.name='Ankit'
        self.gender='male'
        
p=person() # here p is refrance variable who store the address of object
q=p

print("with p",p.name)
print("with q",q.name)

q.name="Pai"

print("after change")
print("with p",p.name)
print("with q",q.name)

# instce variable:-
    # ek aisa variblae jiska vaue alag alag point or object k liye alag alag hota hai
    
class school:
    def __init__(self,input_student,input_roll):
        self.student_name=input_student # here student_name is refrance variable 
        self.student_roll=input_roll # here student_roll is refrane variable
        
s1=school('Ankit','07') 
s2=school("Pai",'05')

print(s1.student_name)
print(s2.student_name)
        
        
# you can make privete variable using double underscore __val here val is private 
# and you can sea the val of outsoide of the class 
# for access _classnem__variable name 



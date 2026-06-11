# polimorphism means having multiple scence

# there are three type:
# 1. Methoad OverRiding
# 2. Methoad Overloading : in python methoad overloading not work and latestst code will be excuted
    # but for cleaning code using default argumant
# 3. operator Overloadong

class shape:
    def area(self,a,b=0):
        if b==0:
            return 3.24*a*a
        else: 
            return a*b
        
s=shape()

print(s.area(7))
print(s.area(3,4))
        

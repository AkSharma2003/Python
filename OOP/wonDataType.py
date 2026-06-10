# paramiterized constructor :- who need some argument like def __ init__ (self,x,y) here x and y is argument

class fraction:
    def __init__ (self,x,y):
        self.nem=x
        self.den=y
        
    def __str__(self): # it is magoic methoad 
        return '{}/{}'.format(self.nem,self.den)
     
    def __add__(self,other):
        return '{}/{}'.format(self.den*other.nem+self.nem*other.den,self.den*other.den) 
    
    def __sub__(self,other):
        return '{}/{}'.format(self.den*other.nem-self.nem*other.den,self.den*other.den) 
    
    def __mul__(self,other):
        return '{}/{}'.format(self.nem*other.nem,self.den*other.den) 
    
    def __truediv__(self,other):
        return '{}/{}'.format(self.nem*other.den,self.den*other.nem) 
    
    
fr1=fraction(2,3)
fr2=fraction(3,4)
print(fr1)
print(fr2)
print(fr2+fr1)
print(fr2-fr1)
print(fr2*fr1)
print(fr2/fr1)
    
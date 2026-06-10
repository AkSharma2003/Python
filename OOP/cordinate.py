class point:
    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y
        
    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)
    
    def eucliean_distance(self,other):
        return ((self.x_cod-other.x_cod)**2+(self.y_cod-other.y_cod)**2)**0.5
    
    def distance_from_orogin(self):
        return self.eucliean_distance(point(0,0))
    
class line:
    def __init__(self,x,y,c):
        self.x=x
        self.y=y
        self.c=c
        
    def __str__(self):
        return '{}x+{}y+{}'.format(self.x,self.y,self.c)
        
    def isPresent(self,point):
        if(self.x*point.x_cod+self.y*point.y_cod+self.c) :return False 
        else: return True
        
        
    
    
p1=point(0,0)
p2=point(4,3)

print(p1,end=" ")
print(p2)

print(p1.eucliean_distance(p2))
print(p2.distance_from_orogin())

l1=line(2,3,0)
print(l1)

print(l1.isPresent(p1))

#pikling:- pikling is the process whereby a python object hierarchy is converted in to a byte stream ,
# and unpikling is the inverse option, whereby a byte stream (from a binary file or bytes like object)is 
# converted back into an object heirarchy

class persson:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def desplay(self):
        print('Hi my name is ',self.name,' and I am',self.age,' years old')
        
    
p=persson('miss Pai',2)

# Conver into a binary
import pickle
with open('persson.pkl','wb') as f:
    pickle.dump(p,f)
    
with open('persson.pkl','rb') as f:
    p=pickle.load(f)
    p.desplay()
    
    
    
# pickle vs JSON
    # pickle lets the user to store data in binary format. JSON lets the user store data in Human readable text format

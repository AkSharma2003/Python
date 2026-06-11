# what is agrigation
    # agrigation means one class won the other class || in second word has a relationship
    # agrigation does not access private variable
    # for access private variable we should use gater methoad
    
class customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
                
    def print_add(self):
        print(self.address.get_city(),self.address.pin,self.address.state)    # here use agrigation
        
    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name=new_name
        self.address.edit_address(new_city,new_pin,new_state)
           
           
class address:
    def __init__(self,city,pin,state):
        self.__city=city
        self.pin=pin
        self.state=state
        
    def get_city(self):
        return self.__city
    
    def edit_address(self,new_city,new_pin,new_state):
        self.__city=new_city
        self.pin=new_pin
        self.state=new_state
        
 
        
add1=address('Aurangabad',824102,'Bihar')
cus1=customer('Ankit','Male',add1)
cus1.print_add()

cus1.edit_profile('MissPai','patana',824022,'Bihar')
cus1.print_add()
    
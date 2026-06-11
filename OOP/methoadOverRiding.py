# methoad overRiding meanse let if parent and child have same methoad name then child methoad will be execute

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
   def buy(self):
       print('buy a smartphon')
    
    
s=smdaartPhone(20000,'apple',13)
s.buy() 


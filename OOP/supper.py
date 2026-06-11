# supper key word is besicaly use for call parrent methoad
# super key only call in to the child calss and it not use outside of the class
# supeer can't access variable

 

# parrent
# class phone:
#     def __init__(self,price,brand,camra):
#         print('inside the phone class')
#         self.price=price
#         self.brand=brand
#         self.camra=camra
        
#     def buy(self):
#         print('phone is buying')
        
# class smdaartPhone(phone):
#    def buy(self):
#        print('buy a smartphon')
#        super().buy()
    
    
# s=smdaartPhone(20000,'apple',13)
# s.buy() 


class phone:
    def __init__(self,price,brand,camra):
        print('inside the phone class')
        self.price=price
        self.brand=brand
        self.camra=camra
        
    def buy(self):
        print('phone is buying')
        
class smdaartPhone(phone):
    def __init__(self, price, brand, camra,os,ram):
        print('inside the smartpohne')
        super().__init__(price, brand, camra)
        self.os=os
        self.ram=ram
        print('again inside the smartpohne')
         
    
s=smdaartPhone(20000,'apple',13,'ios',3)
s.buy() 

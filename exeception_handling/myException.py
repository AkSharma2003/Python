# in own exeption class also should be child on exception class

class myException(Exception):
    def __init__(self,message):
        print(message)

class bank:
    def __init__(self,balance):
        self.balance=balance
        
    def withdraw(self,amount):
        if amount<0:
            raise myException('amount cant be negative')
        if amount > self.balance:
            raise myException('you have not availble balance')
        
        self.balance=self.balance-amount

# example 1
obj=bank(10000)
try:
    obj.withdraw(5000)
except myException as e:
    pass
else:
    print(obj.balance)
finally:
    print('your command is successfull run')
    
# example 2    
obj2=bank(10000)
try:
    obj2.withdraw(20000)
except myException as e:
    pass
else: 
    print(obj.balance)
finally:
    print('your command is successfull run')
    
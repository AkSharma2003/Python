# raise Exception :- in python progrmaing exception are raised when error occures run time
# we can also manually raise exception usingn the rise keyword.
# we can optionally pass values to the exception to clearify why that exception was raised

class bank:
    def __init__(self,balance):
        self.balance=balance
        
    def withdraw(self,amount):
        if amount<0:
            raise Exception('amount cant be negative')
        if amount > self.balance:
            raise Exception('you have not availble balance')
        
        self.balance=self.balance-amount

# example 1
obj=bank(10000)
try:
    obj.withdraw(5000)
except Exception as e:
    print(e)
else:
    print(obj.balance)
finally:
    print('your command is successfull run')
    
# example 2    
obj2=bank(10000)
try:
    obj2.withdraw(20000)
except Exception as e:
    print(e)
else: 
    print(obj.balance)
finally:
    print('your command is successfull run')
    
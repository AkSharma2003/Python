
class Atm:
    # constructor
    def __init__(self):
        self.pin=""
        self.__balance=0 # here balance is private
        self.menu()
    
    def get_balance(self):
        print("balance is: ",self.__balance)
    
    def set_balance(self,val):
        if type(val)==int:
            __balance=val
        else:
            print("please enter correct details")
    
    def menu(self):
        user_input=input("""
                        How can i help you
                        1. press 1 to create pin
                        2, press 2 for change pin
                        3. press 3 for chaack balance
                        4. press 4 for withdraw
                        5. press anything for exits
                        """)
        
        #  pass :- if you dont use pass then it is IndentationError: expected an indented bloc
        if user_input == '1':
            #crreate pin
            self.createPin()
        elif user_input == '2':
            # change pin
            self.changePin()
        elif user_input == '3':
            # cheak balance
            self.cheak_balance()
        elif user_input == "4":
            self.withdraw_balance()
        else:
            exit()
        
    # for create pin
    def createPin(self):
        user_pin=input("Enter your pin: ")
        self.pin=user_pin
        
        user_balance=int(input('Enter your balance:'))
        self.balance=user_balance
        print("pin created successfull")
        self.menu()
    
    # for change pin
    def changePin(self):
        change_pin=input("enter your old password: ")
        if self.pin==change_pin:
            new_pin1=input("Enter new pin")
            new_pin2=input("Enter new pin")
            
            if new_pin1==new_pin2:
                self.pin=new_pin1
            else:
                print("botu pin are not match")
                
            print("Pin chaage successfully")
        else:
            print("you cant change pin 'Somthing is wrong' ")
        self.menu()
        
        
    # for cheack balance
    def cheak_balance(self):
        curr_pin=input("Enter your pin: ")
        if curr_pin==self.pin:
            print("curr balance is : ", self.__balance)
        else:
            print("Your pin is incorrect")
        self.menu()
        
    # for withdraw
    def withdraw_balance(self):
        curr_pin=input("Enter your pin: ")
        if curr_pin==self.pin:
            bal=int(input("Enter your withdraw amount"))
            if bal>self.balance:
                print("balance is not sufficioent")
            else:
                self.balance=self.balance-bal
                print("balamce withdraw successfully")
                print("your curr balance is ",self.__balance)
                
        else:
            print("Your pin is incorrect")
        
        self.menu()
        
        
# create an object of Atm class
obj=Atm()
        


 
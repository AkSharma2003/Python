# oop:- everything in python is object

# principle of python
# 1. class
# 2. object
# 3. abstraction
# 4. inheritance
# 5. encapsulation
# 6. polymorfism

# class :- class is blueprint  
    # it have two atribute 
        # 1. data or property
        # 2. functions or behavior


# object :- object is an instance of the class


# Syntax to create an object
# objectname =classname()

# object literal
# l=[1,2,3] or you can create without literal l=list()

# code of basic atm machine using calss

# what is function and methoad
# methoad:- function who is inside of class
# function:- independent or outside of class
    # for example
    # l=[1,2,3,4]
    # len(l) here len is function
    # l.append(2) here apend is methoad
    
    



class Atm:
    # constructor
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()
        
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
        curr_pin=input("Enter your pin: ");
        if curr_pin==self.pin:
            print("curr balance is : ", self.balance)
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
                print("your curr balance is ",self.balance)
                
        else:
            print("Your pin is incorrect")
        
        self.menu()
        
        
# create an object of Atm class
obj=Atm()
        


 
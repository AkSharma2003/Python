class SecurityError(Exception):
    def __init__(self,message):
        print(message)
        
    def logout(self):
        print('log out all device')
        

class google:
    def __init__(self,name,email,password,device):
        self.name=name
        self.email=email
        self.password=password
        self.device=device
        
    def login(self,email,password,device):
        if device!=self.device:
            raise SecurityError('somthing went wrong')
        if email==self.email and password==self.password:
            print('welcom to home')
        else:
            print('Login error')
        
obj=google('Ankit','ak@123gmail.com','1234','android')

try:
    obj.login('ak@123gmail.com','1234','and')
except SecurityError as e:
    e.logout()
else:
    print(obj.name)
finally:
    print('database connected successfully')
    
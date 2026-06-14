# decorator:-  decoratore in python is a function that recrives another function as input and adds some 
# functionality(decoration) to and it ans resumre it 
# this can happenon only becouse python function are 1st class citizens.
# there are two type of decorators availble in python 
#   1. builtin decorators:- like @staticmethoad, @classmethoad, @abstractmethoad, @property
#   2. user defind decorators:- that we programmer can creat according to our need


# python are first class function
def modify(func,num):
    return func(num)

def squre(num):
    return num**2

a=modify(squre,2)
print(a)


# simple example of decorator

def my_decorator(fun):
    def warp():
        print('*****************************')
        fun()
        print('*****************************')
    return warp 
    
        
def hello():
    print('hello')
    
a=my_decorator(hello) # here a is act a like a function becouse warp have no () so  
a()

# here is a shortcut methoad
@my_decorator
def ak():
    print('i love miss pai')
    
ak()
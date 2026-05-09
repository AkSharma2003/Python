def is_even(num):
    """
    this function return Even  and Odd base on its input
    input: valid integer
    output: even/odd
    """
    if num%2==0 :return "even"
    else: return "odd"

for i in range(1,11):
    print(is_even(i))


def sqr(a=1,b=1): # this is defoult argument
    print(a**b)

# Type of argumant
# positional argumnet:
sqr(2,3) 

# keyword argumnet
sqr(b=2,a=3) # it is not use positional argument


# args (use :-> *nmae )
def mult(*args): # besicaly arges convert all parameater in touple 
    # not complesary that here use only args its your choice
    product=1
    for i in args:
        product=product*i

    print("product of all number is: ",product)

mult(1,2,3,4,5,6,7,8,9,10)

# kwargs (use :-> **name)
def display(**kwargs): # besicaly kwarges conver all parameater to dictionary
    for (key,value) in kwargs.items():
        print(key,'->',value)

display(india='delhi', shrilanka='colomboo', nepal='kathmandu')

# when we use both *args and **kwargs then order is improtant
# first use *args then **kwargs name should be changable

# nested Function

def g():
    def f():
        print("i am inside the function f")
    f()
    print("i am inside the function g ")

g()

# function like immutable data type
# python function can return function

def fun():
    def x(a,b):
        return a+b
    return x;
val=fun() (3,4)
print(val)
    

# function are a first class cityzens
# use function like argument

def func_a():
    print("i am inside function a")

def func_b(z):
    print("i am inside function c")
    return z()

print(func_b(func_a))


# benifit of function
# 1. code Modularuty
# 2. code Readibility
# 3. code Reusability


# defefrant between lamda function and normal function
# no name
# lamda had no return value bcz it return whole function
# no reusable
# lamda function use in hof

# cheack that present a i given string
a=lambda s: 'a' in s
print(a('ankit'))

# odd or even
b= lambda num: 'even' if num%2==0 else 'odd'
print(b(4))


# function use as an input in a function then funnction called HOF
def squar(n):
    return n**2

# HOF
def transform(f,l):
    output=[]
    for i in l:
        output.append(f(i))

    print(output)

l=[1,2,3,4,5]
transform(squar,l)

# here is a problum that if i want to print cuble then right a new function of cube 
# for soolve this problum i will use lambda function inside whose function who take function as input
transform(lambda s:s**2,l) # it is same as previous
transform(lambda s:s**3,l)


# there are 3 hiegher order function 
# map :-> map besicaly expect two value one is lamda function and second is itrable and traivre every value of list
p=list (map(lambda s:s**2,[1,2,3])) # retunr a list of squara of given list
print(p)

p=list(map(lambda s: 'even' if s%2==0 else 'odd',[1,2,3,4,5])) # labeling of even odd in the given list
print(p)

users=[
    {
        'name':"Ankit kumar Sharma",
        'gender':'male',
        'age':22
    },
    {
        'name':"Like mom",
        'gender':'female',
        'age':18
    },
    {
        'name':"abc",
        'gender':'trans',
        'age':30
    }
]

q=list(map(lambda user:user['gender'],users)) # return all gender and store it in list q
print(q)

# filter :-> filter besicaly use for return filterd value with given list
fruits=['apple','guava','cherry']
a=list(filter(lambda item:item.startswith('a'),fruits))
print(a)

nums=[5,4,6,4,5,3,7,5]
b=list(filter(lambda num: num>=5,nums))
print(b)

# reduce :-> for use reduce first impot functools, 
# reduce besicaly reduce list 

# find sum of given list
import functools
l=[1,2,3,3,4]
a=functools.reduce(lambda x,y:x+y,l)
print("sum of all list item is:",a)

# find min in given list
l1=[2,3,4,0,6,-2]
a1=functools.reduce(lambda x,y: x if x<y else y,l1)
print("minimum value in given list is:",a1)




 

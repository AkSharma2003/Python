# NameSpace:- A namespace is a space that holds name(idetifires). programitly peeking, namespace are dictionary 
# of identifires(key) and their objects(value)

# there are 4 types of namespace
# 1. Builtin NameSpace
# 2. Globle NameSpace 
# 3. Enclosing NameSpace
# 4. Local NameSpace

# Scop:- A scop is a textual region of a python program where a namespace is directly accessible
# LEGB rull:- the interprator searched for a name from the inside out looking, in the local, encloasing globle, and finally 
# the built-in scope. if the life interprator doesn't find the name  any thes location, then python raise a nameError exception.

# local and globle samename

a=2
def temp():
    a=3
    print(a) # first cheack it local if avalble then print it otherwise globle

temp() # output is 3

def ram():
    print(a) # here is not local value of a so it found globle value of a

ram() #print 2


# built in scop
# for use builtins then foirst import builtins then prinf(dir(builtins))

import builtins
print(dir(builtins)) 

def outer():
    def inner():
        print('inner function')
    inner()
    print('outer function')
    
outer()
print('mian function')
        
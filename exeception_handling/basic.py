# there are two stages where error may happen in a program 
    # During complition:- SyntaxError
    # During Execution :- Exception
    
# SyntaxError:- 
#     somthing in the program is not writtn acording to the program gramerm
#     error is realesed by the interpretor/compiler
#     you can solve it by rectifying the program 

# some Example of Syntax Error
#     1. Leaving Symbol like colon, brackets
#     2. Misspelling a keywoed 
#     3. incorrect Indentation
#     4. empty if/else/loop/class/function
    
# Type of SyntaxError:- 
#     1. IndexError:- the index error is thrown when trying to access an item at an invailid index
#         L=[1,2,3]
#          but access L[100] this is index error 

#     2. ModuleNotFoundError:- the. moduleNotFoundError is thrown when a module could not be found
#           import mathi (here  mathi is not modul  )
#                 math.floor(5.3)

#     3. KeyError:- the KeyError is thrown when a key is not found 
#       d={'name':'nitish'}
#           d['age'] (here age is not key in the d so it is key error)

#     4. TypeError:- the TypeError is rhrown when an opration or function is applied to an object of an inappropriate type
#            1+'a' here we want to add an integer and charechtor so it is typeError

#     5. valueError:- the ValueError is thrown when a function's argument is of an inappropriate type
#           int('a') it is valueError 

#     6. nameError:- The name error is thrown when an object could not be. found
#           print(k) here k is not found

#     7. AttributeError :- 
#               L=[1,2,3]
#               L.upper() here upper is the string function but i want to use in list so it is Attribute Error


# Exceptions :- if things go wrong during the execution of the program(run time). it generally happens when something
# unforseen has happend 
#   exception are raised by python runtime
#   You have to takle is on the fly
#       example: 
                # Memory Overflow
                # Diviede by 0 -> logic error
                # DataBase error






# try and except block

with open('sample.txt','w') as f:
    f.write('hello world')
    
try:
    with open('sample.txt','r') as f:
        print(f.read())
except:
    print('file is not found in this address')
    
    
    
import numpy as np
a=np.random.random((3,3)) # create 3*3 matrix of rxndom  element
a=np.round(a*100) # multiply 100 and round it

print(a)


# max/min/sum/prod

print('min in given matrix is',np.min(a))
print('max in given matrix is',np.max(a))
print('sum of all element in given matrix is',np.sum(a))
print('product of all element in given matrix is',np.prod(a))

# in axies (0-> col, 1->row) {max,min,sum,prod} all is aplicable
print("min in all row",np.min(a,axis=1)) 

# mean/median/std/var {it is applicable in all row and collumn with axis and without }
p=np.mean(a,axis=1)
print(p)

# trignomatric function
print(np.sin(a))

# dot product
a=np.arange(12).reshape(4,3)
b=np.arange(12).reshape(3,4)

c=np.dot(a,b)
print(c)

# log and exponant 
print(np.log(a)) # it is log
print(np.exp(a)) # it is exponant 

# round/floor/ceil
print(np.round(np.random.random((2,3))*10)) # print 1 to 10 random number and stor it in matrix


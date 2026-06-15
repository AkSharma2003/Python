# numpy:- numPty is the fundamental packege for scientefic computing in python. it is a python library that providea
# multidimensional arry, obkect various derived objects(such as a mkrked array and matrics). and an assortment of routines
# for fast perations on arrays, including mathematical, logical, shape manupalation, sorting, selecting, I/O descrete fourior 
#  transforms, basic leanera alzebra, basic statics operations, random silmulation ans much more.

# -> At the core of thr numpy packege is the ndarray object. This encapsulate n-dimesional array of homogenious data types

# numPy Array vs python Sequance
# * numPay array have afixed size at creation, unlike Python list(whixh can grow dynemicaly). changing the size of an
#   ndArray will create a new array and delete the original

# * the element in a numPy array all required to be of the same data type, and thus will be the same data type, and thus will 
#   be the same size in memory .

# * numPy array faciliate advance mathematical and other types of operations on large numbers of data. typically such 
#   operations on large numbers of data typicaly such operation are executed more efficieantly and with less code than is 
#   posible using python's built-in sequances.

# * A growing plethora of scientific and mathematical Python based packege are using numPy arrays though typiclly support 
#   python-seqaunce input, they convert such input to numPy arrays prior to proceccingm, and they oftten output numPy arrays


# for using NumPy first import it

import numpy as np # here np is short form of numpy

a=np.array([1,2,3,4])
print(a) 

# using np.arange();
a=np.arange(1,11) # here 11 is not br includerd
print(a)

# with reshape .reshape(row,collumn) row*collumn must be total length of element
a=np.arange(1,11).reshape(2,5)
print(a)

# np.ones and np.zeroes
a=np.ones((4,3)) # all element is 1
print(a)
a=np.zeros((3,4)) # all element is 0
print(a)

# np.random()
a=np.random.random((3,4))
print(a)

# np.linspace(starting,end,count) {distance between two number is same of next two number}
a=np.linspace(-10,10,5)
print(a)

#np.identity(n) generate n*n identity matrics
a=np.identity(3)
print(a)




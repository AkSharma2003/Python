import numpy as np



a=np.arange(10)
b=np.arange(12).reshape(4,3)
c=np.arange(8).reshape(2,2,2)

print(a)
print(b)
print(c)


# indexing and slicing is besicaly like normal python


# nditer :-> conver in 1 d array and print it
# ravel is same as nditer 

for i in np.nditer(b):
    print(i)
import numpy as np
# fancy indexing 
a=np.arange(24).reshape(6,4)
print(a)
c=a[[0,1,3]] # 1,2,4 row
print(c)

c=a[:,[0,3]] # 1 4 colllumn
print(c)

#boolian indexing
a=np.random.randint(1,100,24).reshape(6,4)
print(a)

# based on comdition
# grater than 50

c=a[a>50] # defiend all element who is grater than 50
print(c)

c=a[(a>50)&(a%2==0)] # here use & becouse use in only booleon 
print(c)
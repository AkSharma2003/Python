import numpy as np

a=np.arange(10)
b=np.arange(12,dtype=float).reshape(12,1)
c=np.arange(8).reshape(2,2,2)

print(a)
print(b)
print(c)

# ndim -> it is return dimemtional of array

print(a.ndim)
print(b.ndim)
print(c.ndim)

# shap and size -> number of items in every dimantionn, total element in given matrics

# itemsize -> return item size

print(a.itemsize)

# dtype -> return data type of given matrix element

 
# scaler operator
print(a+2)
print(b*2)  

# rlational operator
print(a>5)


# vector opration
print(a*b)


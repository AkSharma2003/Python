# Broadcasting:- The term broadcasting describes how numpy treats array with defrent shap
# the smaller  array is broascating acroos the larger array so that they have compleatble shape

import numpy as np

a=np.arange(6).reshape(2,3)
b=np.arange(3).reshape(1,3)

print(a+b)


# broadcasting rules:- 
# 1. make the two array have the same number of dimensions
#   -> if the number of dimensions of the two arrays are diffrent, add new dimendions with size 1 to the head of the array 
#       with the simmilar dimensions

# 2. make each dimensions of two array the same size
#    -> if the size of each dimensions of the two arrays do not match, dimensions with size 1 are streached to the size of 
#       the other array
#    -> if there is a dimension whose size is not 1 in either of two array it can not be boardcast, and an error is raised

a=np.arange(6).reshape(2,3)
b=np.arange(3).reshape(3)

print(a+b) 

a=np.arange(3).reshape(1,3)
b=np.arange(3).reshape(3,1)
print(a+b)
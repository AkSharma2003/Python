# stacking besically add two or matrix (shape should be same)
# there are two types of stacking 
# 1. horizontal stacking
# 2. Vertical stacking

import numpy as np

a=np.arange(12).reshape(3,4)
b=np.arange(12).reshape(3,4)

# horizontal stacking
c=np.hstack((a,b))
print(c)

# vertical stacking
c=np.vstack((a,b ))
print(c)



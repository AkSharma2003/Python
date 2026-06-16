import numpy as np

a=np.array([1,2,3,3,4,np.nan,6]) # here np.nan is a missing value simmilar to none but none and nan is deferent

b=a[~np.isnan(a)] # remove all empty value
print(b)
import sys # sys is useualy for system data
import numpy as np
import time

# python list vs numpy array (in turms of time)
a=[i for i in range(10000000)]
b=[i for i in range(10000000,20000000)]
print("print without using np",sys.getsizeof(a))

c=[]
start=time.time()
for i in range(len(a)):
    c.append(a[i]+b[i])

print(time.time()-start)

a=np.arange(1000000)
b=np.arange(1000000,2000000)
start=time.time()
c=a+b
print(time.time()-start)

# python list vs numpy array (in turms of memeory)

print("print using np",sys.getsizeof(a))

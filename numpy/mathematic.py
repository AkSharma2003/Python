import numpy as np

# sigmoid
def sigmoid(arr):
    return 1/(1+np.exp((-arr)))

a=np.arange(100)
b=sigmoid(a)
print(b)


# mean squad error
def mes(act,pre):
    return np.mean((act-pre)**2)

act=np.random.randint(1,50,25)
pred=np.random.randint(1,50,25)

a=mes(act,pred)
print(a)


# binary cross entropy


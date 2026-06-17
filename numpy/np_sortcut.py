import numpy as np

# np.sort :- return a sorted copy of an array
a=np.random.randint(1,100,15) # 1D array
print(a)
a=np.sort(a)
print(a)

b=np.random.randint(1,100,15).reshape(5,3)
print(b)
b=np.sort(b)# sorted in row wise by default (axies=1)
print(b)
b=np.sort(b,axis=0) # sorted by collumn
print(b)


# np.append :- the numpy.append() append values along the mentioned axis at the end of the array 
mt=np.random.randint(1,50,15).reshape(5,3)
print(mt)
mt=np.append(mt,np.random.randint(1,10,5).reshape(5,1),axis=1) # for append it matrix name,column/ row name then posotion like axis 1 or 0
print(mt)



# statics (bwllow function mostky ude in statistics)
# np.concatenate :- numpy.concatenate() function concatenate of a sequance of arrays along an existing axis
m1=np.arange(6).reshape(2,3)
m2=np.arange(6,12).reshape(2,3)
print(m1)
print(m2)
c=np.concatenate((m1,m2),axis=1) #for collum wise
print(c)
c=np.concatenate((m1,m2),axis=0) #for row wise
print(c)


#np.unique :- with the help of np.unoque() methoad, we can get the unique value from an array given as parameter in
#             np.unique() methoad 
e=np.array([1,2,1,2,3,4,4,3,4,2,1,4])
a=np.unique(e)
print(a)


# np.expand_dims :- with the help of Numpy.expand_dims() methoad, we can get the expanded dimension of an array 
a=np.array([1,2,45,23,44,34])
print(a)
b=np.expand_dims(a,axis=0)
print(b,b.shape)
c=np.expand_dims(a,axis=1)
print(c,c.shape)


# np.where :- the numpy.where() function returns the indices of element in the input array where the given condition 
#             is satisfied
a=np.array([11,53,28,500,34,56,56,6,76,3,34,56])
b=np.where(a>50)
print(b) # return indexing of givrn array

c=np.where(a>50,0,a) # here is conditional statment if a is grater than 50 then replace with 0 
print(c)


# np.argmax :- numpy.argmax() function returns indices of the max element of the array in the particular axis
a=np.random.randint(1,20,6).reshape(1,6)
print(a)
print(np.argmax(a))

b=np.random.randint(1,50,12).reshape(3,4)
print(b)
print(np.argmax(b,axis=0)) # column wise
print(np.argmax(b,axis=1)) # row wise 


# np.argmin() :- numpy.argmax() function returns indices of the min element of the array in the particular axis
a=np.random.randint(1,20,6).reshape(1,6)
print(a)
print(np.argmin(a))

b=np.random.randint(1,50,12).reshape(3,4)
print(b)
print(np.argmin(b,axis=0)) # column wise
print(np.argmin(b,axis=1)) # row wise 


# np.cumsum :- numpy.cumsum()function is used when we want to compute the cumulative sum of array element of given axis
a=np.random.randint(1,30,6).reshape(1,6)
print(a)
print(np.cumsum(a))

b=np.random.randint(1,50,12).reshape(3,4)
print(b)
print(np.cumsum(b,axis=0)) # column wise
print(np.cumsum(b,axis=1)) # row wise 


# np.cumprod() ;- numpy.cumsum()function is used when we want to compute the cumulative product of array element of given axis
a=np.random.randint(1,30,6).reshape(1,6)
print(a)
print(np.cumprod(a))

b=np.random.randint(1,50,12).reshape(3,4)
print(b)
print(np.cumprod(b,axis=0)) # column wise
print(np.cumprod(b,axis=1)) # row wise 


# np.percentile :- numpy.prcentile() function used to compute the nth percentile of the given data (array of element) along
#                  the specified axis
a=np.random.randint(1,30,6).reshape(1,6)
print(a)
print(np.percentile(a,100))


# np.histogram :- numpy has a built in numpy.histogram() functionwhich repersents to the frequency oif data distrbution in 
# the graphical form
a=np.random.randint(1,100,20).reshape(1,20)
print(a)
print(np.histogram(a,bins=[0,20,40,60,80,100]))


# np.corrcoef :- Return pearson product moment correlation coefficients
salary=np.array([20000,30000,40000,230000])
exp=np.array([1,2,3,8])
print(np.corrcoef(salary,exp))


# utilit function
# np.isin :- with the help of numpy.isin() methoad, we can see the one array having values are cheaked in a deferent numpy
#            array having different elements with diffiren sizes
a=np.array([11,53,28,500,34,56,56,6,76,3,34,56])
items=np.array([5,6,7,8,9,10,11])
ch=np.isin(a,items)
print(ch)
print(a[ch])


# np.flip() :- the numpy.flip() function reverse the order of array elements along the specified axies, preserving 
#              the shape of the array 
a=np.random.randint(1,100,20).reshape(1,20)
print(a)
print(np.flip(a))

b=np.random.randint(1,50,12).reshape(3,4)
print(b)
print(np.flip(b)) # row and collum
print(np.flip(b,axis=0)) # column wise
print(np.flip(b,axis=1)) # row wise 



# np.put() :- the numpy.put() function replaces specific elemnt of an array with given values of p_array. Array indexed 
#             works on flattend array it change in original array
a=np.array([11,53,28,50,34,56,56,6,76,3,34,56])
print(a)
np.put(a,[0,1],[22,33]) # put(array_name,[position],[new_value])
print(a)


# np.delete() :- the numpy.delete() function return a new array with the delation of sub-arrays along with the mentioned axis
a=np.array([11,53,28,50,34,56,56,6,76,3,34,56])
print(a)
b=np.delete(a,[0,2,3]) # delete(array_name,[position])
print(b)



# set function
a=np.array([1,2,3,4,5])
b=np.array([3,4,5,6,7,])
print(a)
print(b)
# np.union1d
print(np.union1d(a,b))
# np.intersect1d
print(np.intersect1d(a,b))
# np.setdiff1d
print(np.setdiff1d(a,b))
# np.setxor1d
print(np.setxor1d(a,b))
# np.isin
b=np.isin(a,1)
print(b)
print(a[b])


# np.clip() :- numpy.clip() function is used to clip(limit) the value in an array
a=np.array([1,22,34,56,76,54,678,66,46,3463,67])
print(np.clip(a,a_min=10,a_max=100))


# List :- we can Store multiple data type in a single list and it is dynamic array and refrantial array
# ["Ankit",3.24,4,[2,3,4]] like this
# list is hetrogenious but array is homogenious
# consume extra memory and slower than array
# list is mutable means you can edit

# Empty List
print([])

# 1D List
print([1,2,3]) #also Homogenius list

# 2D List
print([1,2,3,[4,5]]) #it is hetrogenius List

#3D List
print([[[1,2,3],[2,5,6]],[[7,1,2],[1,2,4]]]) #it is Homogenius list

# hetrogenius List
print(1,2.4,True,"Ankit")

#convert in to list
print(list('helo')) # convert all char int list of elment

# slicing
l=([1,2,3,4,5])
print(l[0:3]) # start from 0 index and print if 3 is less than size of list then print all value of list

# adding items in list
# append()-> add only one item in the last of list
# extend()-> add more than on item in the list
# insert(position,want io add) -> add any position in list one element

l.append(True)
print(l)
l.extend([2,3,4,'heloo'])
print(l)

# cheak in reverse
l.append([2,3,4,'heloo']) # apend list 
print(l)
l.extend('Hello') # first break than apend like H 
print(l)
l.insert(1,100)
print(l)

#eidting list
p=([1,2,3])
print(p)
p[1]=5 # editing with indexing
print(p)
p[1:4]=(100,200,300,400) # editing with slicing
print(p)

# deletenig list
# 1. del :-> p then delete all list but 
# del p[index] delete item of particular list here can use slicing method also
del p[1]
print(p)
# 2. pop :-> p.pop(index) delete paritucal index and return it but 
p.pop(1)
print(p)
# p.pop() delete last elemnt of given list
p.pop()
print(p)
# 3. remoove :-> use for particular element p.remove(400) then it find 400 and delete it
# p.remove(400) if 400 not present then throw error
p.remove(300)
print(p)
# 4. clear :-> p.clear() remove all element from list and make it empty list
p.clear()
print(p)


# oprator on list
# 1. arithmatic oprator :-> +,*
q=([2,3,4])
print(p+q) # merge p and q list items then print
print(q*3) # repeat 3 times of list q and merge it then print

# 2. membership oprator :-> in, not in
s=[1,2,3,[4,5]]
print(4 in s)
print([4,5] in s)
print(3 not in s)

# 3. loop
for i in s:
    print(i)


l1=([3,4,1,23,43])
# function in list
# 1. min,max,sorted :-> it is aplicable for sorted data only
print(min(l1))
print(max(l1))
print(sorted(l1)) # 1,3,4,23,43 it is temprory sorted

# len,count :-> 
print(len(l1))
p1=([1,2,1,2,4,3,4,5,64,54])
print(p1.count(2)) # return  number of 2 in given list

# index :-> return first occurance in given list of particular item




# List Comperhension
#1. add 1 to 10 in a list

L=[i for i in range(1,11)]
print('List using List comperhensing {}'.format(L))

s=[i**2 for i in L]
print(s)

# print all number 1 to 50 who is devisible by 5
print([i for i in range(1,51) if i%5==0])


# way to triverse list
# item wise, index wise

# item wise
for i in p1:
    print(i,end=' ')

print()

# index wise

for i in range(0,len(p1)):
    print(p1[i],end=' ')

print()

# Zip() :-> besicaly make a touple in given list
a=([1,2,3])
b=([-1,-2,-3])

print([i+j for i,j  in zip(a,b)])


# risky to use list in python
m=([1,2,3])
n=m
o=m.copy()
print("m=",m)
print("n=",n)
print("o=",o)
m.append(4)
print("m=",m)
print("n=",n)
print("o=",o)





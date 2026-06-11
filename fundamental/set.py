# set :-> set is unordered colection of times
# every set have unique colection and it is mutable, also can't contain mutable data types

# creating set
s=set() # impty set {} is empty dectionory 
print(s)
s1={1,2,3,4} # it is homogenious set
print(s1)

s2={1,'hello',(12,3,4)} # hetro
print(s2)

# set oprations
print("set opration")
s3={1,2,3,4}
s4={3,4,5,6}
# 1. union s3|s4
print(s3|s4)

# 2. intersection s3&s4
print(s3&s4)

# 3. Difference s3-s4
print(s3-s4)

# 4. Symetric defrance s3^s4
print(s3^s4)

# also you can use membership opperator and loops in set
# len, max, min, shorted, sum also use 

# union and update
print(s3.union(s4)) # print union of both 
s3.update(s4) # chenge s3 to union of s3 and s4 
print("s3= ",s3)
print("s4= ",s4)

# intersection and intersection_update
# differance and difference_update
# symetric_diffrence and symetric_diffrence_update
# above 3 function look like union and union_update 

# isdisjoint, issubset, issuperset

print(s3.isdisjoint(s4))
print(s3.issubset(s4))
print(s4.issuperset(s4))

# copy :-> create copy of set who have defrent address that means deep copy







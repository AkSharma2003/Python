# dic is a cloction of key and value use for store value like map it also known as asosiative array
# {'name':'Ankit', 'age':'22'} it is dictionary
# it is mutable
# indexing has no meaning
# key can't be duplicate
# key can't be mutable items

# create dictionary

d={} # empty dictionary
print(d)

# 1d dictionary 
d1={'name':'Ankit Kumar Sharma', 'age':'22', 'Gender':'Male'} # homogenius dictionary
print(d1) 

d2={(1,2,3):1,'name':'pai'} # mixed dictionary
print(d2)

# 2d dictionary
s={
    'name':'Miss Pai',
    'age':19,
    'marks':{
        'english':90,
        'math':80
    }
}
print(s)

# using sequance and dict function
d3=dict([('name','ankit'),('gender','male')])
print(d3)

# accesing data from dictinary
# []
print(d1['name'])
# get 
print(d1.get('name'))

# add value in dictionary
d1['coll']='IIIT'
print(d1)

# remove key value
# pop(key)
d1.pop('coll')
print(d1)

#popitem() delete last item
d1.popitem()
print(d1)

# del
del(d1) # dlete d1 full
#print(d1) # you can't print this
d1={'name':'Ankit Kumar Sharma', 'age':'22', 'Gender':'Male'}
del(d1['name']) # delete specific behavior like pop
print(d1)
# clear() :-> clear full dictionary
#d1.clear()
print(d1)

# editing is normal like all array 
d1['age']=23
print("change age 22 to 23: ",d1)

# loop in dict
for i in d1:
    print(i,d1[i])# becouse i is key of given dictionary

# len, max, min also is dict function
# len return leghth of dict
# max return maximum key and min return minimum key using asici value   


# items, key, values
print(d1.items()) # print all key and value in tuople form
print(d1.keys()) # print all key of dict
print(d1.values()) # print all values of given dict

# update :-> update besicaly update permamemtly dictionary key and value 
p1={1:2,2:3,3:4}
p2={3:5,4:5}
print("p1: ",p1)
print("p2: ",p2)
p1.update(p2)
print("after update p1:",p1)
print("after update p2:",p2)

# dictionary comperhentioin behavior like list touple set and all over this 






# what is pandas :- pandas is fast, powerfull, flexible, and easy to use open source data analysis ans manipulation tool,
# built on top of the programnig langeuage 

# pandas sereis :- A pandas sereis like a collumn in a table. it is a 2-D array holding data of any type 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# using list
# string
country =['India','Pakistan','Shrilanka','Nepal']
a=pd.Series(country)
print(a)

# integer
age =[34,45,43,56,56,78,]
a=pd.Series(age)
print(a)

# custom index
marks=[68,89,90,100]
subject=['English','Hindi','Science','Math']
a=pd.Series(marks,index=subject,name='Ankit ka marks' )
print(a)

# using dictionary

marks={
    'English':68,
    'Hindi':89,
    'Science':90,
    'Math':100
}
print(pd.Series(marks,name='new marks'))


# series attributes
# size
print(a.size) # 4

# dtype
print(a.dtype) # int64

# name
print(a.name) # Ankit k marks

# is_unique
print(a.is_unique) # True

# index
print(a.index) # ['English','Hindi','Science','Math']

# value
print(a.values) 


# series using red_csv
# witb one col 
subs=pd.read_csv('/Users/paimatho/Desktop/Python/pandas/customers-100.csv',index_col='Customer Id')['First Name']
# in sub here 12 collum but in the series only two collum is avaible
print(subs)
print(subs.name)
print(type(subs))

# series methoad
#head and tail
print(subs.head(20)) #bydefault 5 top 
print(subs.tail()) #bottom

# sample -> random select by default 1
print(subs.sample())

# value_counts :- count the value
print(subs.value_counts())

# sort_values for change original data use (inplace=True)
print(subs.sort_values(ascending=False)) # by default ascending order

#soert_index :- samne as like sort_value


# series Maths Methods
# count :- it is count all vale excpet non but size all value count
print(subs.count())

# sum and product :- sum all value and product all value
# mean, ,median, mode, std, var
# min and max

# describe :- make a summry
print(subs.describe())


# series indexing it is working only posative integer
x=pd.Series([12,13,14,35,46,54,39,89,90])
print(x)
print(x[3])
print(subs['7E441b6B228DBcA']) 

# fancy indexing
print(x[[1,3,5]])


# edit series
# 1. using indexing, 2. slicing, 3. fancy indexing, 


# Series with Python functionalities
# len, type, dir, sorted, max, min 
print(len(x))
print(type(x)) 
print(dir(x))
print(sorted(x))
print(max(x))
print(min(x))

# type conversing convert any type like list and dict also
print(dict(subs))

# membership operator :- it run by default on the index
print(subs)
print('cb8E23e48d22Eae' in subs) # true
print('Lynn' in subs) # false becouse Lyma is in name not in idexing
print('Lynn' in subs.values) # true becouse i am cheacking in values and Lynn is in the value collumn

# loop :- it run by default on the value
for i in subs:
    print(i)
for i in subs.index: # loop on index
    print(i)
    
# arithmatic opration(Broadcasting) You can use all operator also relation operator
print(100-x)
a=(50>x)
print(x[a])


# Line plot
plt.figure()
x.plot()
plt.title("Line Plot")

# Bar plot
plt.figure()
x.plot(kind='bar')
plt.title("Bar Plot")

# Pie plot
plt.figure()
x.plot(kind='pie')
plt.title("Pie Plot")

plt.show()




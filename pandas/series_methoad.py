import numpy as np
import pandas as pd;
vk=pd.read_csv('/Users/paimatho/Desktop/Python/pandas/data/kohli_ipl.csv',index_col='match_no')['runs']
print(vk)

# astype you can change size of any thing
import sys
sz=sys.getsizeof(vk)
print(sz)
vk=vk.astype('int16')
print(vk.dtype)
sz=sys.getsizeof(vk)
print(sz)

# betweem :- find the value exists or not in the given range and retuern true and false
print(vk[vk.between(51,99)])

# clip :- increase value between given range
print(vk.clip(50,100))
print(vk.drop_duplicates()) # by default first 
print(vk.drop_duplicates(keep='last')) # last

# cheak that duplicate value is present or not 
print(vk.duplicated())  
print(vk.duplicated().sum()) # count total value of duplicate

# isnull :- cheak that given value is null or not
print(vk.isnull())
print(vk.isnull().sum()) # count tatal null value

# dropna :- drop all na value and create a new sereis who have no any null value
print(vk.dropna())

# fillna :- by this methoad you can replace missing value by any value 
print(vk.fillna(0)) # here repalce by 0 of all missing or null value

# isin :- besicaly cheak condition that given value is exist or not
cond=vk.isin((vk==49) | (vk==99))
print(vk[cond])
print(vk[(vk==49) | (vk==99)])

# apply :- for use custum function who created by you
print(vk.apply(lambda x: 'good day' if x> vk.mean() else 'bad day'))

# copy :- creat a copy of intire data
new =vk.head().copy()
print(vk)
new[1]=100
print(vk)
print(new)


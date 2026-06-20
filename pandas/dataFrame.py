# what is data frame :- 2D structuctor of data consisting  of rows and collumn  is called data frame

import numpy as np
import pandas as pd

# data frame config 
# using list

student_data=[
    [100,80,14],
    [120,70,21],
    [80,90,14],
    [70,50,2],
]
daata=pd.DataFrame(student_data,columns=['iq','marks','pakege'])
print(daata)

# using dict
student_dic={
    'name':['Ankit','Miss Pai', 'matbho','nitishj'],
    'iq':[100,120,80,70],
    'marks':[80,70,90,50],
    'package':[14,21,14,2]
}

marks=pd.DataFrame(student_dic)
print(marks)

# using read_csv
d=pd.read_csv('/Users/paimatho/Desktop/Python/pandas/customers-100.csv')
print(d)

match=pd.read_csv('/Users/paimatho/Desktop/Python/pandas/matches.csv')
print(match)

# dataFram atributes and methoad
# shape
print(d.shape)

# dtypes
print(match.dtypes)

# index
print(match.index)

#columns
print(match.columns)
print(d.columns)

# values
print(match.values)

# head & tail
print(match.head())
print(match.tail())

# sample
print('here is sample')
print(match.sample(5))

# info
print(d.info())

# describe
print(match.describe())

# isnull
print(match.isnull().sum())

# duplicate
print(match.duplicated())

# rename 
change=marks.rename(columns={'marks':'percenatge','package':'lpa'},inplace=True) # for perma nant change inplace=true;
print(change)
print(marks) # here rename is changed permanantly

# math function
# same as sries and numpy


# slecting col from DataFrame 
#.   ->  single collumn is series and multiple collumn is dataframe
# single collumn
print(match['venue']) # it is series
print(type(match['venue']))

# multiple collumn
print(match[['venue','highscore']]) # here passes a list for fatching atributes
marks.set_index('name',inplace=True)
print(marks)

# seleting row from a dataset
#   -> iloc :- searching using index position
#   -> loc :- searching using index labels
# single row
print(match.iloc[0])
# multiple row
print(match.iloc[0:5]) # first five row
# fancy indexing
print(match.iloc[[0,3,4]]) # particular row using indexing value

# using loc
print(marks.loc['Ankit'])

# selsecting both row and column
print(marks.iloc[0:3,0:3])
print(match.loc[0:2, 'venue':'toss_winner'])


# filtering a DataFrame
print(match[['match_winner',]])


# Add new collumn
# compleating new
print(daata)
daata['location']='india'
print(daata)
# from existing new



# astype :- reduce memory oot print


# GroupBy:- The study of group is called groupBy
import numpy as np
import pandas as pd

movie=pd.read_csv('/Users/paimatho/Desktop/Python/pandas/data/imdb-top-1000.csv')
ipl=pd.read_csv('/Users/paimatho/Desktop/Python/pandas/data/deliveries.csv')

gener=movie.groupby('Genre') # use group by here

# Q1. Find the top 3 genres by total earning
gross=gener.sum()['Gross']
print(gross.sort_values(ascending=False).head(3))

# Q2. find the genre with hieghest avg IMDB rating
rat=gener['IMDB_Rating'].mean()
print(rat.sort_values(ascending=False).head())

# Q3. find director with most popularty
gener=movie.groupby('Director')
vote=gener['No_of_Votes'].sum()
print(vote.sort_values(ascending=False).head(1))

# find the total movie done by actor not use count_value
gener=movie.groupby('Star1')['Director'].count()
print(gener.sort_values(ascending=False))

# find the total number genre 
print(len(movie.groupby('Genre')))

# find the total number of row in each row
print(movie.groupby('Genre').size())

# first And Last and nth position in group by methaod
gener=movie.groupby('Genre')
print('First value of each genre')
print(gener.first())
print('Last value of each genre')
print(gener.last())
print('7th value of each genre')
print(gener.nth(6)) # if not avlaible in 7th value then skip the group 

# get_group :- print particular group data
print(gener.get_group('Horror'))

# groups :- return a dictionry and it have postion or indexing of particular data
print(gener.groups)

# describe() :- crate all mathematical operation
print(gener.describe())

# sample :- random 
print(gener.sample())

# nunigue :- give unique value
print(gener.nunique())

# agg methoad :- it means aggrigate methoad for it use passing dictionary
val=gener.agg({
    'Runtime':'mean',
    'IMDB_Rating':'mean',
    'No_of_Votes':'sum',
    'Gross':'sum',
    'Metascore':'min'
})

print(val)

# passing list
val = gener[['Runtime','IMDB_Rating','No_of_Votes','Gross','Metascore']].agg(['min','max','mean'])
print(val)

# looping on group
# Q find the higher eted moovie of each gener
df=pd.DataFrame(columns=movie.columns)
for group,data in gener:
    temp=data[data['IMDB_Rating']==data['IMDB_Rating'].max()]
    df=pd.concat([df,temp]) # append is removed in new pandas library
print(df)

# apply :- it work in three stage spliting, add custom methoad then combine
# Q find number of moovie startung with A of each group 
def foo(group):
    return group['Series_Title'].str.startswith('A').sum()

print('here is something change')
data=gener.apply(foo) # here you can use built in methoad
print(data)

# Q find the ranking of movie in the group according to IMDB rating
def ranking(group):
    group['rank']=group['IMDB_Rating'].rank(ascending=False)
    return group

f=gener.apply(ranking)
print(f)

# group by on multiple column
duo=movie.groupby(['Director','Star1'])
print(duo.size())

# Q find the most earning actor->director combo
ans=duo['Gross'].sum().sort_values(ascending=False).head(1)
print(ans)

# Q find the best(interms of meta score(avg)) actor->gener combo
duo=movie.groupby(['Genre','Star1'])
ans=duo['Metascore'].mean().reset_index().sort_values('Metascore',ascending=False).head(1)
print(ans)


# practice Q uestion
# Q1. find top 10 bestman in the basses of run 
play=ipl.groupby('batsman')
sm=play['batsman_runs'].sum()
print(sm.sort_values(ascending=False).head(10))

# Q2. find the batsman with most number of six
six=ipl[ipl['batsman_runs']==6]
six=six.groupby('batsman')['batsman'].count()
print(six.sort_values(ascending=False).head(10))


# Q3. find bestman with most number of 4's and 6's in last 5 over
last=ipl[ipl['over']>15]
last=last[(last['batsman_runs']==4) | (last['batsman_runs']==6)]
last=last.groupby('batsman')
print(last['batsman'].count().sort_values(ascending=False).head(10))

# Q4. find V kohli's record againts all teams
v=ipl[ipl['batsman']=="V Kohli"]
v=v.groupby('bowling_team')
print(v['batsman_runs'].sum().sort_values(ascending=False).reset_index())
print(v)

# Q5. create a function that can return the highest score of any batsman
def heighest(batsman):
    bt=ipl[ipl['batsman']==batsman]
    return bt.groupby('match_id')['batsman_runs'].sum().sort_values(ascending=False).head(1).iloc[0] # values not exist in the mordern pandas


print(heighest('MS Dhoni'))


print(ipl.columns)

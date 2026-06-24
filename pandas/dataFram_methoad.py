import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # for create pai chart
# pd.set_option('display.max_rows', None) # all value print means unlimited
#pd.set_option('display.max_columns', None) # all value print means unlimited
# 0 makes pandas auto-detect your terminal height/width dynamically
# pd.set_option('display.width', 0)

# value count :- it count unique value in given data set (applicavle on series and datafram)
marks=pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14]
    ],columns=['iq','marks','package'])

print(marks)
print(marks.value_counts()) # besiclay it return value count of row
ipl=pd.read_csv('/Users/paimatho/Desktop/Python/pandas/ipl-matches.csv')
bestman=pd.read_csv('/Users/paimatho/Desktop/Python/pandas/batsman_runs_ipl.csv')
# Q1. print all olayer who have how many man of the matches
print(ipl[ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts())

# Q2. Toss decision plot
ipl['TossDecision'].value_counts().plot(kind='pie')
# plt.show() # showing pie chart

# Q3. find which player has won most potm -> in final and qualifirs

# Q4. how many matches each team has played
team1=ipl['Team1'].value_counts()
team2=ipl['Team2'].value_counts()
print((team1+team2).sort_values(ascending=False))


# sort_values :- it is alicavle for series and dataafram both
# in the datafram if missing data is present then ussing(na_position) you can find all nan at the top or bottom

# rank (series) :- it provide ranking system 
rk=bestman['batsman_run'].rank(ascending=False)
print(rk)
bestman['batting_rank']=rk
print(bestman)
print(bestman.sort_values('batting_rank'))


# set_index (dataFram) -> inplace by default false
bestman.set_index('batter',inplace=True)
print(bestman)

# reset_index(series+datafram) -> drop parameater it have also inplace by default false
bt=bestman.reset_index()
print(bt)
print(bestman)

# Q set index as batting rank without missing old value
bt=bestman.reset_index().set_index('batting_rank')
print(bt)

# if you want to convert datafram from series then use reset_index() methoad
marks={
    'English':68,
    'Hindi':89,
    'Science':90,
    'Math':100
}
marks=pd.Series(marks,name='new marks')
print(type(marks))
print(type(marks.reset_index()))
marks=marks.reset_index()

# rename(datafram) -> index
print(marks)
marks.rename(columns={'index':'subject','new marks':'marks'},inplace=True)
print(marks)

# unique(series) :- count all unique value including non value also
# nunique(series+datafram) :-  it count all unique value 

# isnull(series+datafram) :- cheak that null value is present in the series or datafram
print(marks.isnull())

# notnull(series+datafram) :- cehak that not null value present in the given series or datafram
print(marks.notnull())

# hasnans(series):- it is cheack that missing value is present or not in the columns return true or false
print(marks['subject'].hasnans)

# dropna(series+datafram) :- if any columns have no ot missing value then remove whole row
#       -> if you can modify his feature then use how it have by default any 
#       -> it is also applicable for columns base for use column base use dropna(subset=['columns name'])

# fillna(series+datafram) :- replace missing value from all datafram or series according to your given data

# duplicate(series + datafram) :- cheak that any duplicate row exist or not
# drop_duplicate(series+datafram) :- remove duplicate 

# drop(series and datafram) :- name.drop(index=[index_position])
#           in datafram name.drop(column=[column name]) and for row same as series

# apply(series+datafram) 
temp=pd.Series([10,20,30,40,50])
def sigmoid(value):
    return 1/1+np.exp(-value)

temp=temp.apply(sigmoid)
print(temp)

point_df=pd.DataFrame(
    {
        '1st point':[(3,4),(-6,5),(0,0),(-10,1),(4,5)],
        '2nd point':[(-3,4),(0,0),(2,2),(10,10),(1,1)]
    }
)

print(point_df)

def calulate(row):
    p1=row['1st point']
    p2=row['2nd point']
    
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

dis=point_df.apply(calulate,axis=1)
point_df['dis']=dis
print(point_df)






import pandas as pd
import numpy as np
#fetch the file to work with
df = pd.read_csv('./data/student_scores.csv',header=0)
print(df)
print(df.shape)
print(df.describe())
print(df.info)

#Split Data into Groups
print('\n===========split data===============')
item_group = df.groupby('first_name')
print(item_group.groups)

#groupby using multiple columns 
Groupby_MultipleColumns = df.groupby(['first_name', 'last_name'])
print('\n===========multiple cplumns groups===============')
print(Groupby_MultipleColumns.groups)

#Iterating through Groups
print('\n=============Iterating through Groups=============')
for name,group in item_group:
    print('{}:'.format(name))
    print(group)

    #using  get_group method to select a particular group
print('\n=============using get_ Group mothod=============')
item_group = df.groupby('Subject')
#item_group.groups
print(item_group.get_group('Calculus'))

# Directly using mean() function
print('\n=============aggregating groups=============')
agg_group_subject = df.groupby('Subject')['score'].mean()
print(agg_group_subject)

#calculate average score of each student
agg_group_stu = df.groupby(["first_name", "last_name"])['score'].mean()
print(agg_group_stu)

# Aggregation group for Multiple columns:
agg_group = df.groupby(["first_name", "last_name"])['score'].aggregate([np.mean,np.sum])
print(agg_group)

# count the number of students
agg_group_count = df.groupby(["first_name", "last_name"])["id"].count()

print(agg_group_count)

#Find the highest score of the each Student
print('\n=============highest score of each student=============')
print(df.groupby(["first_name", "last_name"]).max())

#Find the lowest score of the each Student
print('\n=============lowest score of each student=============')
print(df.groupby(["first_name", "last_name"]).min())
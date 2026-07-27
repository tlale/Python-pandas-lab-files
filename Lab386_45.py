import pandas as pd
import numpy as np
#df = pd.read_csv ('./data/employee.csv')
zoo =pd.read_csv('./data/zoo.csv')
print(zoo)
print('\n ======show the zoo table information======')
#zoo.info()
#pandas count
#print(zoo.count()) 
#zoo[['animal']].count() preffered method to show zoo table colums and count
print(zoo[['animal']].count())
print(zoo[['water_need']].count())
print(zoo[['uniq_id']].count())
#alternative way for above code
zoo.animal.count()

#using sum in pandas
print('\n ======using sum ======')
print(zoo.water_need.sum())
#alternative way for above code
zoo.sum()


# Pandas Data Aggregation #3 and #4: min() and max()
print('\n ======using min and max ======')
print(zoo.water_need.min())
print(zoo.water_need.max())

#Averages in Pandas: mean() and median()
print('\n ======using mean and median ======')
print(zoo.water_need.mean())
print(zoo.water_need.median())

#Pandas groupby() function
print('\n ======GROUPBY INACTION======')
print(zoo.groupby('animal').mean())
print('\n ======GROUPBY 2 columns======')
print(zoo.groupby('animal').mean()[['water_need']])

#alternative code as the one above


print(zoo.groupby('animal').mean().water_need)#returns data frame

#Pandas groupby() and count()
zoo.groupby('animal').count()
print(zoo)
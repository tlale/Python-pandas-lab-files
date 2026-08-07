import pandas as pd
import numpy as np
df = pd.read_csv ('./data/employee.csv')
print(df)
# # #columns
# # #print(df[['Name', 'Age']])

# # #rows
# # print(df.loc[1:4])#loc looking for labels,labels are inclusive

# # #iloc works best as list index. its exclusive.
# # print('\n Iloc demo')
# # print(df.iloc[1:4, 0]) #slicing rows and columns.its exclusive of 4

# # #rows and columns
# # print('\n row 4 column 2')
# # print(df.iloc[:4, :2])#uses position in the data table

# # print('\n loc as label demo')
# # #access rows and columns
# # print(df.loc[1:5, 'Name': 'Weight'])#inclusive so 5 

# #working with missing values
# print(df)
# #show missin values
# print(df.isnull())

# #For example Replaces both the Salary and the Age
# df.fillna({'Age':18, "Salary": 25000}, inplace=True)

# #fill missing values

# #df['Age'].fillna(18,implace=True)
# # df = df['Age'].fillna(18)
# # df['Age'] = df['Age'].fillna(18) #create a range of build in random
# # df['Salary'] = df['Salary'].fillna(20000)
# # #df = df.fillna(18)
# # print(df)

# #drop rows with missing values
# df = df.dropna()
# #replace missing values
# df = df.replace('James', 'Replaced')
# df["newCol"] = df["newCol"].replace[False, True]
# df.replace(np.nan, True)
# print(df)
today = pd.to_datetime('2026-07-21')
print(today)

print(pd.date_range('2026-01-01', '2026-01-11'))
print(df)
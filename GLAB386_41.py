import pandas as pd
df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },

)


df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },

)


df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },

)

frames = [df1, df2, df3]
result = pd.concat(frames, ignore_index=True) #resetting the index

#print(frames)
print(result)

#Assigning keys to indexes
print('\n====== Assigning keys to indexes xyz=======')
result = pd.concat(frames, keys=["x", "y", "z"])
print(result)

#select out each chunk by key
print('\n ====selecting chunk by keys or their index(y)=====')
result_y = result.loc[('y')] 
print(result_y)

print('\n ====selecting chunk by keys or their index(x)=====')
result_x = result.loc[('x')] 
print(result_x)

#ignoring the overlapping index
print('\n====ignoring the overlapping index====')
df4 = pd.DataFrame(
    {
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    },
    index=[12, 13, 14, 15],
)
print(df4)
#ignore is set to true 
result = pd.concat([df1, df4], ignore_index=True, sort=False)
print(result)
#concating df1,dg2 and the result table
result = pd.concat([df1, df4], axis=1, sort=False)
print(result)

#example2
#fetching the files to use
realState_df1=pd.read_csv('./data/RealEstate1.csv')
realState_df2=pd.read_csv('./data/RealEstate2.csv')
realState_df3=pd.read_csv('./data/RealEstate3.csv')

#check the files path is correct
# print(realState_df1)
# print(realState_df2)
# print(realState_df3)

#concat the 3 files into one
print('\n concatted results table')
realStateDataFrame = pd.concat([realState_df1,realState_df2,realState_df3], axis=0, ignore_index=False)
print(realStateDataFrame)

# select single column by column index number
#s = df[df.columns[0]]
realStateDataFrame[realStateDataFrame.columns[1]]

# select column to Series
#s = df['colName']
print('\n====== column to series=======')
series = realStateDataFrame['MLS']
print(series)

#df[df["columName"] > condidtion]
print('\n =====series with bedroom more than 3=====')
series = realStateDataFrame[realStateDataFrame['Bedrooms'] >3 ]
print(series)
import pandas as pd

data = {
    'Category': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Value': [10, 15, 20, 25, 30, 35],
    'Fee' :[20000,25000,26000,22000,24000,35000],
    'Duration':['30day','40days','35days','40days','60days','60days'],
    'Discount':[1000,2300,1200,2500,2000,2000]
}
df= pd.DataFrame(data)
print('===========show our table=======:\n',df)

#applying single aggregate Function
total_sum = df['Value'].aggregate('sum')#more dynamic my preffered
print('Total Sum:', total_sum)

#alternative way to perform similar aggregation as above
total_sum2 = df[['Value']].sum()
print("Total Sum:", total_sum2)

# cumulative sum of the differences between the values and the average in the given data
df[['Value']].cumsum()#revist

#calculate the mean of the value column
average_value = df['Value'].aggregate('mean')
print('\nAverage Value code method1:', average_value)

#alternative to the above code
average_value2 = df[['Value']].mean()
print('\nAverage Value method2:', average_value2)

#calculate the maximun value in the value column
max_value = df[['Value']].aggregate('max')
print('Maximum Value:',max_value)

#Altenative to the above code
max_value2 = df[['Value']].max()
print('Maximum Value:',max_value2)

#calculate the total number of value
std_value = df['Value'].aggregate('count')
print('Total count:', std_value)

#Altenative to the above code
std_value2 = df[['Value']].count()
print("Total count:", std_value2)

#apply multiple aggregate functions in pandas
# applying multiple aggregation functions to a single column
result = df[['Fee','Discount']].aggregate('sum')
print(result)

#Alternate

result2 = df[['Fee','Discount']].sum()
print(result2)

#check the group of the aggregated value
# Use DataFrame.group() Function
result_Group = df.groupby('Category')[['Fee','Discount']].aggregate('sum')
print(result_Group)
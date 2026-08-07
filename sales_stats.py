import pandas as pd
trans1_df = pd.read_csv('./data/transactions1.csv')
trans2_df = pd.read_csv('./data/transactions2.csv')

# print(trans1_df)
# print(trans2_df)
#combining 2 data files using concat
combine_trans_df = pd.concat([trans1_df, trans2_df], ignore_index=True)
print(combine_trans_df)

#EDA
print(combine_trans_df)
print(combine_trans_df.info())
print(combine_trans_df.describe())

#groupby
category_group = combine_trans_df.groupby('Category')
store_group = combine_trans_df.groupby('StoreID')
print(category_group)
 #get_group function can only get one group at the time
#print(category_group.get_group('Home').sort_values(['SalesAmount', 'Date'], ascending = [False,True]))
print(store_group.get_group(101).sort_values(['SalesAmount', 'Date'], ascending = [False,True]))


print(category_group.get_group('Electronics'))

#how much each category make group and aggregate 
category_stats= combine_trans_df.groupby('Category')['SalesAmount'].agg(['sum','mean', 'median'])

#rename the columns respectively named as above aggrgation index
category_stats.columns = ['Total Sales', 'Avarage', 'Middle']
print(category_stats)

#Pivot table function
store_stats = combine_trans_df.pivot_table('SalesAmount', 'StoreID', aggfunc=['count','sum'])
print(store_stats)

#cummulativesum

# print(combine_trans_df)
combine_trans_df = combine_trans_df.sort_values(by=['StoreID', 'Date'])
# print(combine_trans_df)

print('\n=================CUMSUM=====================')
combine_trans_df['Cumulative_Sales'] = combine_trans_df.groupby('StoreID')['SalesAmount'].cumsum()
print(combine_trans_df)

print('\n ======================TRANSFORM=============')
combine_trans_df['Total'] = combine_trans_df.groupby('StoreID')['SalesAmount'].transform('sum')
print(combine_trans_df)

print('\n================DIFF sales trends per day============')
combine_trans_df['Trend'] = combine_trans_df.groupby('StoreID')['SalesAmount'].diff()
print(combine_trans_df)
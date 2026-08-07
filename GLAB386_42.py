 #Create Pandas DataFrame
import pandas as pd
left_df = pd.DataFrame({'Courses': ["Spark","PySpark","Python","pandas","Java"],
                    'Fee' : [20000,25000,30000,24000,40000],
                    'Duration':['30day','40days','60days','55days','50days']})

right_df = pd.DataFrame({'Courses': ["Java","PySpark","Python","pandas","Hyperion","html"],
                    'Fee': [20000,25000,30000,24000,40000,4000],
                    'Percentage':['10%','20%','25%','20%','10%','50%']})

print("First DataFrame:\n", left_df)
print("Second DataFrame:\n", right_df)

#merge the data frame without any key
print('\nmerged dataframe')
merged_df = pd.merge(left_df,right_df)
merged_df.shape#check the merged dataframe shape thus num of columns and rows
print(merged_df)

#merged dataFrame besed on single column
print('\n======merged dataframe based on single column=====')
result = pd.merge(left_df, right_df, on="Courses")
print(result)
print("shape After merging the DataFrames:\n", result.shape)
#result.shape #return the number of columns and rows after the merge

#merging multiple columns
# Use pandas.merge() on multiple columns
print('\n======merged dataframe based on multiple column=====')
df_result = pd.merge(left_df,right_df, on=['Courses','Fee'])
print("shape After merging the DataFrames:\n", df_result.shape)

#merging different column name
results = pd.merge(left_df, right_df, how='left', left_on=['Courses','Fee'], right_on = ['Courses','Fee'])
print("shape After merging the DataFrames:\n", results)
print("shape After merging the DataFrames:\n", results.shape)

#checking duplicate keys
left = pd.DataFrame({"A": [1, 2], "B": [1, 2]})

right = pd.DataFrame({"A": [4, 5, 6], "B": [2, 2, 2]})
#one  to many validation
result = pd.merge(left, right, on="B", how="inner", validate="one_to_many")
print(result)

# Create a DataFrame with sales transactions
sales_data = {
    'TransactionID': [1, 2, 3, 4, 5],
    'ProductID': [101, 102, 103, 101, 105],
    'StoreID': [1, 2, 1, 3, 2],
    'Quantity': [5, 3, 2, 4, 1],
    'Amount': [500.00, 300.00, 200.00, 400.00, 150.00]
}

df_sales = pd.DataFrame(sales_data)

# Create a DataFrame with product details
products_data = {
    'ProductID': [101, 102, 103, 104, 105],
    'ProductName': ['Laptop', 'Headphones', 'Smartphone', 'Tablet', 'Monitor'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics']
}
df_products = pd.DataFrame(products_data)
# Merge the DataFrames based on 'ProductID' and 'StoreID' keys
df_combined = pd.merge(df_sales, df_products, on='ProductID', how='left')

# Display the combined DataFrame
print("Combined DataFrame:")
print(df_combined)
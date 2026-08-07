import pandas as pd
from sqlalchemy import create_engine, text

#create angine
#it need url of connection string
#engine = create_engine("mysql+mysqldb://user:password@localhost:3306/databasename")
engine = create_engine("mysql+mysqldb://root:root@localhost:3306/classicmodels")#default port is 3306
#Queries
sql_query_order = """ SELECT orderNumber, productCode,priceEach, orderLineNumber, quantityOrdered FROM orderdetails; """
SQL_Query_product = """ SELECT * FROM products """;  

#open the database connection and query database
with engine.connect() as my_conn:

    my_data = pd.read_sql(text(SQL_Query_product),my_conn)
    print(my_data)

    #printing first 10 columns
    print(my_data.head(10))   

#printing specific columns
    print(my_data[['productCode','productName']].head(10))

# #printing data using the index column 
# print('\n =====use index to show products====')

    products_df = pd.read_sql(text(SQL_Query_product),my_conn, index_col ='productCode')
    print(products_df)

    #perform exploratory Data Analysis
    print('\nBasic Statistics:')
    print(products_df.describe())

#check data type 
   # print('\ndata types within product table:')
   # print(products_df.dtypes())

#find the number of rows and columns
print(products_df.shape)# Get the number of rows and columns
print(products_df.shape[0]) # Get the number of rows only
print(products_df.shape[1]) # Get the number of columns only

#check missing values
print("\nMissing Values:")
print(products_df.isnull().sum())

#grouping and aggregation
grouped_df = products_df.groupby('productLine').agg({'quantityInStock': 'sum', 'buyPrice': 'mean'}).reset_index()
print("\nGrouped Data:")
print(grouped_df)

#user order details table
#find the total amount of each order
orders_prod_df = pd.read_sql(text(sql_query_order),my_conn)
print("Sample of the 'orders' DataFrame:")
print(orders_prod_df.head())
 
orders_prod_df['totalCost'] = orders_prod_df['priceEach'] * orders_prod_df['quantityOrdered']

  	 # Group by 'orderNumber' and sum 'totalCost' for each group
       
grouped_df = orders_prod_df.groupby('orderNumber')['totalCost'].sum().reset_index()
print(grouped_df)


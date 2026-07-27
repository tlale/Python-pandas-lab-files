import pandas as pd
import numpy as np
#pandas transform in action
df = pd.read_csv('./data/sales_transactions.csv')
print(df)

#MERGE 
Order_Total = df.groupby('order')["ext price"].sum()
print(Order_Total)
print('\n======step1B combining data back to original dataframe========')
# # order_total = df.groupby('order')["ext price"].sum().rename("Order_Total").reset_index()
# df_1 = df.merge(Order_Total)
# df_1["Percent_of_Order"] = df_1["ext price"] / df_1["Order_Total"]
# print(df_1)
print('\n======step1B using transform and group by========')
sum_of_orders = df.groupby('order')["ext price"].transform('sum')
print(sum_of_orders)

print('\n======step1C using transform and group by========')
df["Order_Total"] = df.groupby('order')["ext price"].transform('sum')
Order_Total = df["Order_Total"]
print(Order_Total)
#using group by function to transfor data table
df["Percent_of_Order"] = df["ext price"] / df["Order_Total"]
Percent_of_Order = df["Percent_of_Order"]
print(Percent_of_Order)
#alternative of the above lines of code to transform with group by
print('\n======combine transform code into one statement========')
df["Percent_of_Order"] = df["ext price"] / df.groupby('order')["ext price"].transform('sum')
Percent_of_Order = df["Percent_of_Order"]
print(Percent_of_Order)
print(df)
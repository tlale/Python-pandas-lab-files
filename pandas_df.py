# import pandas as pd
# #create empty dataFrame
# df = pd.DataFrame()

# #create new column with some data
# df["SQL"] = [78, 89, 90]

# df["Python"] = [67, 78, 99]
# length = 3
# index = 2
# print(df.loc[0])

# #insert a new row

# df.loc[len(df)] = [78, 79]
# print(df.shape)
# print(df)


# print("#####################################")
# data = { 'apples sales': [3,2,0,1,9,6,3,2,7], 
#         'oranges sales': [0,3,7,2,2,5,8,7,1]   }
# #better view
# #idx = ['2000', '2001', '2002', '2003', '2004','2005', '2006', '2007', '2008']
# #idx = ['2000', '2001', '2002', '2003', '2004','2005', '2006', '2007', '2008']

# idx = pd.RangeIndex(2000,2009)# label the data index based on the year range you labeled

# sales_df = pd.DataFrame(data, index=[idx])
# print(sales_df)
# print(sales_df.shape)
# print(sales_df.dtypes)
# print(type(sales_df["apples sales"]))

# #accessing the index info
# print(sales_df.index)
# print(sales_df.index[0])
# print(sales_df.index[-1])
# print(sales_df.index.values)
# print(sales_df.index.to_list())


# print("==================csv=================")
# employee_df = pd.read_csv('./data/employee.csv')
# #first step to get data set info 
# print(employee_df.info())
# #print(employee_df)

# print("==================json=================")
# cars_df = pd.read_json('./data/cars.json')
# print(cars_df)
# print(cars_df.info())
# print(cars_df.dtypes)

# #print("==================describe=================")
# #print(cars_df.describe(include='all'))

# print("================column attributes=================")

# student_dict = {    'Name': ['Joe', 'Nat', 'Harry'],  
#                 'Age': [20, 21, 19],  
#                 'Marks': [85.10, 77.80, 91.54]}
# student_df = pd.DataFrame(student_dict)
# # Get the column names as a Pandas Index object
# columns_index = student_df.columns
# print("Columns (Index):", columns_index)

# # Get the label of the first column
# first_column = student_df.columns[0]
# print("First Column Name:", first_column)

# # Get the column names as a list
# columns_list = student_df.columns.tolist()
# print("Columns (List):", columns_list)

# #get the data from the columns

# print(student_df['Name']) #single column
# print(student_df[['Name', 'Age', 'Marks']]) #getting data from multiple column

# print(student_df['Age'].value_counts())
# print(cars_df['MPG'].value_counts(ascending=True))

# #turn a series to a list
# print(student_df['Marks'].values.tolist())
# print(student_df.to_string())
# print(cars_df.head(10)) #return the fisrt 10 column
# print(cars_df.tail(10)) #return the last 10 column

# print("+++++++++++++++++++++++Rename Functions+++++++++++++++++++++++")
# technologies = ({'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],''
# 'Fee' :[20000,25000,26000,22000,24000,21000,22000],
# 'Duration':['30day', '40days' ,'35days', '40days', '60days', '50days', '55days']})
# df = pd.DataFrame(technologies)
# print(df.columns)

# # Rename a Single Column 
# df2=df.rename(columns = {'Course':'Course_Name','Fee':'Fee_Semester'})                     
# #df2=df.rename(columns = {'Fee':'Fee_Semester'})
# df2=df.rename(columns= {'Duration':'Duration_PerCourse'})# rename the column from Courses to Courses_Name.
# print(df2.columns)

# df.insert(1, 'Available', False)
# #use assign method to add new columns
# df['Available'] = False
# print(df['Available'])

# df.assign(Available=True)# return a  new data frame back to you
# print(df)
# print(df['Available'].values)

import pandas as pd

# create empty dataframe
df = pd.DataFrame()

# creates a new column with some data
df["SQL"] = [78, 89, 90]
df["Python"] = [67,78,99]

# length = 3
# index = 2
# print(df.loc[0])

# insert a new row
# df.loc[3] = [78, 89]
df.loc[len(df)] = [78,89]

print(df.shape)
print(df)

print('=====================================')
data = {
        'apples sales': [3,2,0,1,9,6,3,2,7],
        'oranges sales': [0,3,7,2,2,5,8,7,1]
    }

# idx = ['2000', '2001', '2002', '2003', '2004','2005', '2006', '2007', '2008']
idx = pd.RangeIndex(2000, 2009)

sales_df = pd.DataFrame(data, index=idx)

print(sales_df)
print(sales_df.shape)
print(sales_df.dtypes)
print(type(sales_df["apples sales"]))

# Index Object
print(sales_df.index)
print(sales_df.index[0])
print(sales_df.index[-1])
print(sales_df.index.values)
print(sales_df.index.to_list())

print('===============CSV File======================')
employee_df = pd.read_csv('./data/employee.csv')
# employee_df = pd.read_csv('./data/employee.csv', index_col=0)

print(employee_df)
print(employee_df.info())

print('===============JSON File======================')

cars_df = pd.read_json('./data/cars.json')


print(cars_df)
print(cars_df.info())

print('===============Describe======================')
print(cars_df.describe())
# print(cars_df.describe(include='all'))

print('===============Column Attribute======================')
# Create DataFrame from a dictionary
student_dict = {
    'Name': ['Joe', 'Nat', 'Harry'],
    'Age': [20, 21, 19],
    'Marks': [85.10, 77.80, 91.54]
}

student_df = pd.DataFrame(student_dict)

# Get the column names as a Pandas Index object
columns_index = student_df.columns
print("Columns (Index):", columns_index)

# Get the label of the first column
first_column = student_df.columns[0]
print("First Column Name:", first_column)

# Get the column names as a list
columns_list = student_df.columns.tolist()
print("Columns (List):", columns_list)

# ============= Access the column data =====================
# select a single column
print(student_df["Name"])

# select multiple column
print(student_df[["Name", "Age"]])


print(student_df["Age"].value_counts())

print(cars_df['MPG'].value_counts(ascending=True))
print(cars_df['MPG'].value_counts())

# turn a series to a list
print(student_df["Marks"].values.tolist())

print(cars_df.head(10))
print(cars_df.tail(10))

print(cars_df.to_string())



print('============= Rename function =====================')

technologies = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
     'Fee' :[20000,25000,26000,22000,24000,21000,22000],
     'Duration':['30day', '40days' ,'35days', '40days', '60days', '50days', '55days']
     })


df = pd.DataFrame(technologies)
print(df.columns)

# Rename a Single Column
df2 = df.rename(columns = {'Courses':'Courses_Name', "Fee": "Course_Fee"}) # rename the column from Courses to Courses_Name.

print(df2.columns)

print("================================")

df["Available"] = False
print(df["Available"])

# df.insert(1, 'Available', False)
df = df.assign(Available=True)
print(df)


print(df["Available"])
# print(df["Available"].values)

print(df)

# ================== Sort Values =========================
print(df.sort_values("Courses"))
print(df.sort_values(by=["Courses"]))
print(df.sort_values(by=["Courses", "Fee"]))



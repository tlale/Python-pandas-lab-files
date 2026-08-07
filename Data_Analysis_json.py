import pandas as pd
# Read JSON file
df_cars = pd.read_json('cars.json')
print(df_cars.dtypes)
df_cars.describe()

#dataFrame count
df_cars.count()
df_cars.info()

#select few columns
df_cars.head(2) #first 2 column

df_cars.tail(2) #last 2 column
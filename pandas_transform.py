
import pandas as pd
# Loading the datasets
store_info_df = pd.read_csv('./data/store_info.csv')
trans1_df = pd.read_csv('./data/transactions1.csv')
trans2_df = pd.read_csv('./data/transactions2.csv')
# print(store_info_df)
# print(trans1_df)
# print(trans2_df)
# Combine the transactions
combine_trans_df = pd.concat([trans1_df, trans2_df], ignore_index=True)
print(combine_trans_df)

# Merge the store info with the transactions
merged_trans_df = pd.merge(combine_trans_df, store_info_df, on="StoreID")
print(merged_trans_df)

trans1_df = trans1_df.set_index('StoreID')
trans2_df = trans2_df.set_index('StoreID')


trans2_df
import pandas as pd
import numpy as np
import lib.load as load
import data_cleaning as dc
import lib.df_info as i
import lib.func as f

def print_section(w):
    print('\n-------------------------------------')
    print(w)
    print('-------------------------------------\n ')

df = load.load_data()
df_transactions = df[0]
#df_new_cust_list = df[1]
df_demographic = df[2]
df_address = df[3]

try:
    df_demographic = dc.clean_demographic(df_demographic).reset_index(drop=True)
    df_address = dc.clean_address(df_address).reset_index(drop=True)
    df_transactions = dc.clean_transactions(df_transactions).reset_index(drop=True)
    print("Data cleaning successful.")
except Exception as e:
    print("An error occurred during data cleaning:", e)

print_section('TRANSACTION WITHOUT CLEANING')
i.df_info.columns_na(df[0])

print_section('TRANSACTION AFTER CLEANING')
i.df_info.columns_na(df_transactions)

print_section('MERGE DFF CLEANING')
dff = f.merge_df_inner(df_demographic,df_transactions,df_address)
i.df_info.columns_na(dff)
print('\n')
f.percentage_cleaning_tr(dff,df)
print('\n')

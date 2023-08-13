# %load main.py
   
import pandas as pd
import numpy as np
import lib.load as load
import data_cleaning as dc
import lib.df_info as i
import lib.func as f

df = load.load_data()
df_transactions = df[0]
#df_new_cust_list = df[1]
df_demographic = df[2]
df_address = df[3]

try:
    df_transactions = dc.clean_transactions(df_transactions).reset_index(drop=True)
    print('Success: transactions')
except Exception as e:
    print(f'Error transactions: {e}')

try:
    df_demographic = dc.clean_demographic(df_demographic).reset_index(drop=True)
    print('Success: demographic')
except Exception as e:
    print(f'Error demographic: {e}')

try:
    df_address = dc.clean_address(df_address).reset_index(drop=True)
    print('Success: address')
except Exception as e:
    print(f'Error address: {e}')
    
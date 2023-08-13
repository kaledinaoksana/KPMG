   
import pandas as pd
import numpy as np
import lib.load as load
import data_cleaning as dc
import lib.df_info as i
import lib.func as f
import os
import settings as s

df = load.load_data()
df_transactions = df[0]
#df_new_cust_list = df[1]
df_demographic = df[2]
df_address = df[3]

try:
    df_demographic = dc.clean_demographic(df_demographic).reset_index(drop=True)
    df_address = dc.clean_address(df_address).reset_index(drop=True)
    df_transactions = dc.clean_transactions(df_transactions).reset_index(drop=True)
except Exception:
    print('ERROR.')
    
path = os.getcwd() + s.file_dem 
    
if not os.path.isfile(path):
    df.to_csv(path, header = 'column_names')
else:
    df.to_csv(path, mode = 'a', header = False)

import pandas as pd
import lib.func as f
import os
import settings as s

def load_data():
    path = os.getcwd() + s.source
    # print(path)
    # df_transactions = pd.read_excel(path,sheet_name=1,parse_dates=['transaction_date', 'product_first_sold_date'],date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d'))
    # df_new_cust_list = pd.read_excel(path, sheet_name=2,parse_dates=['DOB'], date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d'))
    # df_demographic = pd.read_excel(path,sheet_name=3,parse_dates=['DOB'], date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d'))
    # df_address = pd.read_excel(path, sheet_name=4)
    # Read the Excel sheets
    df_transactions = pd.read_excel(path, sheet_name=1, parse_dates=['transaction_date', 'product_first_sold_date'], date_format='%Y-%m-%d')
    df_new_cust_list = pd.read_excel(path, sheet_name=2, parse_dates=['DOB'], date_format='%Y-%m-%d')
    df_demographic = pd.read_excel(path, sheet_name=3, parse_dates=['DOB'], date_format='%Y-%m-%d')
    df_address = pd.read_excel(path, sheet_name=4)

    dff = [df_transactions,df_new_cust_list,df_demographic,df_address]
    dff = f.change_index(dff)
    return dff

# TEST

df = load_data()
dff = df[0]
print(dff)
    
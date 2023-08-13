import pandas as pd
import lib.load as load
import os
import settings as s


def clean_demographic(df):
    # drop columns
    df = df.drop(columns="default")
    # DOB
    #df = df.rename(columns={"DOB": "date_of_birth"})
    # 'gender'
    df['gender'] = df['gender'].str.replace('Female','F')
    df['gender'] = df['gender'].str.replace('Femal','F')
    df['gender'] = df['gender'].str.replace('Male','M')
    df['gender'] = df['gender'].str.replace('F','Female')
    df['gender'] = df['gender'].str.replace('M','Male')
    # 'deceased_indicator'
    df['deceased_indicator'] = df['deceased_indicator'].str.replace('N','No')
    df['deceased_indicator'] = df['deceased_indicator'].str.replace('Y','Yes')
    # create age 
    df['DOB'] = pd.to_datetime(df['DOB'], format='mixed', errors='coerce')
    df['age'] = ((pd.Timestamp('today').normalize() - df['DOB']).dt.days // 365)

    # age between < 90
    df = df.drop(df[df['age'] > 90].index)
    # df = df.drop(df[df['age'].isnull()].index)
    # indexes before
    # df = df.drop(df[df['customer_id'] < 3501 ].index)
    df = df.rename(columns={"past_3_years_bike_related_purchases": "past_3y_brp"})
    path = os.getcwd() + s.file_dem
    df.to_csv(path, index = False)
    return df

def clean_address(df):
    df['state'] = df['state'].str.replace('Victoria','VIC')
    df['state'] = df['state'].str.replace('New South Wales','NSW')
    # df = df.drop(df[df['customer_id'] < 3501 ].index)
    path = os.getcwd() + s.file_address
    df.to_csv(path, index = False)
    return df

def clean_transactions(df):
    #delete rows with null (555 rows)
    #df = df.drop(df[df['customer_id'] < 3501 ].index)
    df = df.loc[(df['brand'].notnull())]
    df = df.loc[df['online_order'].isnull(), 'online_order'] = 0.0
    path = os.getcwd() + s.file_trans
    df.to_csv(path, index = False)
    return df

#TEST

# df = load.load_data()
# df_transactions = df[0]
# df_new_cust_list = df[1]
# df_demographic = df[2]
# df_address = df[3]

# try:
#     df_demographic = clean_demographic(df_demographic)
#     df_address = clean_address(df_address)
#     df_transactions = clean_transactions(df_transactions)
# except Exception:
#     print('This function has already used or you have ERROR.')
    
# print(df_demographic.reset_index())





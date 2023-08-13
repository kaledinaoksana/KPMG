

def change_index(df):
        for dff in df:
            dff.index = dff.index + 1
        return df
    
# MERGE
def merge_df_inner(d_d,d_t,d_a):
    df = d_d.merge(d_a, how = 'inner', on = 'customer_id') 
    df = df.merge(d_t, how = 'inner', on = 'customer_id') 
    return df

def revenue(df):
    return ((df['list_price'] - df['standard_cost']).sum())

def percentage(x,y):
    return 100*(x-y)/x

def percentage_cleaning_tr(dff,df):
    per_revenue = percentage(revenue(df[0]),revenue(dff))
    per_len = percentage(len(df[0]), len(dff))
    #how changed transaction len and revenue after cleaning dataset
    print('percent revenue = ',per_revenue,', percent len = ',per_len)
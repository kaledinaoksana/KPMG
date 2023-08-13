

import pandas as pd
import numpy as np
import lib.func as f 

class df_info:
    
    def null_count(df):
        return df.isnull().sum()
    
    def all_cells_na(df):
        missing_values_count = df.isnull().sum()
        total_cells = np.product(df.shape)
        total_missing = missing_values_count.sum()
        percent_missing = (total_missing/total_cells) * 100
        return total_cells,total_missing, percent_missing.round(2)
    
    def rows_na(df):
        # dropna - rows
        rows_with_na_dropped = df.dropna()
        a = df.shape[0] - rows_with_na_dropped.shape[0]
        per_cent = a/df.shape[0]*100
        print("Rows in original dataset: %d" % df.shape[0])
        print("Rows with na's dropped: %d " % rows_with_na_dropped.shape[0])
        print("Rows with na: %d "% a)
        print("Percent of rows with na: %d"% per_cent + '%')
        return
        
    def columns_na(df):
        # dropna - columns
        columns_with_na_dropped = df.dropna(axis=1)
        a = df.shape[1] - columns_with_na_dropped.shape[1]
        per_cent = a/df.shape[1]*100.00
        print("Columns in original dataset: %d " % df.shape[1])
        print("Columns with na's dropped: %d " % columns_with_na_dropped.shape[1])
        print("Columns with na: %d "% a )
        print("Percent of columns with na: %d"% per_cent + '%\n')
        nulls = df.isnull().sum().to_frame()
        for index, row in nulls.iterrows():
            if (row[0] != 0):
                print(row[0], index)
        return
        
    def column_names(df):
        for col in df.columns:
            print(col)
        return
        
    def unique(df,column):
        return pd.unique(df[column].values.ravel())
    
    def na_in_column(df, column):
        df = df.loc[df[column].isnull()].reset_index()
        f.change_index(df)
        return df
     
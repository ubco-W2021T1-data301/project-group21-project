import pandas as pd
import numpy as np
import pandas as pd

def load_and_process(url_or_path_to_csv_file):
    df1 = (
        pd.read_csv(url_or_path_to_csv_file, sep=",", header=0)     
        )
    
    df2 = (
    df1
        .assign(
            RSI = lambda x: 100 - 
            (100/(1+((((x['Close'].diff()).clip(lower=0)).ewm(com=13, adjust=False).mean())/
                     ((-1*(x['Close'].diff()).clip(upper=0)).ewm(com=13, adjust=False).mean())))),
            MACD = lambda x: (x['Close'].ewm(span=12, adjust=False).mean()) - (x['Close'].ewm(span=26, adjust=False).mean()),
            Signal_line = lambda x: ((x['MACD']).ewm(span=9, adjust=False).mean())
    )
        .drop('OpenInt', axis=1)

    )
    
    df2.dropna(inplace = True, axis = 0)
    df2['Date'] = pd.to_datetime(df2['Date'])
    df2.index = df2["Date"]
    del df2['Date']
       
    return df2
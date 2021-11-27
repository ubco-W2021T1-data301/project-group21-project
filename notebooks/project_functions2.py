import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns #Understanding my variables

def load_and_process(url_or_path_to_csv_file):
    df = (pd.read_csv(url_or_path_to_csv_file, sep=",", header=0)
    .assign(
            RSI = lambda x: 100 - (100/(1+((((x['Close'].diff()).clip(lower=0)).ewm(com=13, adjust=False).mean())/((-1*(x['Close'].diff()).clip(upper=0)).ewm(com=13, adjust=False).mean())))),
            MACD = lambda x: (x['Close'].ewm(span=12, adjust=False).mean()) - (x['Close'].ewm(span=26, adjust=False).mean()),
            Signal_line = x['MACD'].ewm(span=9, adjust=False).mean()
    )
    .drop(['OpenInt'], axis=1))
    
    df['Date'] = pd.to_datetime(df['Date'])
    df = [df['Volume'].between(1, 1.0e+15)]
    df.index = df["Date"]

          
    return df
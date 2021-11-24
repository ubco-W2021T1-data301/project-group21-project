import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
plt.show()
plt.rc("axes.spines", top=False, right=False)

def load_and_process(url_or_path_to_csv_file, start, end):
    # Method Chain 1 - load data
    df = pd.read_csv(url_or_path_to_csv_file, sep=",", header=0, names=["Date", "Open", "High", "Low", "Close", "Volume", "OpenInt"])
    
    # Method Chain 2 - set time series index
    df['Date'] = df['Date'].apply(pd.to_datetime)
    df.set_index('Date', inplace = True)
    df.drop(columns=['OpenInt'], inplace=True)
    
    # Method Chain 4 - Plot Monthly Mean Close Price for Security for start date till end date
    start_date = start
    end_date = end
    df[(start_date <= df.index) & (df.index <= end_date)]['Close'].resample('M').mean().plot(kind ='bar', grid=False, figsize = (16,8))
    plt.title(f'Monthly Mean Close Price for Security between {start} and {end}')
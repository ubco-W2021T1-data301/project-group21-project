import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os, random
plt.style.use('fivethirtyeight')
plt.show()
plt.rc("axes.spines", top=False, right=False)


def load_and_process(url_or_path_to_csv_file, start, end):
    
    '''
    load_and_process takes a random filename, chosen among the files of the given path.
    It also indicates a start and end date denoted as 'YYYY-MM-DD', processes the dataset and returns a plot and a table.
    '''
    
    n=0
    random.seed();
    for root, dirs, files in os.walk(url_or_path_to_csv_file):
      for name in files:
        n += 1
        if random.uniform(0, n) < 1:
            rfile=os.path.join(root, name)
    print(rfile)
    
    # Method Chain 1 - load data
    df = pd.read_csv(rfile, sep=",", header=0, names=["Date", "Open", "High", "Low", "Close", "Volume", "OpenInt"])
    
    # Method Chain 2 - set time series index
    df['Date'] = df['Date'].apply(pd.to_datetime)
    df.set_index('Date', inplace = True)
    df.drop(columns=['OpenInt'], inplace=True)
    
    # Method Chain 3 - Plot Monthly Mean Close Price for Security
    df['Close'].resample('M').mean().plot(kind='bar',grid=False, figsize = (16,8))
    plt.title('Monthly Mean Close Price for Security')
    
    # Method Chain 4 - Plot Monthly Mean Close Price for Security for 2015 - 2017
    start_date = start
    end_date = end
    df[(start_date <= df.index) & (df.index <= end_date)]['Close'].resample('M').mean().plot(kind ='bar', grid=False, figsize = (16,8))
    plt.title(f'Monthly Mean Close Price for Security between {start} and {end}')
    df.head()
    
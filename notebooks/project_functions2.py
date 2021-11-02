import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns #Understanding my variables

def load_and_process(url_or_path_to_csv_file):
    df = (pd.read_csv(url_or_path_to_csv_file, sep=",", header=0).drop(['OpenInt'], axis=1))
    df['Date'] = pd.to_datetime(df['Date'])
    df = [df['Volume'].between(1, 1.0e+15)]

          
    return df
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns #Understanding my variables
from IPython.display import display
import mplfinance as fplt

def load_and_process(url_or_path_to_csv_file):
	ddf = (pd.read_csv(url_or_path_to_csv_file, sep=",", header=0)
	.assign(
		DailyReturn = lambda x: x['Close'].pct_change(),
		VolumeChange = lambda x: x['Volume'].pct_change()
	)
	.drop('OpenInt', 
	axis=1))
	
	
	ddf.dropna(inplace = True, axis = 0)
	ddf['Date'] = pd.to_datetime(ddf['Date'])
	ddf.index = ddf["Date"]
	ddf = ddf.loc['1995-01-01':'2002-10-01']

	return ddf
import pandas as pd
from pandas import Series,DataFrame
def quarter_volume():
	data = pd.read_csv('/home/shiyanlou/Code/apple.csv',header=0)
	df = data[['Date','Volume']]
	df.Date = pd.to_datetime(df.Date)
	volume = df.resample('Q',on='Date').sum().sort_values(by='Volume',ascending=False).iloc[1].Volume
	return volume

	

if __name__ == '__main__':
	vol = quarter_volume()
	print(vol)


	
	

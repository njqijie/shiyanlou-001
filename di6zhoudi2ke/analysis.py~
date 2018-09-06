import json
import pandas as pd
from pandas import Series,DataFrame
def analysis(file,user_id):
	times = 0
	minutes = 0
	with open(file,'r') as json_file:
		data = pd.read_json(json_file)
		df = DataFrame(data)
		df = df[df['user_id']==user_id]
		times = df['user_id'].count()
		minutes = df['minutes'].sum()
		return times,minutes
			
	
if __name__ == '__main__':
	file = '/home/shiyanlou/Code/user_study.json'
	t,m = analysis(file,5348)
	print(t,m) 

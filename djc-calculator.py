#!/usr/bin/env python3
import sys
import csv
import time
from multiprocessing import Process,Queue

class Args():
	def __init__(self):
		self.args = sys.argv[1:]
		index = self.args.index('-c')
		self.configfile = self.args[index+1]
		index = self.args.index('-d')
		self.userfile = self.args[index+1]
		index = self.args.index('-o')
		self.gongzifile = self.args[index+1]
			


class Config(object):
	def __init__(self):
		self.config = self._read_config()
	def _read_config(self):
		d = {'s':0}
		with open(args1.configfile) as f1:
			for line in f1.readlines():
				m = line.split('=')
				a,b = m[0].strip(),m[1].strip()
				if a == 'JiShuL' or a == 'JiShuH':
					d[a] = float(b)
				else:
					d['s'] += float(b)
				
		return d


def f2(q2,q1):
	for a,b in q1.get():
		salary = int(b)
		shebao = salary * config['s']
		if salary < config['JiShuL']:
			shebao = config['JiShuL'] * config['s']
		if salary >config['JiShuH']:
			shebao = config['JiShuH'] * config['s']
		m = salary - shebao -3500
		if m <=0:
			shui = 0
		elif m <=1500:
			shui = m * 0.03
		elif m <= 4500:
			shui = m*0.1-105
		elif m <= 9000:
			shui = m*0.2-555
		elif m <=35000:
			shui = m*0.25-1005
		elif m <=55000:
			shui = m* 0.3-2755
		elif m <=80000:
			shui = m*0.35-5505
		else:
			shui = m*0.45-13505
		shuihou = salary - shebao - shui
		
		
		newdata1 = [a,salary,format(shebao,'.2f'),format(shui,'.2f'),format(shuihou,'.2f')]
		newdata.append(newdata1)
		time.sleep(0.01)
	q2.put(newdata)
	#print(newdata)

def f1(q1):
	#def __init__(self):
	with open(args1.userfile) as f:
		data = list(csv.reader(f))
	q1.put(data)


#data = Data().value

def f3(q2):
	#print(dayinwo)
	with open(args1.gongzifile,'w') as f:
		for i in q2.get():
			#print(q2)
			csv.writer(f).writerow(i)
		#for a,b in data:
		
		#x = calc_for_all_userdata(b)
		#x.insert(0,a)
		#writer = csv.writer(f)
		#writer.writerow(x)
def main():
	 Process(target=f1 ,args=(queue1,)).start()	
	 Process(target=f2 ,args=(queue2,queue1)).start()
	 Process(target =f3,args=(queue2,)).start()
	
if __name__=='__main__':
	
	queue1 = Queue()
	queue2 = Queue()
	args1 = Args()
	config = Config().config
	newdata = []
	main()

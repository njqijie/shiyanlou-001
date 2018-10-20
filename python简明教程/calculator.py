#!/usr/bin/env python3
import sys
import csv

class Args():
	def __init__(self):
		self.args = sys.argv[1:]
		index = self.args.index('-c')
		self.configfile = self.args[index+1]
		index = self.args.index('-d')
		self.userfile = self.args[index+1]
		index = self.args.index('-o')
		self.gongzifile = self.args[index+1]
			
args1 = Args()

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

config = Config().config

def calc_for_all_userdata(salary):
	salary = int(salary)
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
		
		
	return [salary,format(shebao,'.2f'),format(shui,'.2f'),format(shuihou,'.2f')]

class Data:
	def __init__(self):
		with open(args1.userfile) as f:
			l = list(csv.reader(f))
		self.value = l

data = Data().value

with open(args1.gongzifile,'w') as f:
	for a,b in data:
		
		x = calc_for_all_userdata(b)
		x.insert(0,a)
		writer = csv.writer(f)
		writer.writerow(x)		



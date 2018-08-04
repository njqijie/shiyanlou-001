#!/usr/bin/env python3
import sys
import csv

class Args():
	def __init__(self):
		
		self.args = sys.argv[1:]
		#print(self.args)
		index = self.args.index('-c')
		self.configfile = self.args[index+1]
		#print(self.configfile)
		index = self.args.index('-d')
		self.userfile = self.args[index+1]
		index = self.args.index('-o')
		self.gongzifile = self.args[index+1]
		print(self.gongzifile)
		
		
			
args1 = Args()



class Config(object):
	def __init__(self):
		#print(8888)
		self.config = self._read_config()
	def _read_config(self):
		d = {'s':0}
		with open(args1.configfile) as f1:
			
			for line in f1.readlines():
				m = line.split('=')
				print(m)
				a,b = m[0].strip(),m[1].strip()
				
				if a == 'JiShuL' or a == 'JiShuH':
					d[a] = float(b)
				else:
					d['s'] += float(b)
				
		return d
class IncomeTaxCalculator(object):
	def calc_for_all_userdata(self):
		salary = int(salary)
		shebao = salary * config['s']
		if salary < ('JiShuL'):
			shebao = config['JiShuL'] * config['s']
		if salary >('JiShul'):
			shebao = config['JiShuL'] * config['s']
		m = salary - shebao -3500
		
config = Config().config


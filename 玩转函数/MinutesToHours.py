#!/usr/bin/env python3
import sys
for str0 in sys.argv:
	b = str0
a  =int(b)

try:
	
	
	if a >= 60:
		h = int(a/60)
		m = a%60
		print("{} H, {} M".format(h,m))
	elif a >=0:
		h = 0
		m = a%60
		print("{} H, {} M".format(h,m))
	elif a < 0:
		raise ValueError
except ValueError:
	print("ValueError:  Input number cannot be negative")
	


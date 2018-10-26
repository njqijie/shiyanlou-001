#!/usr/bin/env python3
file = open("/home/shiyanlou/Code/String.txt")
s = []
for i in file.read():
	if i.isdigit():
		s.append(i)
z = ''.join(s)
print("%s"%(z))

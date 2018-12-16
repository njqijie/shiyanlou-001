#!usr/bin/env python3
import sys
try:
	for arg in sys.argv[1:]:
		a = int((arg.split(':'))[0])
		b = int((arg.split(':'))[1])

		gxshbx = b * 0.165
		ynsds = b -gxshbx-3500

		if ynsds <= 0:
			gz = b - gxshbx 
			print("{}:{:.2f}".format(a,gz))
		elif  0 < ynsds <= 1500:
			gz  = b *0.835 - (ynsds*0.03)
			print("{}:{:.2f}".format(a,gz))
		elif  1500 <ynsds <=4500:
			gz = b*0.835 - (ynsds*0.1 -105)
			#print("gz: ",gz)
			#print("gz = b*0.835 - (ynsds*0.1 -105) :",( b*0.835 - ynsds*0.1 -105))
			print("{}:{:.2f}".format(a,gz))
		elif 4500 <ynsds <=9000:
			gz = b * 0.835 - (ynsds*0.2 -555)
			print("b *0.835 - (ynsds*0.25 -1005): ",b *0.835 - ynsds*0.25 -1005)
			print("{}:{:.2f}".format(a,gz))

		elif 9000 < ynsds <=35000:
			gz = b *0.835 - (ynsds*0.25 -1005)
			
			print("{}:{:.2f}".format(a,gz))

		elif 35000 < ynsds <=55000:
			gz = b -gxshbx - (ynsds * 0.3 -2755)
	
		elif 55000 <ynsds <= 80000:
			gz = b *0.835 -(ynsds * 0.35 -5505)
			print("{}:{:.2f}".format(a,gz))
		else:
			gz = b *0.835 -(ynsds *0.45-13505)	
			print("{}:{:.2f}".format(a,gz))

except ValueError:
	print("Parameter Error")


	 


	

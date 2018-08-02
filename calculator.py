#!/usr/bin/env python3
import sys
#try:
	#for arg in sys.argv[1:]:
		#_income_=arg.split(':')
		#_income_[1]=int(_income_[1])
		
		#tax_income(*_income_)
		
#except:
	#print('erro')	
def tax_income(*income):
	


	
	
	taxincome=income[1]-income[1]*0.165-3500
	if taxincome<0:
		tax=0
	elif taxincome<=1500:
		tax=taxincome*0.03
	elif taxincome<=4500:
		tax=taxincome*0.1-105
	elif taxincome<=9000:
		tax=taxincome*0.2-555
	elif taxincome<=35000:
		tax=taxincome*0.25-1005
	elif taxincome<=55000:
		tax=taxincome*0.3-2755
	elif taxincome<=80000:
		tax=taxincome*0.35-5505
	else:
		tax=taxincome*0.45-13505
	
	print('{}:{:.2f}'.format(income[0],income[1]*(1-0.165)-tax))

try:
	for arg in sys.argv[1:]:
		_income_=arg.split(':')
		_income_[1]=int(_income_[1])
		tax_income(*_income_)
except:
	print("Parameter Error")


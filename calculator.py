#!usr/bin/env python3
import sys
try:
	income=int(sys.argv[1])
except:
	print('erro')	
taxincome=income-3500
if taxincome<=1500:
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
print('{:.2f}'.format(tax))


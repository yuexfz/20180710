#!/usr/bin/env python3
import sys
def pp():
	print("dfsf")
class cfg:
	
	def __init__(self,argv):
		
		with open(argv,'r') as file:
			_cfg=[]
			for line in file:
				try:
					_line=(line.split('='))
					_cfg.append(float(_line[1].strip()))
				except:
					print('erro2')
					exit()
			self._JiShuL=_cfg[0]
			self._JiShuH=_cfg[1]
			self._YangLao=_cfg[2]
			self._YiLiao=_cfg[3]
			self._ShiYe=_cfg[4]
			self._GongShang=_cfg[5]
			self._ShengYu=_cfg[6]
			self._GongJiJin=_cfg[7]
			self._SheBao=_cfg[2]+_cfg[3]+_cfg[4]+_cfg[5]+_cfg[6]+_cfg[7]
			
class user(cfg):
	def __init__(self,argv,argv1,argv2):
		
		cfg.__init__(self,argv)
		with open(argv1,'r') as file1:
			with open(argv2,'w') as file2:
				for line in file1:
					try:
						_line=(line.split(','))
					except:
						print('erro3')
						exit()
					file2.write(_line[0])
					file2.write(',')
					file2.write(_line[1].strip())
					file2.write(',')
					if float(_line[1])<=self._JiShuL:
						SheBaoF=self._JiShuL*self._SheBao	
						if float(_line[1])<SheBaoF:
							SheBaoF=0
					elif float(_line[1])<self._JiShuH:
						SheBaoF=float(_line[1])*self._SheBao
						
					else:
						SheBaoF=self._JiShuH*self._SheBao
					file2.write('{:.2f}'.format(SheBaoF))
					file2.write(',')
					_tax=self.tax(float(_line[1])-SheBaoF)
					file2.write('{:.2f}'.format(_tax))
					file2.write(',')
					file2.write('{:.2f}'.format(float(_line[1])-SheBaoF-_tax))
					file2.write('\n')
					
				
	def tax(self,taxincome):
		taxincome=taxincome-3500
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
	
		return tax





if __name__=='__main__':
	try:
		for arg in sys.argv:
				
			if arg=='-c':
				_index=sys.argv.index('-c')
				argc=sys.argv[_index+1]
			elif arg=='-d':
				_index=sys.argv.index('-d')
				argd=sys.argv[_index+1]
					
			elif arg=='-o':
				_index=sys.argv.index('-o')
				argo=sys.argv[_index+1]
				
		user(argc,argd,argo)
	except:
		print('erro')
		exit()
	
				


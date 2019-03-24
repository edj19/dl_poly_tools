import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import random


def distribution(vx,vy,vz,A,Ek):
	v2 = vx**2+vy**2+vz**2
	Ek0 = 0.5*A*v2/1000
	vx = np.sqrt(vx**2*(Ek/Ek0))
	vy = np.sqrt(vy**2*(Ek/Ek0))
	vz = np.sqrt(vz**2*(Ek/Ek0))
	return vx,vy,vz
def main():
	# Basic parameters in calculations
	m_c = 1.99E-19
	A1 = 15.99
	A2 = 47.87
	M1 = m_c*A1/12
	M2 = m_c*A2/12
	q = 1.6E-19
	Tempe = []
	lists = [1,2,3] # to sample the velocity
	delta_v = 0.5
	timestep = []
	Eatom = []
	step = 0
	Ek = 5.0
	with open("CONFIG",'r') as f:
		f.readline()
		lcfg0,imcn0,*arg = f.readline().split()
		cel = np.zeros(9)
		print(lcfg0,imcn0)
		number = 6000
		E_s = 0.0
		rx,ry,rz = np.zeros(number+1),np.zeros(number+1),np.zeros(number+1)
		vx,vy,vz = np.zeros(number+1),np.zeros(number+1),np.zeros(number+1)
		fx,fy,fz = np.zeros(number+1),np.zeros(number+1),np.zeros(number+1)
		if(imcn0 !=0):
			cel[0],cel[1],cel[2] = f.readline().split()
			cel[3],cel[4],cel[5] = f.readline().split()
			cel[6],cel[7],cel[8] = f.readline().split()
		for i in range(1,number+1):
			name,k = f.readline().split()
			rx[i],ry[i],rz[i]=f.readline().split()
			if(int(lcfg0) !=0):
				vx[i],vy[i],vz[i] = f.readline().split()
			else:
				continue
			if(int(lcfg0) !=1):
				fx[i],fy[i],fz[i] = f.readline().split()
			else:
				continue
			r = np.sqrt((rx[i]-22.97)**2+(ry[i]-22.97)**2+(rz[i]-22.97)**2)
			k_b = 1.880605E-23
			v2 = (vx[i])**2+(vy[i])**2+(vz[i])**2
			if(r<12):
				print(name,k)
				if (name == 'Ti'):
					vx[i],vy[i],vz[i]=distribution(vx[i],vy[i],vz[i],A2,Ek)
				else:
					vx[i],vy[i],vz[i]=distribution(vx[i],vy[i],vz[i],A1,Ek)
				# sampl = random.sample(lists,1)
				# if sampl[0] ==1:
				# 	vx[i]=np.sqrt(2*delta_v+vx[i]**2)
				# elif sampl[0]==2:
				# 	vy[i]=np.sqrt(2*delta_v+vy[i]**2)
				# else:
				# 	vz[i]=np.sqrt(2*delta_v+vz[i]**2)
			if (name=='Ti'):
				E_i = 0.5*A2*v2
				E_eV = E_i*m_c/(12*q)
				step = step+1
				timestep.append(step)
				Eatom.append(E_i/1000)
			else:
				E_i = 0.5*A1*v2
			E_s = E_s+E_i
		T = E_s/((number-1)*0.831451*1.5)  #system temperature in Kelvin
		print(T)
		plt.plot(timestep,Eatom,'b')
		plt.show()


	fout = open("CONFIG_new",'w')
	fout.write("TiO2 structure file system"+"\n")
	fout.write(str(0).rjust(10)+str(2).rjust(10)+str(number).rjust(10)+"\n")
	D = 35.0 # sidelength of simulation cubic box
	fout.write(str(cel[0]).rjust(20)+("%.8f" %0.00).rjust(20)+("%.8f" %0.00).rjust(20)+"\n")  
	fout.write(("%.8f" %0.00).rjust(20)+str(cel[4]).rjust(20)+("%.8f" %0.00).rjust(20)+"\n")
	fout.write(("%.8f" %0.00).rjust(20)+("%.8f" %0.00).rjust(20)+str(cel[8]).rjust(20)+"\n")
	for n in range(1,int(number/3)+1):
		for i in range(1,4):
			if (i==1):
				fout.write("Ti".ljust(8)+str(i+3*(n-1)).rjust(10)+"\n")
				fout.write(("%.8f" %rx[i]).rjust(20)+("%.8f" %ry[i]).rjust(20)+("%.9f" %rz[i]).rjust(20)+"\n")
				fout.write(("%.8f" %vx[i]).rjust(20)+("%.8f" %vy[i]).rjust(20)+("%.9f" %vz[i]).rjust(20)+"\n")
				fout.write(("%.8f" %fx[i]).rjust(20)+("%.8f" %fy[i]).rjust(20)+("%.9f" %fz[i]).rjust(20)+"\n")
			else:
				fout.write("O".ljust(8)+str(i+3*(n-1)).rjust(10)+"\n")
				fout.write(("%.8f" %rx[i]).rjust(20)+("%.8f" %ry[i]).rjust(20)+("%.9f" %rz[i]).rjust(20)+"\n")
				fout.write(("%.8f" %vx[i]).rjust(20)+("%.8f" %vy[i]).rjust(20)+("%.9f" %vz[i]).rjust(20)+"\n")
				fout.write(("%.8f" %fx[i]).rjust(20)+("%.8f" %fy[i]).rjust(20)+("%.9f" %fz[i]).rjust(20)+"\n")

	fout.close()

if __name__ == '__main__':
	main()





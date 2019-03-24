import numpy as np
import matplotlib.pylab as plt

def DFP(Ek,Ed,alpha,beta):
	if Ek<=Ed:
		Vdfp = 0
	else:
		Vdfp = (Ek**alpha-Ed**alpha)/beta
	return Vdfp

def main():
	Ed1 = 19.4
	alpha1 = 0.692
	beta1 = 62.8
	Ed2 = 69.1
	alpha2 = 0.652
	beta2 = 28.6
	energy=[]
	Dfpvalue1,Dfpvalue2=[],[]
	with open('threshold.txt','w') as f:
		for i in range(20,800):
			t1 = DFP(i,Ed1,alpha1,beta1)
			t2 = DFP(i,Ed2,alpha2,beta2)
			energy.append(i)
			Dfpvalue1.append(t1)
			Dfpvalue2.append(t2)
			f.write("%3d %.2f \n" %(i,t2))
	x0 = 469
	y0 = 1.0
	x1 = 336
	y1 = 1.0
	plt.grid(True)
	plt.axis([0,800,0,2.0])
	plt.scatter(x0,y0,color='black')
	plt.scatter(x1,y1,color='black')
	plt.plot([x0,x0],[0,y0],'r--')
	plt.plot([x1,x1],[0,y1],'r--')
	plt.text(x0,y0,str((x0,y0)),ha='left')
	plt.text(x1,y1,str((x1,y1)),ha='right')
	plt.xlabel('PKA energy(eV)')
	plt.ylabel('Defect formation probability')

	plt.plot(energy,Dfpvalue1,color='g',lw=2.0,label='O PKA')
	plt.plot(energy,Dfpvalue2,color='b',lw=2.0,label='Ti PKA')
	plt.legend(loc='upper left')
	plt.show()


if __name__ == '__main__':
	main()
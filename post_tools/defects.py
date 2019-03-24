import numpy as np
import matplotlib.pylab as plt

f = open('DEFECTS')
defects = []
timestep = []
t = 0



for each_line in f:
	if each_line[:8] == 'timestep':
		timestep.append(t/1000)
		t +=10
	elif each_line[:7] == 'defects':
		(name,nu_de,interstitials,nu_in,vacancies,nu_va) = each_line.split( )
		defects.append(int(nu_de))
	else:
		continue
with open("defects.txt",'w') as f:
	for i in range(len(timestep)):
		f.write("%.2f %3d \n" %(timestep[i],defects[i]))
print(defects)
plt.plot(timestep,defects,'bo--')
plt.xlabel('Timestep(ps)')
plt.ylabel('Number of frenkel pairs')
plt.grid(True)
plt.axis([0,10,0,200])
plt.show()



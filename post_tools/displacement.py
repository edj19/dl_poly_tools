import numpy as np
import matplotlib.pylab as plt
f = open('RSDDAT')
displacements = []
timestep =[]
time = []
number = 0
t = 0
# To calculate the all of displacement numbers
# for each_line in f:
#     if each_line[:8] == 'timestep':
#         timestep.append(t)
#         t +=50
#         # print(t)
# #     elif each_line[:13] == 'displacements':
# #         (rol,y) = each_line.split( )
# #         displacements.append(y)
# #         number+=1
#     else:
#         continue


# To calculate the specific atom displacement distance

for each_line in f:
    if each_line[:8] == 'timestep':
        timestep.append(t)
        t +=10
    elif each_line[:2] == 'Ti':
        (name,index,disp) = each_line.split( )
        # print(index)
        if index == '1' :
            displacements.append(float(disp))
            number+=1
            time.append(t)
    else:
        continue
print(displacements)
n = np.arange(number)
#plt.plot(n,displacements,'r')
# plt.axis([0,4000,0,3.0])
plt.plot(time,displacements,'r--')
plt.show()

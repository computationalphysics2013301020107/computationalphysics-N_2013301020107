
import numpy as np
import matplotlib.pyplot as plt
import math

v=[]
t=[]
a=10
b=1
dt=0.1
v.append(100.)
t.append(0)
end_time=15

for i in range(int(end_time/dt)):
        tmp=v[i]+(a-b*v[i])*dt
        v.append(tmp)        
        t.append(dt*(i+1))
        print t[-1],v[-1]


plt.plot(t,v,color="blue",linestyle='-',label='Eluer')
plt.xlabel("time(s)")
plt.ylabel("speed(m/s)")
plt.title("v-t")
plt.show()
savefig("test_.jpg")




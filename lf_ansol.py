import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#VALORI DI INPUT ---------------------------------
a=1
x0=5
L=10
J=101
cf= 0.5
u = []
un,un2,norme = [],[],[]
err=[]
deltax= L/(J-1)
deltat= (deltax * cf)/a

#FUNZIONI-----------------------------------------
def gaussian(a, b):
    return np.exp(-np.power(a-b,2))
    
def analytical(a,b,t):
    return np.exp(-np.power(a-t-b,2))

def laxfried(*x):
    y = []
    for j in range(0,len(x)):
        if j==0:
            umin=-1
            umax=j+1
        else:  
            if j==J-2:
                umin=j-1
                umax=0
            else:
                umin=j-1
                umax=j+1
        val= 0.5*( (x[umin]) + (x[umax]) ) - ( (a*deltat)/(2*deltax) )*( (x[umax]) - (x[umin]) )
        y.append(val)
    return y

def norma(*y):
    return LA.norm(y)/np.sqrt(J)
#--------------------------------------------------
x_val= np.arange(0,L,deltax)  #calcolo vettore x 

fig1=plt.figure(1)

u = gaussian(x_val,x0)
plt.plot(x_val,u,label='0')
analytical_solutions = []

permitted_times = {
    100:5,
    200:10,
    300:15,
    400:20
}

for val in permitted_times.values():
    analytical_solutions.append(analytical(x_val,x0,val))

analytical_solutions = np.asarray(analytical_solutions)

for i in range(len(analytical_solutions)):
        plt.plot(x_val, analytical_solutions[i],label=str(5*(i+1)))
plt.legend(loc=0)  
plt.xlabel('x')
plt.ylabel('u')
plt.title('Sol. analitiche Lax-Friedrichs')
#fig1.set_size_inches(10,7)
#plt.savefig("2_lax-friedrichs.png", dpi=100)
plt.show(block=True)
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#VALORI DI INPUT ---------------------------------
a=1
x0=5
L=10
J=101
cf=0.5
#u = []
un,un2,norme = [],[],[]
deltax= L/(J-1)
deltat= (deltax * cf)/a

#FUNZIONI-----------------------------------------
def gaussian(a, b):
    return np.exp(-np.power(a-b,2))

def ftcs(*x):
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

        val= x[j] - ( (a*deltat)/(2*deltax) )*( (x[umax]) - (x[umin]) )
        y.append(val)
    return y

def analytical(a,b,t):
    return np.exp(-np.power(a-t-b,2))

def norma(*y):
    return LA.norm(y)/np.sqrt(J)
#--------------------------------------------------

x_val= np.arange(0,L,deltax) #calcolo vettore x

fig1=plt.figure(1)
'''
for i in x_val:
    u.append(gaussian(i,x0))  #calcolo vettore u
'''
u = gaussian(x_val,x0)
plt.plot(x_val,u, label='u(x,0)')

un = ftcs(*u)                 #secondo u
permitted_times = {
    200:10,
    400:20
}

err = []

#tutti gli altri u
for i,n in enumerate(np.arange(0,20+deltat,deltat)):
    un2 = ftcs(*un)
    norme.append(norma(*un2))
    if i in permitted_times.keys():
        err.append(norma(un2 - analytical(x_val,x0,i)))
        plt.plot(x_val,un2,label='u(x,'+ str(permitted_times[i]) +')')
        plt.legend(loc=0)
    un = un2

plt.xlabel('x')
plt.ylabel('u')
plt.title('Metodo FTCS')
#fig1.set_size_inches(10,7)
plt.savefig("1new_ftcs.png", dpi=100)
plt.show(1)

fig2=plt.figure(2)
plt.plot(np.arange(0,20+deltat,deltat),norme)
plt.title('Norma L2 con metodo FTCS')
plt.xlabel('t')
plt.ylabel('L2-norm')
fig2.set_size_inches(10,7)
plt.savefig("1_normeftcs.png", dpi=100)


plt.figure(3)
for t,e in zip((permitted_times.values()),err):
    plt.plot(t,e,marker='.')
plt.show(3)
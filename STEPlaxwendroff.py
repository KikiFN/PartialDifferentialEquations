import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#VALORI DI INPUT---------------------------------
a=1
x0=5
L=10
J=101
cf= 0.5
u = []
un,un2,norme = [],[],[]
deltax= L/(J-1)
deltat= (deltax * cf)/a

#FUNZIONI-----------------------------------------
def step(*j):
    s=[]
    for x in j:
        if x <= 6. and x >= 4:
            s.append(1)
        else: 
            s.append(0)
    return s

def laxwendroff(*x):
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

        val= x[j]-(((a*deltat)/(2*deltax))*(x[umax]-x[umin]))+(((np.power(a,2)*np.power(deltat,2)/(2*np.power(deltax,2)))*(x[umax]-(2*x[j])+x[umin])))
        y.append(val)
    return y

def norma(*y):
    return LA.norm(y)/np.sqrt(J)
#--------------------------------------------------
x_val= np.arange(0,L,deltax)                  #calcolo vettore x

fig1=plt.figure(1)
u = step(*x_val)             #primo u
plt.plot(x_val,u, label='u(x,0)')
un = laxwendroff(*u)         #secondo u

permitted_times = {
    100:5,
    200:10,
    300:15,
    400:20
}
#tutti gli altri u
for i,n in enumerate(np.arange(0,20+deltat,deltat)):
    un2 = laxwendroff(*un)
    norme.append(norma(*un2))
    if i in permitted_times.keys(): 
        plt.plot(x_val,un2,label='u(x,'+ str(permitted_times[i]) +')')
    un = un2
plt.legend(loc=0)
plt.xlabel('x')
plt.ylabel('u')
plt.title('Metodo Lax-Wendroff')
fig1.set_size_inches(12,7)
plt.savefig("STEPlax-wendroff.png", dpi=100)

fig2=plt.figure(2)
plt.plot(np.arange(0,20+deltat,deltat),norme)
plt.title('Norma L2 con metodo Lax-Wendroff')
plt.xlabel('t')
plt.ylabel('L2-norm')
fig2.set_size_inches(12,7)
plt.savefig("STEPnormewendroff.png")
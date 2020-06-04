import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#VALORI DI INPUZZ ---------------------------------
a=1
x0=5
L=10
J=101
cf= 0.5
u = []
un,un2,normacons = [],[],[]
s, sn, sn2, normanoncons = [],[],[],[]
deltax= L/(J-1)
deltat= (deltax * cf)/a

#FUNZIONI-----------------------------------------
def gaussian(a, b):
    return (10*np.exp(-np.power(a-b,2)))

def conservative(*x):
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

        val= x[j] - (deltat/deltax)*((0.5*(x[j]**2))-(0.5*(x[umin]**2)))
        y.append(val)
    return y

def NONconservative(*x):
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

        val= x[j] - (deltat/deltax)*x[j]*(x[j] - x[umin])
        y.append(val)
    return y


def norma(*y):
    return LA.norm(y)/np.sqrt(J)
#--------------------------------------------------

#calcolo vettore x
x_val= np.arange(0,L,deltax) 

plt.figure(1)
#primo u
for i in x_val:
    u.append(gaussian(i,x0)) #calcolo vettore u
plt.plot(x_val,u)
normacons.append(norma(*u))
#secondo u
un = conservative(*u)
plt.plot(x_val,un)
normacons.append(norma(*un))

#tutti gli altri u
for n in np.arange(0,0.5+deltat,deltat):
    un2 = conservative(*un)
    normacons.append(norma(*un2))
    #print(un2)
    plt.plot(x_val,un2)
    un = un2
    n+=1

plt.savefig("Upwindcons.png")

plt.figure(2)
plt.plot(normacons)
plt.savefig("Cons-norma.png")

#-------------------------------------- NON CONSERVATIVA -------------------------------
plt.figure(3)
#primo u
for i in x_val:
    s.append(gaussian(i,x0)) #calcolo vettore s
plt.plot(x_val,s)
normanoncons.append(norma(*s))
#secondo s
sn = NONconservative(*s)
plt.plot(x_val,sn)
normanoncons.append(norma(*sn))

#tutti gli altri s
for n in np.arange(0,0.5+deltat,deltat):
    sn2 = NONconservative(*sn)
    normanoncons.append(norma(*sn2))
    #print(un2)
    plt.plot(x_val,sn2)
    sn = sn2
    n+=1

plt.savefig("UpwindNONcons.png")

plt.figure(4)
plt.plot(normanoncons)
plt.savefig("NONCons-norma.png")




import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#VALORI DI INPUZZ ---------------------------------
a=1
x0=5
L=10
J=101
cf= 0.5
u,un,u0,norme = [],[],[],[]
deltax= L/(J-1)
deltat= (deltax * cf)/a

#FUNZIONI-----------------------------------------
def gaussian(a, b):
    return np.exp(-np.power(a-b,2))
def gaussian0(a, b):
    return np.exp(-np.power(a-(b-1),2))
def laxfried(*v):
    y = []
    for j in range(0,len(v)):
        if j==0:
            meno1=-1 #indice per ultimo valore del vett
            piu1=j+1 
        else:  
            if j==J-2:
                meno1=j-1
                piu1=0 #indice primo valore del vett
            else:
                meno1=j-1
                piu1=j+1

        val= 0.5*( (v[meno1]) + (v[piu1]) ) - ( (a*deltat)/(2*deltax) )*( (v[piu1]) - (v[meno1]) )
        y.append(val)
    return y

def leapfrog(v,w):
    y = []
    for j in range(0,len(v)):
        if j==0:
            meno1=-1 #indice per ultimo valore del vett
            piu1=j+1 
        else:  
            if j==J-2:
                meno1=j-1
                piu1=0 #indice primo valore del vett
            else:
                meno1=j-1
                piu1=j+1

        val= w[j] - ( (a*deltat)/(deltax) )*( (v[piu1]) - (v[meno1]) )
        y.append(val)
    return y
    
def norma(*y):
    return LA.norm(y)/np.sqrt(J)
#--------------------------------------------------

#calcolo vettore x
x_val= np.arange(0,L,deltax) 
plt.figure(1)
'''
for n in np.arange(0,20+deltat,deltat):
    if n == 0:
        for i in x_val:
            u.append(gaussian(i,x0)) #calcolo vettore u
        plt.plot(x_val,u)
        norme.append(norma(*u))
    un = laxfried(*u)
    norme.append(norma(*un))
    plt.plot(x_val,un)
    u = un
    n+=1
'''
for n in np.arange(0,20+deltat,deltat):
    if n == 0:
        for i in x_val:
            u.append(gaussian(i,x0)) #calcolo gaussiana u
            u0.append(gaussian0(i,x0)) #calcolo gaussiana prec u0
        plt.plot(x_val,u)
        plt.savefig("leap/leapfrog" + i + ".png")
    un = leapfrog(u[:],u0[:])
    plt.plot(x_val,un)
    u0=u
    u=un
    n+=1
plt.savefig("leap/leapfrog" + i + ".png")
#plt.show(1)
'''
plt.figure(2)
plt.plot(norme)
plt.savefig("norme.png")
plt.show(2)
'''
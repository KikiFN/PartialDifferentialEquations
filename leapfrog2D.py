import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#VALORI DI INPUZZ ---------------------------------
a=1
v=1
x0=5
y0=5
L=10
J=51
I=51
cf= 0.5
u,un,u0,norme = [],[],[],[]
deltax= L/(J-1)
deltay= L/(I-1)
deltat= (0.5*deltax)/v
cost=((v**2)*(deltat**2))/(deltax**2)

#FUNZIONI-----------------------------------------
def gaussian(a, b, c, d):
    return np.exp(-np.power(a-b,2) - np.power(c-d,2))
def gaussian0(a,b,c,d):
    return np.exp(-np.power(a-(b-1),2) - np.power(c - (d-1),2))

def leapfrog(v,w,z):  #AGGIUNGERE INDICE i
    y = []
    for j,i in (range(0,len(v)),range(0,len(z))):
        if j==0:
            jmeno1=-1 #indice per ultimo valore del vett
            jpiu1=j+1 
        else:  
            if j==J-2:
                jmeno1=j-1
                jpiu1=0 #indice primo valore del vett
            else:
                jmeno1=j-1
                jpiu1=j+1
        if i==0:
            imeno1=-1 #indice per ultimo valore del vett
            ipiu1=i+1 
        else:  
            if i==I-2:
                imeno1=i-1
                ipiu1=0 #indice primo valore del vett
            else:
                meno1=i-1
                piu1=i+1
        val= 2*v[]
        y.append(val)
    return y
    
def norma(*y):
    return LA.norm(y)/np.sqrt(J)
#--------------------------------------------------

#calcolo vettore x
x_val= np.arange(0,L,deltax) 
plt.figure(1)

for n in np.arange(0,20+deltat,deltat):
    if n == 0:
        for i in x_val:
            u.append(gaussian(i,x0)) #calcolo gaussiana u
            u0.append(gaussian0(i,x0)) #calcolo gaussiana prec u0
        plt.plot(x_val,u)
        norme.append(norma(*u))
    un = leapfrog(u[:],u0[:])
    plt.plot(x_val,un)
    norme.append(norma(*un))
    u0=u
    u=un
    n+=1
plt.savefig("leapfrog1D.png")
#plt.show(1)

plt.figure(2)
plt.plot(norme)
plt.savefig("leapfrog1D-norme.png")
#plt.show(2)

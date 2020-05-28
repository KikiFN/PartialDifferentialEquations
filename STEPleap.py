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
def step(*j):
    s=[]
    for x in j:
        if x <= 6. and x >= 4:
            s.append(1)
        else: 
            s.append(0)
    return s

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

'''
#normal chart
plt.figure(1)
for n in np.arange(0,20+deltat,deltat):
    if n == 0:
        u = step(*x_val)
        u0 = step(*(x_val-1))
        plt.plot(x_val,u)
        norme.append(norma(*u))
    un = leapfrog(u[:],u0[:])
    plt.plot(x_val,un)
    norme.append(norma(*un))
    u0=u
    u=un
    n+=1
plt.savefig("leap/STEP/leapfrogTOTAL.png")
#plt.show(1)
#end total chart

'''
#chart for gif
for m,n in enumerate(np.arange(0,20+deltat,deltat)):
    plt.clf()
    if n == 0:
        u = step(*x_val)
        u0 = step(*(x_val-1))
        plt.plot(x_val,u)
        norme.append(norma(*u))
        plt.savefig("leap/STEP/leapfrog" + str(m) + ".png")
    un = leapfrog(u[:],u0[:])
    plt.plot(x_val,un)
    norme.append(norma(*u))
    u0=u
    u=un
    n+=1
    plt.savefig("leap/STEP/leapfrog" + str(m) + ".png")
    plt.clf()
    plt.plot(norme)
    plt.savefig("norme/STEP/norm" + str(m) + ".png")
#plt.show(1)
#end chart for gif

'''
plt.figure(2)
plt.plot(norme)
plt.title('Norma')
plt.savefig("norme.png")
plt.show(2)
'''
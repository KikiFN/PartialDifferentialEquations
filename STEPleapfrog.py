import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#VALORI DI INPUT ---------------------------------
a=1
x0=5
L=10
J=101
cf=0.5
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
x_val= np.arange(0,L,deltax)                    #calcolo vettore x

fig1=plt.figure(1)
permitted_times = {
    100:5,
    200:10,
    300:15,
    400:20
}
for i,n in enumerate(np.arange(0,20+deltat,deltat)):
    if n == 0:
        u = step(*x_val)
        u0 = step(*(x_val+deltat))
        plt.plot(x_val,u, label='u(x,0)')
        #norme.append(norma(*u))
    un = leapfrog(u[:],u0[:])
    if i in permitted_times.keys(): 
        plt.plot(x_val,un,label='u(x,'+ str(permitted_times[i]) +')')
    norme.append(norma(*un))
    u0=u
    u=un
plt.legend(loc=0)
plt.xlabel('x')
plt.ylabel('u')
plt.title('Metodo Leapfrog')
fig1.set_size_inches(12,7)
plt.savefig("STEPleapfrog.png", dpi=100)

fig2=plt.figure(2)
plt.plot(np.arange(0,20+deltat,deltat),norme)
plt.title('Norma l2 con metodo Leapfrog')
plt.xlabel('t')
plt.ylabel('l2-norm')
fig2.set_size_inches(12,7)
plt.savefig("STEPleapfrog-norme.png")
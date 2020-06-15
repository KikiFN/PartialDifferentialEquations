import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
#VALORI DI INPUT ---------------------------------
x0=5
L=10
J=101
cf= 0.5
u = []
un,un2,normacons = [],[],[]
s, sn, sn2, normanoncons = [],[],[],[]
deltax= L/(J-1)
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
        val= x[j] - (deltat/deltax)*((0.5*((x[j])**2))-(0.5*((x[umin])**2)))
        y.append(val)
    return y

def NONconservative(*v):
    z = []
    for j in range(0,len(v)):
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
        valn= v[j] - (deltat/deltax)*v[j]*(v[j] - v[umin])
        z.append(valn)
    return z

def norma(*y):
    return LA.norm(y)/np.sqrt(J)
#--------------------------------------------------
x_val= np.arange(0,L,deltax)                 #calcolo vettore x

fig1=plt.figure(1)                              
for i in x_val:
    u.append(gaussian(i,x0)) #calcolo vettore u
plt.plot(x_val,u, label='u(x,0)')

a=np.max(u)
deltat= (deltax * cf)/a
un = conservative(*u)                         #secondo u

permitted_times = {
    10:0.05,
    20:0.1,
    50:0.25,
    100:0.5
}
#tutti gli altri u
for i,n in enumerate(np.arange(0,0.5+deltat,deltat)):
    un2 = conservative(*un)
    normacons.append(norma(*un2))
    if i in permitted_times.keys(): 
        plt.plot(x_val,un2,label='u(x,'+ str(permitted_times[i]) +')')
    un = un2
plt.legend(loc=0)
plt.xlabel('x')
plt.ylabel('u')
plt.title('Upwind conservativo')
fig1.set_size_inches(10,7) 
plt.savefig("Upwindcons.png", dpi=100)

fig2=plt.figure(2)
plt.plot(np.arange(0,0.5+deltat,deltat),normacons)
plt.title('Norma l2 upwind conservativo')
plt.xlabel('t')
plt.ylabel('l2-norm')
fig2.set_size_inches(10,7)
plt.savefig("Cons-norma.png")
#-------------------------------------- NON CONSERVATIVA -------------------------------
fig3=plt.figure(3)
for i in x_val:
    s.append(gaussian(i,x0)) #calcolo vettore s
plt.plot(x_val,s, label='u(x,0)')
sn = NONconservative(*s)          #secondo s

#tutti gli altri s
for i,n in enumerate(np.arange(0,0.5+deltat,deltat)):
    sn2 = NONconservative(*sn)
    normanoncons.append(norma(*sn2))
    if i in permitted_times.keys(): 
        plt.plot(x_val,sn2,label='u(x,'+ str(permitted_times[i]) +')')
    sn = sn2
    n+=1
plt.legend(loc=0)
plt.xlabel('x')
plt.ylabel('u')
plt.title('Upwind NON conservativo')
fig3.set_size_inches(10,7) 
plt.savefig("UpwindNONcons.png", dpi=100)

fig4=plt.figure(4)
plt.plot(np.arange(0,0.5+deltat,deltat),normanoncons)
plt.title('Norma l2 upwind non conservativo')
plt.xlabel('t')
plt.ylabel('l2-norm')
fig4.set_size_inches(10,7)
plt.savefig("NONCons-norma.png")

fig5=plt.figure(5)
plt.plot(x_val,s,label='u(x,0)' )
plt.plot(x_val,sn2,label='NFC' )
plt.plot(x_val,un2,label='FC' )
plt.legend(loc=0)
plt.xlabel('x')
plt.ylabel('u')
plt.title('Upwind confronto')
fig5.set_size_inches(10,7) 
plt.savefig("Upwindconfronto.png", dpi=100)
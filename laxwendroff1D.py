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
deltax= L/(J-1)
deltat= (deltax * cf)/a
#FUNZIONI-----------------------------------------
def gaussian(a, b):
    return np.exp(-np.power(a-b,2))

def r(a,t, b):
    return -2*np.exp(-np.power(a-t-b,2))*(a-t-b)

def s(a,t,b):
    return 2*np.exp(-np.power(a-t-b,2))*(a-t-b)

def ws(v,w):    #s e r 
    y = []
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
        snew= v[j] + ((a*deltat)/(2*deltax))*(w[umax] - w[umin]) + (np.power(a,2)*np.power(deltat,2)/(2*np.power(deltax,2)))*(v[umax]-(2*v[j])+v[umin])
        y.append(snew)
    return y

def wendroff(m,n,l):  #u,s(n-1), s
    z=[]
    for j in range(0,len(m)):
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
        unew= m[j] + (deltat/2)*(l[j] + n[j])
        z.append(unew)
    return z

def norma(*y):
    return LA.norm(y)/np.sqrt(J)
#--------------------------------------------------
x_val= np.arange(0,L,deltax)            #calcolo vettore x
t_val= np.arange(0,20,0.2)    #calcolo vettore t

r1=r(x_val,t_val,x0)
s1=s(x_val,t_val,x0)

sn=ws(s1,r1)
fig1=plt.figure(1)
for i in x_val:
    u.append(gaussian(i,x0))    #calcolo vettore u
plt.plot(x_val,u, label='u(x,0)')

permitted_times = {
    100:5,
    200:10,
    300:15,
    400:20
}
#tutti gli altri u
for i,n in enumerate(np.arange(0,20+deltat,deltat)):
    un = wendroff(u,sn,s1)
    norme.append(norma(*un2))
    if i in permitted_times.keys(): 
        plt.plot(x_val,un,label='u(x,'+ str(permitted_times[i]) +')')         
    u = un
plt.legend(loc=0)
plt.xlabel('x')
plt.ylabel('u')
plt.title('Metodo Lax-Wendroff')
fig1.set_size_inches(10,7)
plt.savefig("lax-wendroff1D.png", dpi=100)

fig2=plt.figure(2)
plt.plot(np.arange(0,20+deltat,deltat),norme)
plt.title('Norma L2 con metodo Lax-Wendroff')
plt.xlabel('t')
plt.ylabel('L2-norm')
fig2.set_size_inches(10,7)
plt.savefig("normewendroff1D.png", dpi=100)

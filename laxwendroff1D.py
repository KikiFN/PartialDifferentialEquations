import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
#VALORI DI INPUT ---------------------------------
a=1
x0=5
L=10
J=101
cf= 0.5
un2,norme = [],[]
deltax= L/(J-1)
deltat= (deltax * cf)/a
#FUNZIONI-----------------------------------------
def gaussian(a, b):
    return np.exp(-np.power(a-b,2))

def calc_r(a,t,b): #x,t,x0
    return -2*np.exp(-np.power(a-t-b,2))*(a-t-b)

def calc_s(a,t,b):
    return 2*np.exp(-np.power(a-t-b,2))*(a-t-b)

def whichMinMax(j):
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
    return umin,umax


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
t_val= np.arange(0,20+deltat,deltat)    #calcolo vettore t

r_100,s_100 = np.empty(len(x_val)),np.empty(len(x_val))
s_401 = np.empty([len(t_val),len(x_val)])
r_401 = np.empty([len(t_val),len(x_val)])

for n,t in enumerate(t_val):
    for i,x in enumerate(x_val):
        if n == 0:
            s_100[i] = 0 #100 val
            r_100[i] = calc_r(x,t,x0) #ne fa 100 cmq a t=0
        else:
            umin,umax = whichMinMax(i)
            
            s_100[i]= s_401[n-1,i] + ((a*deltat)/(2*deltax))*(r_401[n-1,umax] - r_401[n-1,umin]) + (np.power(a,2)*np.power(deltat,2)/(2*np.power(deltax,2)))*(s_401[n-1,umax]-(2*s_401[n-1,i])+s_401[n-1,umin])
            
            r_100[i] = r_401[n-1,i] + ((a*deltat)/(2*deltax))*(s_401[n-1,umax] - s_401[n-1,umin]) + (np.power(a,2)*np.power(deltat,2)/(2*np.power(deltax,2)))*(r_401[n-1,umax]-(2*r_401[n-1,i])+r_401[n-1,umin])
            
    s_401[n] = s_100
    r_401[n] = r_100



u0= np.empty(len(x_val))
u = np.empty([len(t_val),len(x_val)])

for n,t in enumerate(t_val):
    for i,x in enumerate(x_val):
        if n == 0:
            u0[i] = gaussian(x,x0)
            
        else:
            u0[i]= u[n-1,i] + (deltat/2)*(s_401[n,i] + s_401[n-1,i])
    norme.append(norma(u0))
    u[n] = u0
    

fig1=plt.figure(1)

permitted_times = {
    100:5,
    200:10,
    300:15,
    400:20
}
for val in permitted_times.keys():
    plt.plot(x_val,u[key], label='u(x,{})'.format(permitted_times[val]))


plt.legend(loc=0)
plt.xlabel('x')
plt.ylabel('u')
plt.title('Metodo Lax-Wendroff')
#fig1.set_size_inches(10,7)
plt.savefig("lax-wendroff1D.png", dpi=100)
plt.show()


fig2=plt.figure(2)
plt.plot(np.arange(0,20+deltat,deltat),norme)
plt.title('Norma L2 con metodo Lax-Wendroff')
plt.xlabel('t')
plt.ylabel('L2-norm')
#fig2.set_size_inches(10,7)
plt.savefig("normewendroff1D.png", dpi=100)
plt.show()

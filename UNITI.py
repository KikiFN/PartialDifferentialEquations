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
u0 = []
u1,u2,u4=[],[],[]
un1,un2,un3,un4=[],[],[],[]
err1,err2,err3,err4=[],[],[],[]
deltax= L/(J-1)
deltat= (deltax * cf)/a
#FUNZIONI-----------------------------------------
def gaussian(a, b):
    return np.exp(-np.power(a-b,2))
def gaussian0(a, b):
    return np.exp(-np.power(a-(b-deltat),2))
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
def laxfried(*x):
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
        val= 0.5*( (x[umin]) + (x[umax]) ) - ( (a*deltat)/(2*deltax) )*( (x[umax]) - (x[umin]) )
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
        val= x[j]-(((a*deltat)/(2*deltax))*(x[umax]-x[umin]))+((np.power(a,2)*np.power(deltat,2))/(2*np.power(deltax,2)))*(x[umax]-(2*x[j])+x[umin])
        y.append(val)
    return y
def norma(*y):
    return LA.norm(y)/np.sqrt(J)
#--------------------------------------------------
x_val= np.arange(0,L,deltax) 
permitted_times = {
    100:5,
    200:10,
    300:15,
    400:20
}
for i in x_val:
    u.append(gaussian(i,x0))
#-----FTCS-----------
u1 = ftcs(*u) 
for i,n in enumerate(np.arange(0,20+deltat,deltat)):
    un1 = ftcs(*u1)
    if i in permitted_times.keys():
        if i == 200 or i == 400: err1.append(norma(un1 - gaussian(x_val,x0)))      
    u1 = un1
#-----FRIED------
u2 = laxfried(*u)  
for i,n in enumerate(np.arange(0,20+deltat,deltat)):
    un2 = laxfried(*u2)
    if i in permitted_times.keys(): 
        if i == 200 or i == 400: err2.append(norma(un2 - gaussian(x_val,x0)))
    u2 = un2
#------Leap-----------------
for k,n in enumerate(np.arange(0,20+deltat,deltat)):
    if n == 0:
        for i in x_val:
            u0.append(gaussian0(i,x0))   #calcolo gaussiana prec u0
    un3 = leapfrog(u[:],u0[:])
    if k in permitted_times.keys(): 
        if k == 200 or k == 400: err3.append(norma(un3 - gaussian(x_val,x0)))
    u0=u
    u=un3
#-------Wend---------------
u4 = laxwendroff(*u) 
for i,n in enumerate(np.arange(0,20+deltat,deltat)):
    un4 = laxwendroff(*u4)
    if i in permitted_times.keys():
        if i == 200 or i == 400: err4.append(norma(un4 - gaussian(x_val,x0))) 
    u4 = un4

fig1=plt.figure(1)
permitted_times = {
    200:10,
    400:20
}
#plt.plot(list(permitted_times.values()),err1,'o-')
plt.plot(list(permitted_times.values()),err2,'o-',label='Lax-Friedrichs')
plt.plot(list(permitted_times.values()),err3,'o-',label='Leapfrog')
plt.plot(list(permitted_times.values()),err4,'o-',label='Lax-Wendroff')
plt.legend(loc=0)
plt.title('Norma l2 per errore della soluzione')
plt.xlabel('t')
plt.ylabel('l2-norm err')
fig1.set_size_inches(12,7)
plt.savefig('Uerr.png', dpi=100)
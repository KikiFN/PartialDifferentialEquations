import numpy as np
import matplotlib.pyplot as plt

#VALORI DI INPUZZ ---------------------------------
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

def norma(*y):
    somma=0
    for j in range(0,len(y)):
        mod=0
        mod = np.power(y[j],2)
        somma+=mod
    return np.sqrt(somma/J)
#--------------------------------------------------

#calcolo vettore x
x_val= np.arange(0,L,deltax) 

plt.figure(1)
#primo u
for i in x_val:
    u.append(gaussian(i,x0)) #calcolo vettore u
#plt.plot(x_val,u)
#norme.append(norma(*u))
#secondo u
un = ftcs(*u)
#plt.plot(x_val,un)
#norme.append(norma(*un))

permitted_times = [0,5,10,15,20]

#tutti gli altri u
for i,n in enumerate(np.arange(0,20+deltat,deltat)):
    un2 = ftcs(*un)
    norme.append(norma(*un2))
    #print(un2)
    if i in permitted_times: plt.plot(x_val,un2)
    un = un2
    n+=1


plt.savefig("ftcs.png")
plt.show(1)

print(len(norme))

plt.figure(2)
plt.plot(np.arange(0,20+deltat,deltat),norme)
plt.savefig("normeftcs.png")
plt.show(2)

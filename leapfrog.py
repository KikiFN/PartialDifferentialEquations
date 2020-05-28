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

def leapfrog(*x):
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

        val=  (x[j]) - ( (a*deltat)/(2*deltax) )*( (x[umax]) - (x[umin]) )
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

#calcolo entrata laxf
for s in x_val:
    s.append(gaussian(i,x0)) #calcolo vettore s
#plt.plot(x_val,s)
#norme.append(norma(*u))
#secondo s
sn = laxfried(*s)

#plt.plot(x_val,un)
#norme.append(norma(*un))

#primo u
un = leapfrog(*u)
plt.plot(x_val,un)
norme.append(norma(*un))

#secondo u
un = leapfrog(*u)
plt.plot(x_val,un)
norme.append(norma(*un))

#tutti gli altri u
for n in np.arange(0,20+deltat,deltat):
    un2 = leapfrog(*un)
    norme.append(norma(*un2))
    #print(un2)
    plt.plot(x_val,un2)
    un = un2
    n+=1


plt.savefig("lax-wendroff.png")
plt.show(1)

print(len(norme))

plt.figure(2)
plt.plot(norme)
plt.savefig("normewendroff.png")
plt.show(2)

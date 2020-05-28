import numpy as np
import matplotlib.pyplot as plt

#VALORI DI INPUZZ ---------------------------------
a=1
x0=5
L=10
J=101
cf= 0.5
u, x= [],[]
un,un2,norme = [],[],[]
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
u = step(*x_val)
plt.plot(x_val,u)
norme.append(norma(*u))
#secondo u
un = laxfried(*u)
plt.plot(x_val,un)
norme.append(norma(*un))

#tutti gli altri u
for n in np.arange(0,5,deltat):
    un2 = laxfried(*un)
    norme.append(norma(*un2))
    #print(un2)
    plt.plot(x_val,un2)
    un = un2
    n+=1


plt.savefig("STEPlax-friedrichs.png")
plt.show(1)

print(len(norme))

plt.figure(2)
plt.plot(norme)
plt.savefig("STEPnorme.png")
plt.show(2)

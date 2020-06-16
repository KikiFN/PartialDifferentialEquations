import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
from mpl_toolkits import mplot3d

#VALORI DI INPUZZ ---------------------------------
a=1
v=1
x0=5
y0=5
L=10
J=51
I=51
cf= 0.5
norme = []
deltax= L/(J-1)
deltay= L/(I-1)
deltat= (0.5*deltax)/v
cost=np.power((v*deltat/deltax),2)

#FUNZIONI-----------------------------------------
def gaussian(a, b, c, d):
    return np.exp(-np.power(a-b,2) - np.power(c-d,2))
def gaussian0(a,b,c,d):
    return np.exp(-np.power(a-(b-deltat),2) - np.power(c - (d-deltat),2))

def whichMinMax(j):
    if j==0:
        umin=-1
        umax=j+1
    elif j==J-2:
        umin=j-1
        umax=0
    else:
        umin=j-1
        umax=j+1
    return umin,umax

def norma(*y):
    return LA.norm(y)/np.sqrt(J)
#--------------------------------------------------

#calcolo vettore x
x_val= np.arange(0,L,deltax) 
y_val= np.arange(0,L,deltay)
t_val = np.arange(0,20+deltat,deltat)
lenX,lenY,lenT = len(x_val),len(y_val),len(t_val)

u_step = np.zeros([lenX,lenY])
u = np.empty([lenT,lenX,lenY]) #201 matrici 50x50

for t in range(lenT):
    for x in range(lenX):
        xmin,xmax = whichMinMax(x)
        for y in range(lenY):
            ymin,ymax = whichMinMax(y)
            if t == 0:
                u_step[x,y] = gaussian0(x,x0,y,y0)
            if t == 1:
                u_step[x,y] = gaussian(x,x0,y,y0)
            else:
                u_step[x,y] = 2*u[t-1,x,y] - u[t-2,x,y] + cost*(u[t-1,xmax,y] - 2*u[t-1,x,y] + u[t-1,xmin,y]) + cost*(u[t-1,x,ymax] - 2*u[t-1,x,y] + u[t-1,x,ymin])
    norme.append(norma(u_step))
    u[t] = u_step
    #print(u_step,u_step.shape, t)


fig = plt.figure(1)
ax = fig.gca(projection='3d')
x_val, y_val = np.meshgrid(x_val, y_val)
ax = plt.axes(projection='3d')
for i,u_t in enumerate(u):
        ax.plot_surface(x_val,y_val,u_t)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
#plt.savefig("leapfrog2D.png")
plt.show(1)

fig2=plt.figure(2)
plt.plot(np.arange(0,20+deltat,deltat),norme)
plt.title('Norma Leapfrog 2D')
plt.xlabel('t')
plt.ylabel('Leap2D-norm')
#fig2.set_size_inches(10,7)
#plt.savefig("normeleap2D.png", dpi=100)
plt.show(2)
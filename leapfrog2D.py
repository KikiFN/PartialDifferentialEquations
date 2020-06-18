import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
from mpl_toolkits import mplot3d
import matplotlib as mpl

#VALORI DI INPUZZ ---------------------------------
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
def gaussian(a, b):
    return np.exp(-((a-5)**2) - ((b-5)**2))
def gaussian0(a,b):
    return np.exp(- ((a-(5-deltat))**2) - ((b-(5-deltat))**2))
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
#MAIN---------------------------------------------
#calcolo vettore x
x_val= np.arange(0,L,deltax)
y_val= np.arange(0,L,deltay)
t_val = np.arange(0,20+deltat,deltat)
lenX,lenY,lenT = len(x_val),len(y_val),len(t_val)

X, Y = np.meshgrid(x_val, y_val)

norme = np.zeros(lenT)
u0 = np.zeros([lenX,lenY])
u_step = np.zeros([lenX,lenY])
u = np.empty([lenT,lenX,lenY])

u0= gaussian0(X,Y)
u[1]= gaussian(X,Y)

for t in range(lenT):
    
    for x in range(lenX):
        xmin,xmax = whichMinMax(x)
        for y in range(lenY):
            ymin,ymax = whichMinMax(y)
            if t ==0:
                u_step[x,y] = u0[x,y]
                #print(u_step[x,y], u0[x,y])
            elif t == 1:
                u_step[x,y] = u[1,x,y]
            else:
                u_step[x,y] = 2*u[t-1,x,y] - u[t-2,x,y] + cost*(u[t-1,xmax,y] - 2*u[t-1,x,y] + u[t-1,xmin,y]) + cost*(u[t-1,x,ymax] - 2*u[t-1,x,y] + u[t-1,x,ymin])
    #print(u_step)
    u[t] = u_step
    norme[t] = norma(u_step)

#print(u[0],u0)

permitted_times = {
    0:0,
    50:5,
    100:10,
    150:15,
    200:20
}

fig = plt.figure(1)
ax = fig.gca(projection='3d')
#x_val, y_val = np.meshgrid(x_val, y_val)
ax = plt.axes(projection='3d')
ph=1
for i,Z in enumerate(u):
    if i in permitted_times.keys():
        #plt.cla()
        surf = ax.plot_surface(X,Y,Z,label='u(x,'+ str(permitted_times[i]) +')',alpha=ph)
        surf._facecolors2d=surf._facecolors3d
        surf._edgecolors2d=surf._edgecolors3d
        ph-=0.2
ax.legend(loc=0)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
#plt.savefig('leapfrog2D_frame{}.png'.format(permitted_times[i]))
plt.show(block=True)

fig2=plt.figure(2)
plt.plot(t_val,norme)
plt.title('Norma Leapfrog 2D')
plt.xlabel('t')
plt.ylabel('Leap2D-norm')
#fig2.set_size_inches(10,7)
#plt.savefig("normeleap2D.png", dpi=100)
plt.show(block=True)
#Autor Sebastian Rodriguez
import math

def sumai(a,b):
    real = a[0]+b[0]
    img = a[1]+b[1]
    return(real,img)

def multii(a,b):
    real = (a[0]*b[0]-a[1]*b[1])
    img = (a[0]*b[1]+a[1]*b[0])
    return(real,img)

def divi(a,b):
    real = ((a[0]*b[0]+a[1]*b[1]),(b[0])**2+(b[1])**2)
    img = ((a[1]*b[0]-a[0]*b[1]),(b[0])**2+(b[1])**2)
    return(real,img)

def modi(a):
    r = math.sqrt((a[0])**2+(a[1])**2)
    return(r)

def conjugado(a):
    respuesta = a[1]*-1
    return(a[0],respuesta)

def fasetest(a):
    r = math.atan2(a[1],a[0])
    return(r)

def polar(a):
    angle = math.atan2(a[1],a[0])
    rho = math.sqrt((a[0] * a[0]) + (a[1] * a[1]))
    if a[1] < 0 and a[0] < 0:
        angle = angle + 180
    if a[1] > 0 and a[0] < 0:
        angle = 180 - angle
    if a[1] < 0 and a[0] > 0:
        angle = 360 - angle
    return (rho, angle)

def inverso(a):
    resp = (a[0]*-1, a[1]*-1)
    return resp
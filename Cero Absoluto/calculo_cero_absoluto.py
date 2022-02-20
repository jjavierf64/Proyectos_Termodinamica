## Creado por Javier Fernández
## Fecha: 18 febrero 2022
## Python 3.9
import math
import matplotlib.pyplot as plt
import numpy as np


def calcY(x, m, b=0.0):
    y=[]
    for xi in x:
        y.append(xi*m+b)
    return y

def calcInterseccion(x, y, m):
    b = y - m*x    
    return b

def calcPendiente(y1,y2,x1,x2):
    m = (y1-y2)/(x1-x2)
    return m

def calcVolumen(diametro):
    volumen = (4*math.pi*(diametro/2)**3)/3
    return volumen



# Definición de Datos

t1 = {
        "Temperatura":37.0,
        "Diametro":6.0}

t2 = {
        "Temperatura":-18.0,
        "Diametro":5.5
}


# Calculo Volumen
t1["Volumen"]= calcVolumen(t1["Diametro"])

t2["Volumen"]= calcVolumen(t2["Diametro"])

# Calculo Pendiente
m = calcPendiente(t1["Temperatura"], t2["Temperatura"], t1["Volumen"], t2["Volumen"])

# Calculo Interseccion

b = calcInterseccion(t1["Volumen"], t1["Temperatura"], m)

# Calculo Datos
V = np.arange(0, 25.0, 1)
T = calcY(V, m, b)

ceroAbsoluto= round(calcY([0],m,b)[0], 3)

print("\n\n El valor estimado para el cero absoluto es de:\n\n  ************\n  *          *\n  * "+str(ceroAbsoluto)+" *\n  *          *\n  ************\n\n\n\n")

plt.plot(V,T)
plt.xlabel('Volumen (cm^3)')
plt.ylabel('Temperatura (°C)')
plt.title('Relación de Temperatura vs Volumen en un globo que se enfría.')
plt.style.use('seaborn-dark')
plt.show()

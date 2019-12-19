import math
from _decimal import Decimal
def power2sum(tab):
    somme = 0.0
    for i in range(len(tab)):
        somme += tab[i] ** 2
    return somme
def sumXY(tab1, tab2):
    somme = 0
    for i in range(len(tab1)):
        somme += tab1[i] * tab2[i]
    return somme
def sum(tab):
    somme = 0.0
    for i in range(len(tab)):
        somme += tab[i]
    return somme
def calcul_A(x,y,z):
    n = len(x)
    Det_P1 = sumXY(x,z)*(n*power2sum(y)-sum(y)**2)-(sumXY(x,y)*(n*sumXY(y,z)-sum(z)*sum(y)))+(sum(x)*(sumXY(y,z)*sum(y)-sum(z)*power2sum(y)))
    Det_P = (power2sum(x) * n * power2sum(y)) - (power2sum(x) * sum(y) ** 2) - (sumXY(x, y) * n * sumXY(x, y)) + ( sumXY(x, y) * sum(x) * sum(y)) + (sum(x) * sumXY(x, y) * sum(y)) - (sum(x) * sum(x) * power2sum(y))
    return Det_P1/Det_P
def calcul_B(x,y,z):
    n = len(x)
    Det_P2 = (power2sum(x)*((sumXY(y,z)*n)-(sum(y)*sum(z))))-(sumXY(x, z)*((n*sumXY(y,x))-(sum(x)*sum(y))))+(sum(x)*((sumXY(y,x)*sum(z))-(sum(x)*sumXY(y,z))))
    Det_P = (power2sum(x) * n * power2sum(y)) - (power2sum(x)*sum(y) ** 2) - (sumXY(x, y) * n * sumXY(x, y)) + (sumXY(x,y)*sum(x) * sum(y)) + \
          (sum(x) * sumXY(x, y) * sum(y)) - (sum(x)*sum(x) * power2sum(y))
    return (Det_P2 / Det_P)
def calcul_C(x,y,z):
    n = len(x)
    c = (sum(z) - calcul_A(x, y, z) * sum(x) - calcul_B(x, y, z) * sum(y)) / n
    return c
def getNe(Filename):
    with open(Filename) as f:

        array = []
        for line in f:  # read rest of lines
            array.append([float(x) for x in line.split()])
    return len(array)

def Regresion3D(NamFile):
    with open(NamFile) as f:
        array = []
        for line in f:  # read rest of lines
            array.append([float(x) for x in line.split()])
    yarray = []
    for x in range(len(array)):
        yarray.append(array[x][1])
    xarray = []
    for x in range(len(array)):
        xarray.append(array[x][0])
    zarray = []
    for x in range(len(array)):
        zarray.append(array[x][2])

    a = calcul_A(xarray,yarray,zarray)
    b = calcul_B(xarray,yarray,zarray)
    c = calcul_C(xarray,yarray,zarray)

    zA = []
    for i in range(len(zarray)):
        zA.append(a * xarray[i] + b * yarray[i] + c)



    return  a,b,c,xarray, yarray, zarray,zA
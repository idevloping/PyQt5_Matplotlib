
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
def Clcul__A_RE(x, z):
    n = len(x)
    one = (n * (sumXY(x, z)) - sum(x) * sum(z))
    two = (n * (power2sum(x)) - sum(x) ** 2)
    return (one / two)
def Calcul__B_RE(x, z):
    n = len(x)
    one = (sum(z) * power2sum(x)) - (sum(x) * sumXY(x, z))
    two = (n * power2sum(x) - sum(x) ** 2)
    return (one / two)
def getNe(Filename):
    with open(Filename) as f:
        array = []
        for line in f:  # read rest of lines
            array.append([float(x) for x in line.split()])
    return len(array)
def Regression2d(FileName):
    with open(FileName) as f:
        array = []
        for line in f:  # read rest of lines
            array.append([float(x) for x in line.split()])
    yarray = []
    for x in range(len(array)):
        yarray.append(array[x][1])
    zarray = []
    for x in range(len(array)):
        zarray.append(array[x][2])
    xarray = []
    for x in range(len(array)):
        xarray.append(array[x][0])
    a = Clcul__A_RE(xarray, zarray)
    b = Calcul__B_RE(xarray, zarray)

    zA = []
    for i in range(len(xarray)):
        zA.append(a * xarray[i] + b )
    # -----------------------------------------------------------------------------

    return a,b, xarray, zarray, zA

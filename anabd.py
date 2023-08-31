import math
from operator import index, indexOf

año = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 1996, 2000, 2010, 2020]
poblacion = [1650, 1750, 1860, 2070, 2300, 2520, 3020, 3700, 4450, 5300, 5570, 6144, 6970, 7821]

print("")

for i in poblacion:
    if len(poblacion) != poblacion.index(i) and poblacion.index(i) > 0:
        k = (math.log(i / poblacion[poblacion.index(i)-1])) / (año[poblacion.index(i)]-año[poblacion.index(i)-1])
        if poblacion.index(i)+1 < len(poblacion):
            print("(" + str(año[poblacion.index(i)]) + "-" + str(año[poblacion.index(i)+1]) + ") k = " + str(k))

print("")
print("Predicciones población:")
    
# vp = variable poblacion, va = variable año, dis = distancia en años
vp = 7821
va = 2020
dis = 1
for i in range(10):
    p = vp * math.e ** (k * dis)
    print("(" + str(va) + "-" + str(va+dis) + ") p = " + str(round(p, 1)) + " millones")
    vp = p
    va = va + dis
print("")
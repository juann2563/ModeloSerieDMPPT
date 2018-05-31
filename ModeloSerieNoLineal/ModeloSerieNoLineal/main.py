#importación de móudlo para obtener los parámetros de la ecuación del panel
import PvEquations as pv
import numpy as np
n = int(input("Ingrese la cantidad de PVs: "))
#Obtengo los valores de Isc, A0, B0 y Vpv para luego poder simular el comportamiento
[Isc, A0, B0, Vpv] = pv.EcuacionPv(n)
print(Isc)
Ipv = np.zeros((n,1),dtype=float) # arreglo para almacenar la corriente de cada pv
ones = np.ones((n,1),dtype=float) ## columna de unos necesaria para ecuacion del panel
Ipv = Isc-A0*(np.e**(B0*Vpv)-ones)
#print(Ipv)




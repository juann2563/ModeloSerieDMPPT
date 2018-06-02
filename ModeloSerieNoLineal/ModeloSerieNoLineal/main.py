#importación de móudlo para obtener los parámetros de la ecuación del panel
import PvEquations as pv
import paramsConverter as conv
import numpy as np
n = int(input("Ingrese la cantidad de PVs: "))
#Obtengo los valores de Isc, A0, B0 y Vpv para luego poder simular el comportamiento
[Isc, A0, B0, Vpv] = pv.EcuacionPv(n)
Ipv = np.zeros((n,1),dtype=float) # arreglo para almacenar la corriente de cada pv
ones = np.ones((n,1),dtype=float) ## columna de unos necesaria para ecuación del panel
# con .dot se realiza la multiplicacion entre matrices
Ipv = Isc-np.dot(A0,(np.exp(np.dot(B0,Vpv))-ones)) # vector con las corrientes de cada PV
a = conv.modelParams(n)
print(a)
#Parámetros del convertidor







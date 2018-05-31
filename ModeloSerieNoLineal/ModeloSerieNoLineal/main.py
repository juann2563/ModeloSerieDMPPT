#importación de móudlo para obtener los parámetros de la ecuación del panel
import PvEquations as pv
import numpy as np
n = int(input("Ingrese la cantidad de PVs: "))
#Obtengo los valores de Isc, A0, B0 y Vpv para luego poder simular el comportamiento
[Isc, A0, B0, Vpv] = pv.EcuacionPV(n)



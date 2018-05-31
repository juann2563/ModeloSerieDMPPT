#biblioteca numpy para manejo de matrices
import numpy as np
#Define los parámetros de impresión, cantidad de decimales
np.set_printoptions(threshold=np.nan, precision=4)

#parámetos por defecto del panel
def parametrosDefault():
    parametros = []
    Istc = float(5.0)
    Gpv = float(1000)
    Gstc = float(1000)
    alphaI = float(0.065)
    Tpv = float(25)
    Tstc = float(25)
    Impp = float(4.7)
    Vmpp = float(18)
    Voc = float(22.1)
    alphaV = float(-80)
    #Cálculo de ecuaciones necesarias para obtener todos los parametros de la ecuacion del panel
    
    Bstc = np.log(1-(Impp/Istc))/(Vmpp-Voc)
    A01 = Istc*(np.e**(-Bstc*Voc))
    B01 = Bstc/(1+alphaV*(Tpv-Tstc))
    Isc1 = Istc*(Gpv/Gstc)*(1+alphaI*(Tpv-Tstc))
    parametros.append(Isc1)
    parametros.append(A01)
    parametros.append(B01)
    return parametros
# Función por Si el usuario quiere ingresar los datos del PV
def datosPv():
    parametros = []
    Istc = float(input("Ingrese Istc: "))
    Gpv = float(input("Ingrese Gpv: "))
    Gstc = float(input("Ingrese Gstc: "))
    alphaI = float(input("Ingrese alphaI: "))
    Tpv = float(input("Ingrese Tpv: "))
    Tstc = float(input("Ingrese Tstc: "))
    Impp = float(input("Ingrese Impp: "))
    Vmpp = float(input("Ingrese Vmpp: "))
    Voc = float(input("Ingrese Voc: "))
    alphaV = float(input("Ingrese AlphaV: "))
    #Cálculo de ecuaciones necesarias para obtener todos los parametros de la ecuacion del panel
    
    Bstc = np.log(1-(Impp/Istc))/(Vmpp-Voc)
    A01 = Istc*(np.e**(-Bstc*Voc))
    B01 = Bstc/(1+alphaV*(Tpv-Tstc))
    Isc1 = Istc*(Gpv/Gstc)*(1+alphaI*(Tpv-Tstc))
    parametros.append(Isc1)
    parametros.append(A01)
    parametros.append(B01)
    return parametros

# Función para calcular los parámetros de la ecuación del Pv
def EcuacionPv(n):
    # arreglos que van a almacenar los valores para n PVs
    Ipv = np.zeros((n,1),dtype=float) # corriente de cada pv
    Isc = np.zeros((n,1),dtype=float) # corriente de corticircuito
    Vpv = np.zeros((n,1),dtype=float) # voltaje de cada pv
    A0 = np.zeros((n,n),dtype=float) # ganacia A0 para cada ecuación del panel
    B0 = np.zeros((n,n),dtype=float) # ganacia B0 para cada ecuación del panel
    # si todos los paneles son iguales solo pide los parametros para uno 
    # y los replica para los demas
    while True:
        paramPv = 0
        equal = input("Son todos los PV iguales? S(si) - N(no) : ")
        tipo = input("Desea agregar los valores por default para el BP585?: S(si) - N(no): ")            
        if(equal == 'S' or equal == 's'):
            #obtengo los cálculos realizados en la funcion datosPV. Esta función
            #retorna arreglo con Isc, A0, B0 respectivametne
            if tipo=="S" or tipo=="s":
                paramPv = parametrosDefault()
            else:
                paramPv = datosPv() # [Isc, A0, B0]
            #Se asignan los mismos valores a cada IPV hasta n Pvs
            for i in range(0,n):
                Isc[i] = paramPv[0]
                A0[i,i] = paramPv[1]
                B0[i,i] = paramPv[2]
            # devuelve los vectores con los parametros
            return (Isc,A0,B0,Vpv)
        elif equal=='N' or equal == 'n':
            for i in range(0,n):
                paramPv = datosPv()
                Isc[i,0] = paramPv[0]
                A0[i,i] = paramPv[1]
                B0[i,i] = paramPv[2]

            return (Isc,A0,B0,Vpv)
        else:
            print("Debe ingresar un valor valido")

   
        


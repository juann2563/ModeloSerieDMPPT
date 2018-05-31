#biblioteca numpy para manejo de matrices
import numpy as np
#Define los parámetros de impresión, cantidad de decimales
np.set_printoptions(threshold=np.nan)
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

def EcuacionPV(n):

#Ecuacion del panel
#IPV = ISC −A0*(e^(B0*VPV) −1)

    # arreglos que van a almacenar los valores para n PVs
    Ipv = np.zeros((n,1),dtype=float) # corriente de cada pv
    Isc = np.zeros((n,1),dtype=float) # corriente de corticircuito
    Vpv = np.zeros((n,1),dtype=float) # voltaje de cada pv
    A0 = np.zeros((n,n),dtype=float) # ganacia A0 para cada ecuación del panel
    B0 = np.zeros((n,n),dtype=float) # ganacia B0 para cada ecuación del panel
    # si todos los paneles son iguales solo pide los parametros para uno 
    # y los replica para los demas
    while True:
        equal = input("Son todos los PV iguales? S(si) - N(no) : ")
        if(equal == 'S' or equal == 's'):
            #obtengo los cálculos realizados en la funcion datosPV. Esta función
            #retorna arreglo con Isc, A0, B0 respectivametne
            paramPv = datosPv() # [Isc, A0, B0]
            #Se asignan los mismos valores a cada IPV hasta n Pvs
            for i in range(0,n):
                Isc[(i,0)] = paramPv[0]
                A0[(i,0)] = paramPv[1]
                B0[(i,0)] = paramPv[2]
                #Isc[(i,0)] = Istc*(Gpv/Gstc)*(1+alphaI*(Tpv-Tstc))
                #A0[(i,0)] = Istc*(np.e**(-Bstc*Voc))
                #B0[(i,0)] = Bstc/(1+alphaV*(Tpv-Tstc))
        
            #Se obtiene el arreglo resultante de multiplicar todos los
            #arreglos con los valores de cada PV
            Ipv = (Isc-A0*(np.e**(B0*Vpv)-1))
            # devuelve los vectores con los parametros
            parametrosPvEqn = np.array([Isc,A0,B0])
            return parametrosPvEqn
        elif equal=='N' or equal == 'n':
            for i in range(0,n):
                paramPv = datosPv()
                Isc[(i,0)] = paramPv[0]
                A0[(i,0)] = paramPv[1]
                B0[(i,0)] = paramPv[2]

            Ipv = (Isc-A0*(np.e**(B0*Vpv)-1))
            parametrosPvEqn = np.array([Isc,A0,B0],dType=float)
            return parametrosPvEqn
        else:
            print("Debe ingresar un valor valido")

   
        


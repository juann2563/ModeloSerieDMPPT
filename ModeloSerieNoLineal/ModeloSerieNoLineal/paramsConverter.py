import numpy as np
#Función para obtener los parámeros del convertidor 
def paramsConverter(n):
    Ci = np.zeros((n,1),dtype=float) # Capacitorres de entrada
    L = np.zeros((n,1),dtype=float) # Bibinas
    Co = np.zeros((n,1),dtype=float) # Capacitores de salida
    Rci = np.zeros((n,1),dtype=float) #Pérdidas en capacitores de entrada
    RL = np.zeros((n,1),dtype=float) # Pérdidas en la bobina
    Rco = np.zeros((n,1),dtype=float) # Pérdidas en capacitor de salida
    Ron = np.zeros((n,1),dtype=float) # Pérdidas en el mosfet
    RB=69*np.exp(-3) # Resistencia de la batería
    VB = float(48) # voltaje de la vatería
    Rmpp = np.zeros((n,1),dtype=float)
    Vci = np.zeros((n,1),dtype=float)
    IL = np.zeros((n,1),dtype=float)
    Vco = np.zeros((n,1),dtype=float)
    equal = input("Son todos los convertidores iguales? : S(si) - N(no)")
    if equal == "S" or equal == "s":
        tipo = input("Desea aplicar los parámetros por defecto: S(si) - N(no)")
        if tipo == 'S' or tipo == 's':
            #Parámetros por defecto para el convertidor
            Ci[:,0] = 27.7*np.exp(-6)
            L[:,0] = 240*np.exp(-6)
            Co[:,0] = 27.7*np.exp(-6)
            Rci[:,0] = 6*np.exp(-3)
            Rco[:,0] = 6*np.exp(-3)
            RL[:,0] = 60*np.exp(-3)
            Ron[:,0] = 35*np.exp(-3)
            RB = 69*np.exp(-3)
            VB = float(48)
            return (Ci,L,Co,Rci,Rco,RL,Ron,RB,VB)
    else:
        for i in range(0,n):
            Ci[i,1] = float(input("Ingrese Ci" + str(i+1)+": "))
            L[i,1] = float(input("Ingrese L" + str(i+1)+": "))
            Co[i,1] = float(input("Ingrese Co" + str(i+1)+": "))
            Rci[i,1] = float(input("Ingrese Rci" + str(i+1)+": "))
            Rco[i,1] = float(input("Ingrese Rco" + str(i+1)+": "))
            RL[i,1] = float(input("Ingrese RL" + str(i+1)+": "))
            Ron[i,1] = float(input("Ingrese Ron" + str(i+1)+": "))
        RB = float(input("Ingrese RB: "))
        VB = float(input("Ingrese VB: "))
        return (Ci,L,Co,Rci,Rco,RL,Ron,RB,VB)

def modelParams(n):
    [Ci,L,Co,Rci,Rco,RL,Ron,RB,VB] = paramsConverter(n)
    Ro = VB;
    Ron = np.zeros((n,1),dtype=float) # Model output resistance
    Rn = np.zeros((n,1),dtype=float) # Model input resistance
    for i in range(0,n):
        Ro = Ro+Rco[i,0]
    for i in range(0,n):
        Ron[i,0] = Ro-Rco[i,0]
    
        


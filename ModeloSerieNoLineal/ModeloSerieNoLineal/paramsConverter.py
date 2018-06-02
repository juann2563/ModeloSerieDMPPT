import numpy as np
#Función para obtener los parámeros del convertidor 
def paramsConverter(n):
    Ci = np.zeros((n,1),dtype=float) # Capacitorres de entrada
    U = np.zeros((n,1),dtype=float) # duty 
    L = np.zeros((n,1),dtype=float) # Bobinas
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
            U[:,0] = float(0.25)
            RB = 69*np.exp(-3)
            VB = float(48)
            return (Ci,L,Co,Rci,Rco,RL,Ron,RB,VB,U)
    else:
        for i in range(0,n):
            Ci[i,1] = float(input("Ingrese Ci" + str(i+1)+": "))
            L[i,1] = float(input("Ingrese L" + str(i+1)+": "))
            Co[i,1] = float(input("Ingrese Co" + str(i+1)+": "))
            Rci[i,1] = float(input("Ingrese Rci" + str(i+1)+": "))
            Rco[i,1] = float(input("Ingrese Rco" + str(i+1)+": "))
            RL[i,1] = float(input("Ingrese RL" + str(i+1)+": "))
            Ron[i,1] = float(input("Ingrese Ron" + str(i+1)+": "))
            U[i,0] = float(input("Ingrese U" + str(i+1)+"En el punto de operación: "))
        RB = float(input("Ingrese RB: "))
        VB = float(input("Ingrese VB: "))
        return (Ci,L,Co,Rci,Rco,RL,Ron,RB,VB,U)

def modelParams(n):
    [Ci,L,Co,Rci,Rco,RL,Ron,RB,VB,U] = paramsConverter(n)
    Ro = VB;
    Ro_n = np.zeros((n,1),dtype=float) # Model output resistance
    Rn = np.zeros((n,1),dtype=float) # Model input resistance
    # Constants like Ko1, Ko2 and Ko(n) are necessary to represent output capacitor voltage of each converter
    Kon = np.zeros((n,1),dtype=float)
    KL_n_3n_1 = np.zeros((n,1),dtype=float)
    KL_n_3n = np.zeros((n,1),dtype=float)
    for i in range(0,n):
        Ro = Ro+Rco[i,0] # Model output resistance
        Rn[i,0] = Rci[i,0]+RL[i,0] + Ron[i,0] # calculating all model input resistances
    for i in range(0,n):
        Ro_n[i,0] = Ro-Rco[i,0] # necesario paa reducir términos
        Kon = 1/(Ro[i,0]*Co[i,0])
    #calculating used in matrix −A and −B to calculate inductor current of each converter.
    for i in range(0,n):
        KL_n_3n_1[i,0] = (Rn[i,0]*Ro+Rco[i,0]*Ro_n[i,0]*(1-U[i,0]))/(L[i,0]*Ro)
        KL_n_3n[i,0] = ((1-U[i,0])*Ro_n[i,0])/(L[i,0]*Ro)
    
        


import numpy as np
#Función para obtener los parámeros del convertidor 
def paramsConverter(n):
    Ci = np.zeros((n,),dtype=float) # Capacitorres de entrada
    U = np.zeros((n,),dtype=float) # duty 
    L = np.zeros((n,),dtype=float) # Bobinas
    Co = np.zeros((n,),dtype=float) # Capacitores de salida
    Rci = np.zeros((n,),dtype=float) #Pérdidas en capacitores de entrada
    RL = np.zeros((n,),dtype=float) # Pérdidas en la bobina
    Rco = np.zeros((n,),dtype=float) # Pérdidas en capacitor de salida
    Ron = np.zeros((n,),dtype=float) # Pérdidas en el mosfet
    RB=69*np.exp(-3) # Resistencia de la batería
    VB = float(48) # voltaje de la vatería
    Rmpp = np.zeros((n,),dtype=float)
    Vci = np.zeros((n,),dtype=float)
    IL = np.zeros((n,),dtype=float)
    Vco = np.zeros((n,),dtype=float)
    equal = input("Son todos los convertidores iguales? : S(si) - N(no)")
    if equal == "S" or equal == "s":
        tipo = input("Desea aplicar los parámetros por defecto: S(si) - N(no)")
        if tipo == 'S' or tipo == 's':
            #Parámetros por defecto para el convertidor
            Ci[:] = 27.7*np.exp(-6)
            L[:] = 240*np.exp(-6)
            Co[:] = 27.7*np.exp(-6)
            Rci[:] = 6*np.exp(-3)
            Rco[:] = 6*np.exp(-3)
            RL[:] = 60*np.exp(-3)
            Ron[:] = 35*np.exp(-3)
            U[:] = float(0.25)
            RB = 69*np.exp(-3)
            VB = float(48)
            return (Ci,L,Co,Rci,Rco,RL,Ron,RB,VB,U)
    else:
        for i in range(0,n):
            Ci[i] = float(input("Ingrese Ci" + str(i+1)+": "))
            L[i] = float(input("Ingrese L" + str(i+1)+": "))
            Co[i] = float(input("Ingrese Co" + str(i+1)+": "))
            Rci[i] = float(input("Ingrese Rci" + str(i+1)+": "))
            Rco[i] = float(input("Ingrese Rco" + str(i+1)+": "))
            RL[i] = float(input("Ingrese RL" + str(i+1)+": "))
            Ron[i] = float(input("Ingrese Ron" + str(i+1)+": "))
            U[i] = float(input("Ingrese U" + str(i+1)+"En el punto de operación: "))
        RB = float(input("Ingrese RB: "))
        VB = float(input("Ingrese VB: "))
        return (Ci,L,Co,Rci,Rco,RL,Ron,RB,VB,U)

def modelParams(n):
    [Ci,L,Co,Rci,Rco,RL,Ron,RB,VB,U] = paramsConverter(n)
    Ro = VB;
    Ro_n = np.zeros((n,),dtype=float) # Model output resistance
    Rn = np.zeros((n,),dtype=float) # Model input resistance
    # Constants like Ko1, Ko2 and Ko(n) are necessary to represent output capacitor voltage of each converter
    Kon = np.zeros((n),dtype=float)
    KL_n_3n_1 = np.zeros((n),dtype=float)
    KL_n_3n = np.zeros((n),dtype=float)
    KL1_3n_1 = np.zeros((n),dtype=float)
    KL2_3n_1 = np.zeros((n),dtype=float)
    KLn = np.zeros((n),dtype=float)
    KLnI = np.zeros((n),dtype=float)
    KL1 = ((1-U1)*(Rco[1]))/(L[1]*Ro)
    Ko1 = 1/(Ro*Co[0])
    Ko2 = 1/(Ro*Co[1])
    KL12 = (Rn[0]*Ro+Rco[1]*Ro_n[0]*(1-U[0]))/(L[0]*Ro)
    KL25 = (Rn[1]*Ro+Rco[0]*Ro_n[1]*(1-U[1]))/(L[1]*Ro)
    KL15 = ((1-U[0])*(1-U[1])*Rco[0]*Rco[1])/(L[0]*Ro)
    KL13 = (1-U[0]*Ro_n[0])/(L[0]*Ro)
    KL26 = (1-U[1]*Ro_n[1])/(L[1]*Ro)
    A11 = np.array([[0,(-1/Ci[0]),0],[(1/L[0]),-KL12,-KL13],[0,Ro_n[0]*(1-U[0])*Ko2,-Ko1]])
    A12 = np.array([[0,0,0],[0,KL15,KL1],[0,Rco[1]*(1-U[1])*Ko1,-Ko1]])
    print(A11)
    for i in range(0,n):
        Ro = Ro+Rco[i] # Model output resistance
        Rn[i] = Rci[i]+RL[i] + Ron[i] # calculating all model input resistances
    for i in range(0,n):
        Ro_n[i] = Ro-Rco[i] # necesario paa reducir términos
        Kon = 1/(Ro*Co[i])
    #calculating params used in matrix −A and −B to calculate inductor current of each converter.
    for i in range(0,n):
        KL_n_3n_1[i] = (Rn[i]*Ro+Rco[i]*Ro_n[i]*(1-U[i]))/(L[i]*Ro)
        KL_n_3n[i] = ((1-U[i])*Ro_n[i])/(L[i]*Ro)
        KL1_3n_1[i] = ((1-U[0])*(1-U[i])*Rco[0]*Rco[i])/(L[0]*Ro)
        KL2_3n_1[i] = ((1-U[1])*(1-U[i])*Rco[1]*Rco[i])/(L[1]*Ro)
        KLn[i] = ((1-U[i])*Rco[i])/(L[i]*Ro)
        KLnI[i] = Rci[i]/L[i]
    
        


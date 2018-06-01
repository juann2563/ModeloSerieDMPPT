import numpy as np

def params(n):
    Ci = np.zeros((n,1),dtype=float)
    L = np.zeros((n,1),dtype=float)
    Co = np.zeros((n,1),dtype=float)
    Rci = np.zeros((n,1),dtype=float)
    RL = np.zeros((n,1),dtype=float)
    Rco = np.zeros((n,1),dtype=float)
    Ron = np.zeros((n,1),dtype=float)
    RB=69*np.exp(-3)
    VB = float(48)
    Rmpp = np.zeros((n,1),dtype=float)
    Vci = np.zeros((n,1),dtype=float)
    IL = np.zeros((n,1),dtype=float)
    Vco = np.zeros((n,1),dtype=float)
    equal = input("Son todos los convertidores iguales? : S(si) - N(no)")
    if equal == "S" or equal == "s":
        tipo = input("Desea aplicar los parámetros por defecto: S(si) - N(no)")
        if tipo == 'S' or tipo == 's':
            #Parámetros por defecto para el convertidor
            Ci[:,1] = 27.7*np.exp(-6)
            L[:,1] = 240*np.exp(-6)
            Co[:,1] = 27.7*np.exp(-6)
            Rci[:,1] = 6*np.exp(-3)
            Rco[:,1] = 6*np.exp(-3)
            RL[:,1] = 60*np.exp(-3)
            Ron[:,1] = 35*np.exp(-3)
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


        
        


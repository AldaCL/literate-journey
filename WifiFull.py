import numpy as np
from numpy.random import seed
from numpy.random import randint
from decimal import *
import random as rn 

#seed(1)

getcontext().prec = 8
Byt= Decimal(8)  #Size of a Byte
DIFS = Decimal(40*Byt)
SIFS =  20*Byt
Datos = 1500*Byt
Ack = 40*Byt 

Rbps = Decimal(1000) #1000kbps = 1Mbps

T_DIFS = DIFS/Rbps
    #print T_DIFS
T_SIFS = SIFS/Rbps
    #print T_SIFS
T_Datos = Datos/Rbps
    #print T_Datos
T_Ack = Ack/Rbps
    #print T_Ack

Transmisores = []
NumeroDeTxs= 50
SLargo = T_Datos + T_SIFS + T_Ack
SCorto = T_DIFS

Total_PKG = 0
Total_TIME = 0

def compare(a, b):
    return not set(a).isdisjoint(b)

class Transmisor(object):
    def __init__(self,index):
        self.index = index
        #super(Transmisor, self).__init__()
        
    
    def EB(self,times): #Exponential Backup function. 
        self.CW = 0
        maxx= np.power(2,times)
        fullWindow = range(0, 8*maxx, 1)
        CW =rn.choice(fullWindow)
        #CW = rn.choice(range(0, 16*times, 1))
        #CW = rn.randrange(0, 16*times,1)
        #print fullWindow
        #print CW
        CW_inDIFS = CW*DIFS
        #print CW_inDIFS
        Times_CW_inDIFS = CW_inDIFS/Rbps
        #print Times_CW_inDIFS
        return Times_CW_inDIFS,CW
    
EB_values = []
indexOfColisions = []

for i in range (NumeroDeTxs):
    Transmisores.append(Transmisor(i))
    time,value = Transmisores[i].EB(1)
    print time
    print value
    #print Transmisores[i].index
    #print Transmisores[i].EB(1)
    EB_values.append(value)

print  EB_values

#print ReduceEB
#EB_values = ReduceEB(EB_values)

existioCol = False
memoria = []
intentosEB = 2

for j in range (NumeroDeTxs):
    print "***********Start************"
    get_indexes = lambda EB_values, xs : [i for (y,i) in zip(xs, range(len(xs))) if EB_values==y]
    Colisiones = get_indexes(0, EB_values) #Obtiene indices de los transmisores que intentan transmitir con EB =0
    
    if len(Colisiones)==1:
        Total_TIME += SLargo
        print "Transmision hecha por el nodo" , Colisiones[0]
        print Total_TIME
        EB_values=list(map(lambda x: x - 1, EB_values))
        print EB_values
        intentosEB = 2
        memoria = []
        print "memoria en tx ", memoria

        time,value = Transmisores[Colisiones[0]].EB(intentosEB-1)
        EB_values[Colisiones[0]] =  value



    elif len(Colisiones)==0:
        print EB_values
        EB_values=list(map(lambda x: x - 1, EB_values))
        print EB_values
        memoria = []
        print "memoria en Tiempo muerto ", memoria

    else:
        #for k in range(0,len(Colisiones)+1):
        print EB_values
        print "Colisiones en RB 0 entre los Tx de indices: "
        print Colisiones
        print "Exp Bck window on start", intentosEB
        print "Loking in memory> " , memoria
        existioCol= True

        #print any(i in Colisiones for i in memoria)
        #any_in = lambda Colisiones, memoria: any(i in memoria for i in Colisiones)
        print compare(memoria,Colisiones)



        for k in Colisiones:
            print k
            #print Colisiones[k]
            if k in memoria:
            #if compare(memoria,Colisiones)==True:
            #if any(g in Colisiones for g in memoria):
                intentosEB= intentosEB +1
                print "Exp Bck window order", intentosEB
                time,value = Transmisores[k].EB(intentosEB)
                EB_values[k] =  value
                print "EB Values post colision------" , EB_values
            else:
                #print k
                time,value = Transmisores[k].EB(2)
                EB_values[k] =  value
                memoria.append(k)
                print "Memoria", memoria
                print "EB Values post colision-------", EB_values

        Transmisores[k]
    
print Colisiones
print EB_values

# for tries in range(10000000):
#     if Total_PKG ==10000:
#         break
#     else: 

        

times_array = (np.zeros((1001,6), dtype=np.dtype(Decimal)))

PromWin = 0
CW1 = 0

i=0
j=0
# for i in range (0,1000):
#     Times_CW_inDIFS,CW1 = EB(1)

#     times_array[[i],[0]] += 0  
#     times_array[[i],[1]] = times_array[[i],[0]] + T_DIFS
#     times_array[[i],[2]] = times_array[[i],[1]] + T_Datos
#     times_array[[i],[3]] = times_array[[i],[2]] + T_SIFS
#     times_array[[i],[4]] = times_array[[i],[3]] + T_Ack
#     times_array[[i],[5]] = times_array[[i],[4]] + Times_CW_inDIFS
#     times_array[[i+1],[0]] = times_array[[i],[5]]
#     PromWin +=  Decimal(CW1)


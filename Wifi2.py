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
print "Tiempo de transmision de DIFS: ", T_DIFS
T_SIFS = SIFS/Rbps
print "Tiempo de transmision de SIFS: ", T_SIFS
T_Datos = Datos/Rbps
print "Tiempo de transmision de Datos: ", T_Datos
T_Ack = Ack/Rbps
print "Tiempo de transmision de  Ack ", T_Ack
print "-------------------------------------------------------------------------------------------------------------------------"
print ""



def EB(times): #Exponential Backup function. 
    fullWindow = range(0, 16*times, 1)
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


SLargo = T_Datos + T_SIFS + T_Ack
SCorto = T_DIFS

times_array = (np.zeros((1001,6), dtype=np.dtype(Decimal)))

PromWin = 0
CW1 = 0

i=0
j=0
for i in range (0,1000):
    Times_CW_inDIFS,CW1 = EB(1)

    times_array[[i],[0]] += 0  
    times_array[[i],[1]] = times_array[[i],[0]] + T_DIFS
    times_array[[i],[2]] = times_array[[i],[1]] + T_Datos
    times_array[[i],[3]] = times_array[[i],[2]] + T_SIFS
    times_array[[i],[4]] = times_array[[i],[3]] + T_Ack
    times_array[[i],[5]] = times_array[[i],[4]] + Times_CW_inDIFS
    times_array[[i+1],[0]] = times_array[[i],[5]]
    PromWin +=  Decimal(CW1)


print times_array

R_experimental = (1000*Datos)/ times_array[999][5]
print "La velocidad de transmision promedio es : ", R_experimental
#print PromWin
PromWin = "El valor promedio de valores tomados por EB es: ", Decimal(PromWin/1000)
print PromWin
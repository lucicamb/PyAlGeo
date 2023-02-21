# File: lsistemi.py - ok
# Date: 6 gen 23
# Note: modulo di funzioni per gli L-sistemi

from kinter import *   #serve [6gen23]

# a partire dall'assioma (per ciascun suo carattere) vengono applicate
# le regole (dizionario) eseguendo la sostituzione per niter volte;
# ritorna la stringa finale
#'''
def sostituisci(assioma:str,regole:dict,niter:int) -> str:
    if not regole is None:
        for i in range(niter):
            ris = ""
            for c in assioma:
                ris = ris + regole.get(c,c) #get: se non c'e' c ritorna c
            assioma = ris
    return assioma
#'''

''' prova per sostituzioni ricorsive - ABBANDONATO
def sostituisci(assioma:str,regole:dict,niter:int) -> str:
    for i in range(niter):
        ris = ""
        for c in assioma:
            for k in regole.keys():
                if c==k:
                    ris = ris + regole.get(k)
        assioma = ris
    return assioma
'''

# traduce in disegno la stringa, applicando l'angolo di rotazione
# e disegnando un tratto al posto dei caratteri F
def disegna(stringa,angolo,passo):
    #show()
    pendown()
    for c in stringa:
        if c == '+':
            right(angolo)
        elif c == '-':
            left(angolo)
        #elif c == 'F':
        elif c in ('F','G'):
            forward(passo)
        elif c == '[':
            push()
        elif c == ']':
            pop()
        #else:
        #    print("comando errato :",b)
       
      


# File: funzioni_geo.py 
# Date: 6 giu 21
# Note: funzioni geometriche [DA INTEGRARE IN costruzioni.py]

#from oper import *
#from graph import *
#from algogeo import *
from kinter import *

_cons_color = 'gray' #colore delle costruzioni

#---------------------------------
# funzioni algoritmiche (di livello 2)

# punto medio fra due punti - ok
def medio(A,B):
    return ((A+B).config(visible=False)/2) #.config(width=3,color='red')
   
# asse di un segmento [lc]
def asse(s):
    P1 = head(s)
    P2 = tail(s)
    c1 = Circle(P1,P2).config(color=_cons_color)
    c2 = Circle(P2,P1).config(color=_cons_color)
    H = Intersection(c1,c2,1)
    K = Intersection(c1,c2,-1)
    return Line(H,K)

# retta per P e perpendicolare alla retta r
def perp(P,r):
    T = Point(RANDOM,on=r,state=VISIBLE,color=_cons_color)
    T = Point(RANDOM,name='T',on=r,state=VISIBLE,color=_cons_color)
    c = Circle(P,T,color=_cons_color)
    P1, P2 = inters(c,r)
    M = (P1+P2)/2
    s = Line(P,M,color=_cons_color,state=VISIBLE)
    return s

# piede del punto P sulla retta r
def piede(P,r):
    s = perp(P,r)
    R = inters(r,s).config(color=_cons_color,state=VISIBLE)
    return R

# simmetrico del punto P rispetto alla retta r
def simmetrico(P,r):
    S = hom(P,piede(P,r),2)
    return S

# punto simmetrico di P rispetto ad r se P e Q stanno dalla stessa parte
# altrimenti il risultato e' P stesso
def speculare(P,Q,r):
    K = hom(P,piede(P,r),2)
    stessaparte = dist(P,Q)<dist(P,K) #e' DataObject: 0.0 o 1.0
    #return K if stessaparte==0. else P #non funziona con i DO
    #return stessaparte.if3(P,K) #-16nov19
    return Cond(stessaparte,P,K)  #16nov19

# P, Q, R sono in ordine sulla stessa retta
def ordinati(P,Q,R):
    '''
    d1 = dist(P,Q)
    d2 = dist(Q,R)
    d3 = 
    ds = d1+d2
    ris = ds==
    '''
    return dist(P,Q)+dist(Q,R) == dist(P,R)

#------

# circolo di dato diametro [lc]
def circolo(A,B):  #ok
#def Circle(A,B):  #no xke richiama la classe
    return Circle(medio(A,B),dist(A,B)/2)

# circolo per 3 punti [lc]
def circolo(A,B,C):  #ok
    a1 = asse(Segment(A,B).config(color=_cons_color)).config(color=_cons_color)
    a2 = asse(Segment(B,C).config(color=_cons_color)).config(color=_cons_color)
    C = Intersection(a1,a2)
    return Circle(C,dist(C,A))

#---- COSTRUZIONI DI SECONDO LIVELLO ----

# ritorna il segmento corda intercettata dalle tg ad a dal punto esterno P
def tangentiEsterne(a:Circle,P:Point):
    C = center(a)#.config(state=VISIBLE,width=3,color='orange') 
    M = ((C+P)/2)#.config(state=VISIBLE,width=3,color='orange') 
    b = Circle(M,C)#.config(state=VISIBLE,width=1,color='red') 
    #seg = inters(c,c1).config(state=const._VISIBLE,width=1,color='red')
    S, T = inters(a,b)
    #S.config(state=VISIBLE,width=2,color='red')
    #T.config(state=VISIBLE,width=2,color='red')
    #seg = Segment(P1,P2)
    #ret = Line(O,P).config(state=const._VISIBLE,width=1,color='orange')
    #Line(P,head(seg)).config(state=const._VISIBLE,width=1,color='orange') # linea di costruzione
    #Line(P,tail(seg)).config(state=const._VISIBLE,width=1,color='orange') # ""
    #return seg
    return (S,T)
   
def asseSegmento(s):
    c1 = Circle(A,B) #.config(visible=True,width=1,color='red') 
    c2 = Circle(B,A) #.config(visible=True,width=1,color='orange')
    seg = inters(c1,c2) #.config(visible=True,width=1,color='red')
    ret = Line(head(seg),tail(seg)) #.config(visible=True,width=1,color='red')
    return ret

# non funziona: SISTEMARE 
def allineati(A,B,C):
    return Line(A,B)==Line(B,C)


    
#======================================================
if __name__ == "__main__": 

    #----------------- main -------------------
    from algogeo import *
    ag = AlgoGeo()
    ntest = 2

    if ntest==1:
        s = ag.input(const._SEGMENT).config(width=1,color='orange')
        A = head(s)
        B = tail(s)
        #M = ((A+B).config(visible=False)/2).config(width=3,color='red') #ok
        M = medio(A,B).config(width=3,color='red') #ok
        
    elif ntest==2: #asse segmento
        A = ag.input().config(name='A',width=3,color='lime green')
        B = ag.input().config(name='B',width=3,color='lime green')
        asse(Segment(A,B).config(color='orange')).config(color='red')
             
    elif ntest==3:
        A = ag.input().config(name='A',width=3,color='lime green')
        B = ag.input().config(name='B',width=3,color='lime green')
        #circolo(A,B).config(color='red',width=2)
        C = ag.input().config(name='C',width=3,color='lime green')
        circolo(A,B,C).config(color='red',width=2)
         
    else:
        print('NTEST errato in oper.py')    

   




# File: puntiretta.py - ok
# Date: 11 feb 23
# Note: operazioni sui punti di una retta - cfr. cap. Tracciare

from costruzioni import *

asse = Line(O,U).config(color='blue',state=OPERABLE,expand=True) #asse dei numeri - solleva O e U
#asse = Line(O,U).config(color='blue',state=OPERABLE,expand=False) #asse dei numeri - non solleva O e U

# funzione di conversione punto -> numero
def phi(p:Point) -> float:
    return coordx(p)

# funzione di conversione numero -> punto asse
def psi(x:float) -> Point:
    P = Point((x,0))
    return P
    #return Point(x,0)

# somma di due punti dell'asse: X1+X2
def somma(X1:Point,X2:Point) -> Point:
    #return X1 #provvisorio
    M = medio(X1,X2)
    Y = simmetrico(O,M)  #definito nel modulo costruzioni
    #Y = simmetrico(O,M).config(name='Y',color='black',state=DRAGABLE)  
    return Y

# differenza di due punti dell'asse: X1-X2
def differenza(X1:Point,X2:Point) -> Point:
    T = somma(X1,X2)
    Y = simmetrico(T,X1)  #definito nel modulo costruzioni
    return Y

# calcolo di due numeri x1+x2
def sommanum(x1:float,x2:float) -> float:
    X1 = psi(x1)
    X2 = psi(x2)
    M = medio(X1,X2)
    P = simmetrico(O,M)  #.config(name='P',color='blue',state=DRAGABLE)
    #print('type(P) =',type(P))
    #P.config(name='P',color='blue',state=DRAGABLE)
    s = phi(P)
    return s

# distanza fra due punti del piano
def distanza(A:Point,B:Point) -> float:
    c = Circle(O,A,B)#.config(color='gray',state=VISIBLE,width=THIN)
    P1, P2 = inters(c,asse)
    d = phi(P1)
    return d
 
# calcolo di sqrt(2)
def radice2() -> float:
    #global asse, O, U
    r = perp(U,asse).config(color='gray',state=VISIBLE,width=THIN)
    alfa = Circle(U,O).config(color='gray',state=VISIBLE,width=THIN)
    P, Q = inters(alfa,r)
    #P.config(color='blue',state=VISIBLE)
    #Q.config(color='red',state=VISIBLE)
    beta = Circle(O,P).config(color='gray',state=VISIBLE,width=THIN)
    R,_ = inters(beta,asse)
    R.config(color='green',state=VISIBLE)
    #Y.config(color='blue',state=VISIBLE)
    return phi(R)

# calcolo di sqrt(x)
def radice(x:float) -> float:
    global O
    X = psi(x)
    Q = somma(X,U)
    Q.config(name='Q',color='red',state=VISIBLE)
    M = medio(O,Q)  
    r = perp(X,asse)
    r.config(color='red',state=VISIBLE,width=THIN)
    a = Circle(M,O).config(color='red',state=VISIBLE,width=THIN)
    R1,R2 = inters(a,r)
    R1.config(color='blue',state=VISIBLE)
    R2.config(color='blue',state=VISIBLE)

    ''' versione 1/2 - ok, 
    #rad = dist(X,R1)      #ok, ma usa dist (versione 1)
    rad = distanza(X,R1)   #ok (versione 2)
    
    #write('O=',O)
    #write('X=',X)
    #write('R1=',R1)
    '''
          
    #''' versione 3 - ok
    b = Circle(O,X,R1) 
    #b.config(color='red',state=VISIBLE,width=MEDIUM) 
    S1,S2 = inters(b,asse)
    radx = phi(S1)
    #'''
    
    ''' versione 4 - ok ma lenta - 25gen23
    b = Circle(X,R1).config(color='red',state=VISIBLE,width=THIN)
    S1,S2 = inters(b,asse)
    T = differenza(S1,X)
    #T.config(name='T',color='red',state=VISIBLE)
    rad = phi(T)
    '''
         
    return radx
    
    

#---- main ----

'''
#funzione phi
x = 3.1415
X = phi(x)
X.config(color='red',state=VISIBLE)
'''


'''
#---- somma(x1,x2) e diff(x1,x2) ---- ok 11feb23
mes = "seleziona un punto sull'asse ..."
X1 = Point(INPUT,msg=mes,on=asse,color='green',state=DRAGABLE)
X2 = Point(INPUT,msg=mes,on=asse,color='green',state=DRAGABLE)
show('X1=',X1)  
show('X2=',X2)
show('phi(X1)=',phi(X1))  
show('phi(X2)=',phi(X2))

# somma di due punti
S = somma(X1,X2)
S.config(color='orange',state=VISIBLE)
show('S=',S)
s = phi(S)
show('somma=',s)

# differenza di due punti
D = differenza(X1,X2) 
D.config(color='red',state=VISIBLE)
show('D=',D)
d = phi(D)
show('diff=',d)

#somma di due numeri:
x1 = 1.234
x2 = 5.345
s = sommanum(x1,x2)
show('x1+x2 = ',s)
show('x1+x2+100 = ',sommanum(s,100))
'''


'''
#---- radice(2) ---- ok 11feb23
x = radice2()
print('x=',x)
show('radice(2)=',radice2())

#---- radice(x) ---- ok ma un po' lento in drag - 11feb23
X = Point(INPUT,on=asse,color='green',state=DRAGABLE)     
x = abs(phi(X))
r = radice(x)
#x.debug('radice di X')
show('x=',x)
show('radice(x)=',r)    
#Text((5,5),"radice({0})={1}",[x,r],color='brown').config(state=DRAGABLE) #...
Writing((80,70),"radice({0})={1}",variables=[x,r],color='brown').config(state=DRAGABLE) #...
#X.dump()
'''
 
 
#'''
# distanza fra due punti del piano (usando phi e psi) - ok 11feb23
A = Point(3,4,name='A',color='green',state=DRAGABLE)
B = Point(1,-2,name='B',color='blue',state=DRAGABLE)
d = distanza(A,B)
show('dist(A,B)=',d)
#'''



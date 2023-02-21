# File: costruzioni.py - ok
# Date: 1 feb 23 
# Note: costruzioni con riga&compasso [cfr. cap. 31]

from kinter import *   #serve [16set21]

_cons_color = 'gray'   # colore delle linee di costruzione
_cons_width = 1        # spessore delle linee di costruzione
_cons_state = VISIBLE  # stato delle linee di costruzione
#_cons_state = INVISIBLE  # stato delle linee di costruzione

esterna = 123 #prova
def ciaox(): print('---------- CIAO DA costruzioni.py -----------')


# asse di un segmento
# cfr. Alg. asse - cap. Punteggiare
def asse(A:Point,B:Point) -> Line:
    global _cons_color
    alfa = Circle(A,B,color=_cons_color,width=_cons_width,state=_cons_state)
    beta = Circle(B,A,color=_cons_color,width=_cons_width,state=_cons_state)
    P, Q = inters(alfa,beta)
    a = Line(P,Q,color=_cons_color,width=_cons_width,state=_cons_state)
    return a

# punto medio fra due punti
# cfr. Alg. medio - cap. Punteggiare
def medio(A:Point,B:Point) -> Point:
    a = asse(A,B).config(color=_cons_color,state=_cons_state)
    r = Line(A,B,color=_cons_color,state=_cons_state,width=_cons_width)
    M = inters(a,r)
    return M 

# simmetrico del punto A rispetto al punto B
def simmetrico(A:Point,B:Point) -> Point:
     
    #S = CondPoint(equal(A,B),A,inters(Line(A,B),Circle(B,A))[0]) #ok 24gen23

    K = inters(Line(A,B),Circle(B,A))[0]
    #S = CondPoint(equal(A,B),A,K) #ok 26gen23
    S = CondPoint(A==B,A,K) #ok 26gen23
    #S = A if A==B else K  #no 26gen23
    
    return S

# retta per il punto A e perpendicolare alla retta r;
# funziona anche nel caso in cui A stia su r
def perp(A:Point,r:Line) -> Line:
    Q = Point(RANDOM,on=r) #,state=_cons_state,color=_cons_color)
    c = Circle(A,Q).config(color=_cons_color,width=_cons_width,state=_cons_state)
    P1, P2 = inters(c,r)  #deve essere P1 != P2
    s = asse(P1,P2)
    s.config(color=_cons_color,width=_cons_width,state=_cons_state) #,expand=False)
    return s

# retta per il punto A e parallela alla retta r
def paral(A:Point,r:Line) -> Line:
    s = perp(A,perp(A,r))
    s.config(color=_cons_color,width=_cons_width,state=_cons_state) #,expand=False)
    return s

# piede del punto P sulla retta r
def piede(P:Point,r:Line) -> Point:
    t = perp(P,r)
    T = inters(t,r)
    return T

# circonferenza passante per 3 punti
def circonf3punti(A:Point, B:Point, C:Point) -> Circle:
#def Circle(A:Point, B:Point, C:Point) -> Circle:
    a1 = asse(A,B)
    a2 = asse(B,C)
    T = inters(a1,a2)
    g = Circle(T,dist(T,A))
    return g

# centro circonferenza passante per 3 punti
def centrocirconf3punti(A:Point, B:Point, C:Point) -> Circle:
    a1 = asse(A,B)
    a2 = asse(B,C)
    T = inters(a1,a2)
    return T

# centro di una circonferenza c (equivale alla center(c))
# cfr. Alg. ... cap. Tracciare
def centro(c:Circle) -> Point:
    global _cons_color
    P = Point(RANDOM,on=c) #,color=_cons_color,state=_cons_state)
    Q = Point(RANDOM,on=c) #,color=_cons_color,state=_cons_state)
    R = Point(RANDOM,on=c) #,color=_cons_color,state=_cons_state)
    C = centrocirconf3punti(P,Q,R)
    return C

# diametro di a passante per A
def diametro(a:Circle,A:Point) -> Segment:
    C = centro(a)
    r = Line(A,C)
    P, Q = inters(r,a)
    s = Segment(P,Q)
    return s

# tangenti alla circonferenza a condotte per il punto esterno P
# cfr. par. Costruzioni nel cap. PUNTEGGIARE
def tangenti(a:Circle,P:Point):
    C = centro(a)#.config(state=VISIBLE,color=_cons_color) 
    M = medio(C,P)#.config(state=VISIBLE,color=_cons_color) 
    #b = Circle(M,C).config(state=VISIBLE,color=_cons_color,width=_cons_width,expand=False) 
    b = Circle(M,C).config(state=VISIBLE,color=_cons_color,width=_cons_width)       
    S, T = inters(a,b)
    return (S,T)



#'''
#prova per test di visibilita'
def ciao(nome:str):
    print('*************** ciao ',nome,' da costruzioni.py ******************')
#'''

#print('----------- in COSTRUZIONI 0 -------------')
#---- main ----

'''
#-- asse -- ok 24gen23  
#A = Point(1,0,name='A',color='blue',state=DRAGABLE)
#B = Point(3,0,name='B',color='green',state=DRAGABLE)
#a = asse(A,B).config(color='red',name='a',state=VISIBLE)
s = "seleziona un segmento ed io ti trovo l'asse"
s = Segment(INPUT,msg=s,color='red',state=DRAGABLE)
s.config(name='s')
M = head(s)    
N = tail(s)
M.config(color='blue',name='M') 
N.config(color='orange',name='N') 
write('dist(M,N) = ',dist(M,N))
a = asse(M,N).config(color='blue',state=SENSIBLE)  
a.config(name='asse',color='blue',state=SENSIBLE) # rende SENSIBILI anche i punti
write('a=',a)
'''


'''
#-- punto medio 1 -- ok 15gen23  
mes = 'seleziona punto A...'
A = Point(INPUT,msg=mes,name='A',color='blue',state=DRAGABLE)
mes = 'seleziona punto B...'
B = Point(INPUT,msg=mes,name='B',color='green',state=DRAGABLE)
M = medio(A,B).config(color='red',name='M',state=VISIBLE)
write('M=',M)
'''

'''
#-- punto medio 2 -- ok 14ott22  
ax = Line(O,U).config(color='blue',state=OPERABLE,expand=True) #asse dei numeri - solleva O e U
write('ax=',ax)
A = Point(INPUT,on=ax,color='green',state=DRAGABLE)
B = Point(INPUT,on=ax,color='green',state=DRAGABLE)
write('A=',A) 
write('B=',B)
M = medio(A,B).config(color='red',name='M',state=VISIBLE)
#write('M=',M)
'''


'''
#-- simmetrico di un punto rispetto ad un altro -- ok 26gen23 
#mes = 'seleziona punto A...'
#A = Point(INPUT,msg=mes,name='A',color='red',state=DRAGABLE)
#mes = 'seleziona punto B...'
#B = Point(INPUT,msg=mes,name='B',color='brown',state=DRAGABLE)
A = Point(1,2,name='A',color='blue',state=DRAGABLE)
B = Point(1,2,name='B',color='black',state=DRAGABLE)   #ok anche cosi'
#B = Point(4,3,name='B',color='black',state=DRAGABLE)  #ok
C = simmetrico(A,B).config(color='red',state=VISIBLE)
write('A=',A)
write('B=',B)
write('C=',C)
'''    


'''
# retta per un punto P perp/paral alla retta r:   ok 24gen23
# caso 1: P sta su r
# caso 2: P non sta su r
A = Point(1,1,name='A',color='blue',state=DRAGABLE)
B = Point(5,3,name='B',color='blue',state=DRAGABLE)
#P = Point(INPUT,msg='B?',color='blue',state=DRAGABLE)
r = Line(A,B,color='orange',state=DRAGABLE)
#P = Point(INPUT,on=r,msg='P?').config(name='P',color='green',state=DRAGABLE) #caso 1
P = Point(INPUT,msg='P?').config(name='P',color='green',state=DRAGABLE)       #caso 2
s = perp(P,r)
t = paral(P,r)
s.config(color='red',state=VISIBLE,width=MEDIUM)
t.config(color='brown',state=VISIBLE,width=MEDIUM)
'''

'''
# centro circonferenza passante per 3 dati punti - ok 24gen23
A = Point(1,1,name='A',color='blue',state=DRAGABLE)
B = Point(5,3,name='B',color='blue',state=DRAGABLE)
C = Point(3,-2,name='C',color='blue',state=DRAGABLE)
#alfa = Circle((A,B,C),color='red',state=DRAGABLE)  #ok
alfa = circonf3punti(A,B,C).config(color='orange',state=DRAGABLE)
centro = centrocirconf3punti(A,B,C)
centro.config(color='red',state=VISIBLE)
'''


'''
# diametro per A - ok 25gen23
C = Point(1,1,name='C',color='green',state=DRAGABLE)
a = Circle(C,Point(3,4),color='red',state=DRAGABLE,width=MEDIUM)
A = Point(RANDOM,on=a,name='A',color='blue',state=DRAGABLE)
s = diametro(a,A)
s.config(color='brown',state=VISIBLE,width=MEDIUM)
'''


'''
#tangenti ad una circ condotte da un punto esterno - ok 25gen23
C = Point(1,1,name='C',color='green',state=DRAGABLE)
a = Circle(C,Point(3,4),color='red',state=DRAGABLE,width=MEDIUM)
P = Point(6,2,name='P',color='blue',state=DRAGABLE)
S,T = tangenti(a,P)
S.config(color='green',width=3)
T.config(color='green',width=3)
t1 = Line(P,S,color='blue',state=VISIBLE)
t2 = Line(P,T,color='blue',state=VISIBLE)
write('t1 = ',t1)
write('t2 = ',t2)
'''    


############# sistemare da qui in poi [25gen23] ############


'''
#-- perpendicolare e piede di un punto -- ok 30ott22  
mes = 'seleziona punto...'
A = Point(INPUT,msg=mes,name='A',color='red',state=DRAGABLE)
B = Point(INPUT,msg=mes,name='B',color='brown',state=DRAGABLE)
r = Line(A,B,color='red',state=DRAGABLE,width=MEDIUM)
C = Point(INPUT,msg=mes,name='B',color='brown',state=DRAGABLE)
#p = perp(C,r).config(color='blue',state=VISIBLE)
T = piede(C,r).config(color='blue',state=VISIBLE)
'''


'''
#test perp - ok
A = Point(3,4,color='red',state=DRAGABLE)
t = Line(Point(1,3,color='red',state=DRAGABLE),Point(4,-1,color='red',state=DRAGABLE),color='red',state=DRAGABLE,width=MEDIUM)
p = perp(A,t)
#p = perp(A,asse)
r = Line(O,U,name='r',color='orange',state=OPERABLE) 
#print('type(p)=',type(p))
#print('type(r)=',type(r))
p.config(color='blue',state=DRAGABLE,width=MEDIUM)
write('p=',p)
write('r=',r)
'''

'''
#test paral - ok
A = Point(3,4,color='red',state=DRAGABLE)
t = Line(Point(1,3,color='red',state=DRAGABLE),Point(4,-1,color='red',state=DRAGABLE),color='red',state=DRAGABLE,width=MEDIUM)
p = paral(A,t)
p.config(color='red',state=VISIBLE,width=MEDIUM)
'''



'''
#-- punto medio+simmetrico+dist -- ok 30ott22  
#c = Circle(Point(1,2,color='blue',state=DRAGABLE),4,state=DRAGABLE,color='green') #blue e draggabile
c = Circle(Point((1,2),color='blue',state=DRAGABLE),3,state=DRAGABLE,color='green') #blue e draggabile
mes = 'seleziona punto A...'
A = Point(INPUT,on=c,msg=mes,name='A',color='blue',state=DRAGABLE)
mes = 'seleziona punto B...'
B = Point(INPUT,on=c,msg=mes,name='B',color='brown',state=DRAGABLE)
d = dist(A,B)
write('dist(A,B)=',d)
write('uguali(A,B)=',equal(A,B))
M = medio(A,B).config(color='red',state=VISIBLE)
write('uguali(A,M)=',equal(A,M))
C = simmetrico(M,O).config(color='green',state=VISIBLE)
D = simmetrico(O,M).config(color='orange',state=VISIBLE)
'''


'''
#-- simmetrico di un punto rispetto ad una retta -- DA COMPLETARE  
mess = 'seleziona la retta...'
r = Line(INPUT,msg=mess,name='r',color='brown',state=DRAGABLE,width=MEDIUM)
mess = 'seleziona un punto...' 
P = Point(INPUT,msg=mess,name='P',color='blue',state=DRAGABLE)
Q = Point(INPUT,msg=mess,name='P',color='green',state=DRAGABLE)
R = simm(P,Q)
'''

 
'''
message('seleziona un punto ...')
P = Point(INPUT,name='P',color='red',state=DRAGABLE)
Q = Point(INPUT,name='Q',color='red',state=DRAGABLE)
message('') #clear
a = asse(P,Q)
a.config(color='brown',state=VISIBLE)
'''

'''
message('seleziona un punto ...')
P = Point(INPUT,name='P',color='red',state=DRAGABLE)
Q = Point(INPUT,name='Q',color='red',state=DRAGABLE)
message('') #clear
M = medio(P,Q) 
M.config(name='M',color='brown',state=VISIBLE) #ERR: non viene ridimensionato
'''

'''
#-- centro circonferenza -- ok 30ott22
s = 'seleziona una circonferenza ...'
c = Circle(INPUT,msg=s,color='red',state=DRAGABLE)
#c = Circle(INPUT,msg=s,color='red',state=VISIBLE)
C = centro(c)
C.config(color='blue',state=VISIBLE)
'''
 


# File: rettaxcirc - ok 
# Date: 11 feb 23
# Note: intersezione retta-circ con il solo uso del compasso 
 
# intersezione retta AB - circonferenza centro C e passante per P - ok
# usando solo il compasso molle
# funziona solo se A!=B ed il centro C non sta sulla retta AB la retta non passa per il centro - SISTEMARE
# return: coppia di punti intersezione
def rettaxcirc(A:Point, B:Point, C:Point, P:Point) -> tuple:
    #if equal(A,B): return (None,None)  #MA COSI' VIENE VALUTATO SOLO UNA VOLTA E ERR IN DRAG!!!
    alfa = Circle(A,C).config(name='a',state=DRAGABLE,width=THIN,color='black')
    beta = Circle(B,C).config(name='b',state=DRAGABLE,width=THIN,color='blue')
    F,E = inters(alfa,beta)
    
    F.config(name='F',state=VISIBLE,color='gray')
    E.config(name='E',state=VISIBLE,color='gray')
    show('A =',A)  #debug
    show('B =',B)  #debug
    show('C =',C)  #debug
    show('F =',F)  #debug
    show('E =',E)  #debug
    Line(A,B,color='orange',state=DRAGABLE,width=THIN) #debug
    
    #T = E if equal(F,C) else F #cosi' non va perche' non e' dinamica!!
    #T = CondPoint(equal(F,C),E,F)  #cosi' ok! [26gen23]
    T = CondPoint(F==C,E,F)  # anche cosi' ok! [26gen23]
    gamma = Circle(T,C,P).config(name='c',state=DRAGABLE,width=THIN,color='orange') 

    #k = equal(F,C) #debug
    #show('k=',k)  #debug
    #show('T=',T)  #debug
    
    delta = Circle(C,P).config(name='d',state=DRAGABLE,width=THIN,color='orange')
    show('gamma=',gamma)
    show('delta=',delta)
    H,K = inters(gamma,delta)
    #show('h=',H)
    #show('k=',K)
    return H,K

#---- main ----
# non funziona se il punto C sta su AB - serve altro procedimento [*]
A = Point(INPUT,msg='A?',name='A',color='blue',state=DRAGABLE)
B = Point(INPUT,msg='B?',name='B',color='blue',state=DRAGABLE)
Line(A,B,color='gray',state=DRAGABLE,width=MEDIUM) #debug visivo
C = Point(INPUT,msg='C?',name='C',color='blue',state=DRAGABLE)   
#C = med(A,B).config(name='C',color='blue',state=DRAGABLE) #[*]  questo caso non va
P = Point(INPUT,msg='P?',name='P',color='blue',state=DRAGABLE)
Circle(C,P,color='gray',state=DRAGABLE,width=MEDIUM) #debug visivo

H,K = rettaxcirc(A,B,C,P) 
H.config(name='H',state=DRAGABLE,color='red')
K.config(name='K',state=DRAGABLE,color='red')
show('H=',H)
show('K=',K)






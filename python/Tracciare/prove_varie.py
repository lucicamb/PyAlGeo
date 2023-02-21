# File: prove_varie - 
# Date: 11 feb 23
# Note: problema con il solo uso del compasso - SCORPORARE GLI ESEMPI!!!
 
# intersezione retta AB - circonferenza centro C e passante per P
# (portata in rettaxcirc.py;
# E' QUI SOLO PER TESTARE L'ESEMPIO simmetric CHE SEGUE
# return: coppia di punti intersezione
def rettaxcirc(A:Point, B:Point, C:Point, P:Point) -> tuple:
    #if equal(A,B): return (None,None)  #MA COSI' VIENE VALUTATO SOLO UNA VOLTA E ERR IN DRAG!!!
    a = Circle(A,C).config(name='a',state=DRAGABLE,width=THIN,color='black')
    b = Circle(B,C).config(name='b',state=DRAGABLE,width=THIN,color='blue')
    F,E = inters(a,b)
    
    F.config(name='F',state=VISIBLE,color='red')
    E.config(name='E',state=VISIBLE,color='red')
    write('A =',A)  #debug
    write('B =',B)  #debug
    write('C =',C)  #debug
    write('F =',F)  #debug
    write('E =',E)  #debug
    Line(A,B,color='orange',state=DRAGABLE,width=THIN) #debug
    
    #T = E if equal(F,C) else F #cosi' non va perche' non e' dinamica!!
    T = CondPoint(equal(F,C),E,F)  #cosi' ok!!!!
    c = Circle(T,C,P).config(name='c',state=DRAGABLE,width=THIN,color='orange') 
    k = equal(F,C) #debug
    write('k=',k)  #debug
    write('T=',T)  #debug
    
    d = Circle(C,P).config(name='d',state=DRAGABLE,width=THIN,color='orange')
    write('c=',c)
    write('d=',d)
    H,K = inters(c,d)
    #write('h=',H)
    #write('k=',K)
    return H,K

# return: simmetrico del punto A rispetto al punto B
def simmetric(A:Point, B:Point) -> Point:
    #a = Circle(A,B).config(name='a',state=DRAGABLE,width=THIN,color='black')
    #C1, C2 = rettaxcirc(A,B,a)  #meglio cosi'?
    C1, C2 = rettaxcirc(A,B,B,A)
    write('C1=',C1)
    write('C2=',C2)
    S = CondPoint(equal(A,C1),C2,C1)
    return S
 
# inverso del punto P rispetto al cerchio c di centro C
# SE P E' VICINO AL CENTRO BISOGNA CAMBIARE PROCEDIMENTO (cfr. Note pdf)
def inverso(P:Point,c:Circle) -> Point:
    C = center(c)
    a = Circle(P,C).config(color='orange',state=DRAGABLE,width=THIN)
    D, E = inters(a,c)
    D.config(name='D',color='green',state=VISIBLE) 
    E.config(name='E',color='green',state=VISIBLE)
    a1 = Circle(D,C).config(color='gray',state=DRAGABLE,width=THIN)
    a2 = Circle(E,C).config(color='gray',state=DRAGABLE,width=THIN)
    F, G = inters(a1,a2)
    K = CondPoint(equal(F,C),G,F)
    return K
    

#---- main ----

''' 
#-- intersezione retta-circonferenza -- ok 8nov22 (non in tutti i casi - serve altro procedimento)
A = Point(INPUT,msg='A?',name='A',color='blue',state=DRAGABLE)
B = Point(INPUT,msg='B?',name='B',color='blue',state=DRAGABLE)
Line(A,B,color='gray',state=DRAGABLE,width=THIN) #debug visivo
C = Point(INPUT,msg='C?',name='C',color='blue',state=DRAGABLE)
P = Point(INPUT,msg='P?',name='P',color='blue',state=DRAGABLE)
Circle(C,P,color='gray',state=DRAGABLE,width=THIN) #debug visivo

H,K = rettaxcirc(A,B,C,P) 
H.config(name='H',state=DRAGABLE,color='red')
K.config(name='K',state=DRAGABLE,color='red')
write('H=',H)
write('K=',K)

# il caso che segue non funziona; serve altro procedimento
#C1, C2 = rettaxcirc(A,B,B,A)
#write('C1=',C1)
#write('C2=',C2)
'''


'''
#-- inverso di un punto rispetto ad una circonferenza -- ok 8nov22
c = Circle(INPUT,color='blue',state=DRAGABLE,width=MEDIUM)
P = Point(INPUT,msg='P?',name='P',color='blue',state=DRAGABLE)
K = inverso(P,c).config(color='red',state=VISIBLE)
'''


''' 
#-- simmetrico di A rispetto a B -- ok 5nov22
A = Point(INPUT,msg='A?',name='A',color='blue',state=DRAGABLE)
B = Point(INPUT,msg='B?',name='B',color='blue',state=DRAGABLE)
#S = simmetric(A,B)
#S.config(name='S',state=DRAGABLE,color='red')


C1, C2 = rettaxcirc(A,B,B,A)
write('C1=',C1)
write('C2=',C2)
#    S = CondPoint(equal(A,C1),C2,C1)
'''


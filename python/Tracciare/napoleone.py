# File: napoleone.py - ok
# Date: 11 feb 23
# Note: problema di Napoleone 

# centro della circonferenza c, usando tracciamenti di sole circ.
# [problema di Napoleone]
#
# TRASCINANDO A SI VERIFICANO CONDIZIONI CHE NON HANNO INTERSEZIONI - SISTEMARE
# FUNZIONA SOLO SE A e T SONO ABBASTANZA LONTANI (> 30 gradi?);
# corrisponde al caso in cui non esiste l'inters che genera E, F
#
# corrispondenze dei nomi delle circ. con articolo Odifreddi:
# beta-c1 gamma-c2 delta-c3 gamma-c4
def napoleone(alfa:Circle) -> Point:
    A = Point(RANDOM,on=alfa,name='A',color='green',state=DRAGABLE)
    #T = Point(RANDOM,on=alfa,name='T',color='blue',state=INVISIBLE)
    T = Point(RANDOM,on=alfa,name='T',color='blue',state=DRAGABLE)

    #beta = Circle(A,dist(A,T)).config(name='c1',state=const.DRAGABLE,width=1,color='orange')
    #beta = Circle(A,T).config(name='c1',state=const.DRAGABLE,width=1,color='orange') #ok ma A diventa orange
    beta = Circle(A,T,name='c1',state=const.DRAGABLE,width=1,color='orange') #A rimane red

    B, C = inters(alfa,beta)
    #B.config(name='B',color='red',width=13,state=VISIBLE) #width ininfluente
    #C.config(name='C',color='red',width=3,state=VISIBLE)

    #gamma = Circle(B,A).config(name='c2',state=const.VISIBLE,width=1,color='green') #blocca A
    #delta = Circle(C,A).config(name='c3',state=const.VISIBLE,width=1,color='green')
    #gamma = Circle(B,A).config(name='c2',state=const.VISIBLE,width=1,color='green',expand=False) #False per non bloccare A
    #deltac3 = Circle(C,A).config(name='c3',state=const.VISIBLE,width=1,color='green',expand=False)
    gamma = Circle(B,A,name='c2',state=const.VISIBLE,width=THIN,color='green') 
    delta = Circle(C,A,name='c3',state=const.VISIBLE,width=THIN,color='green')

    D1, D2 = inters(gamma,delta)  #sistemare l'ordine

    #D = D1 if dist(A,D1) > dist(A,D2) else D2
    #D = D1 if equal(A,D2) else D2  #sembra ok 26gen23

    #D = D1 if A==D2 else D2  # anche cosi' [perche'?]
    D = CondPoint(A==D2,D1,D2)  #ok
    
    #D.config(name='D',color='green',width=3,state=VISIBLE)
    D.config(name='D',color='brown',state=VISIBLE)

    eta = Circle(D,A,name='c4',state=const.VISIBLE,width=1,color='brown') 

    E, F = inters(beta,eta)
    #E.config(name='E',color='black',state=VISIBLE)
    #F.config(name='F',color='black',state=VISIBLE)
    ni = Circle(E,A,name='c5',state=const.VISIBLE,width=1,color='pink')
    theta = Circle(F,A,name='c6',state=const.VISIBLE,width=1,color='pink')
    G1, G2 = inters(ni,theta)
 
    #G = G1 if dist(A,G1) > dist(A,G2) else G2
    #G = G1 if equal(A,G2) else G2  #sembra ok 26gen23 VELOCE!

    #G = G1 if A==G2 else G2  # anche cosi' [perche'?]
    G = CondPoint(A==G2,G1,G2)  #ok  

    G.config(color='red',state=SENSIBLE)

    show('punto A = ',A)
    show('punto B = ',B)
    show('punto C = ',C)
    show('punto D = ',D)
    show('punto E = ',E)
    show('punto F = ',F)
    show('punto G = ',G)
    return G

 
#-- problema di Napoleone -- ok 25nov22
# DRAGANDO PUNTO A, QUANDO c1 non interseca piu' c4, il centro diventa indefinito - SISTEMARE!!
c = Circle(Point((1,2)),1.8).config(name='c',state=const.DRAGABLE,width=2,color='black')
C = napoleone(c)
C.config(color='blue',state=VISIBLE)
Text((0,-2),"trascinare il punto A",color='black',state=DRAGABLE)
Text((0,-3),"centro del cerchio c = [{0},{1}]",[coordx(C),coordy(C)],color='black').config(state=DRAGABLE)




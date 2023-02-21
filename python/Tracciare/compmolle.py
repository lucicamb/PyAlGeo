# File: compmolle.py - ok
# Date: 11 feb 23
# Note: problema del compasso molle

# circonferenza di centro C e raggio AB - ok 18ott22
# usando solo il compasso molle
def circompmolle(C:Point, A:Point, B:Point) -> Circle:
    alfa = Circle(A,C).config(name='a',state=DRAGABLE,width=1,color='black')
    beta = Circle(C,A).config(name='b',state=DRAGABLE,width=1,color='blue')
    D, E = inters(alfa,beta)
    delta = Circle(D,B).config(name='d',state=DRAGABLE,width=1,color='brown')
    eta = Circle(E,B).config(name='e',state=DRAGABLE,width=1,color='gray')
   
    H,K = inters(delta,eta)
  
    ''' mantenere per debug
    H.config(name='H',width=1,color='blue')
    K.config(name='K',width=1,color='blue')
    show('punto D di intersezione = ',D)
    show('punto E di intersezione = ',E)
    show('H=',H)
    show('K=',K)
    dab = dist(A,B)
    dch = dist(C,H)
    dck = dist(C,K)
    dh = abs(dist(C,H)-dist(A,B))
    dk = abs(dist(C,K)-dist(A,B))
    show('dist(A,B)=',dab)
    show('dist(C,H)=',dch)
    show('dist(C,K)=',dck)
    show('dist(C,H)-dist(A,B)=',dh)
    show('dist(C,K)-dist(A,B)=',dk)
    #q = (dist(C,A)-dist(A,B))<.2
    #q = dh<dk  #ok
    '''
    
    q = dist(A,B)==dist(C,H) #29set22:ok
    show('Q=',q)
    #T = H if B==H else K  # logica errata - prova del 29set22
    T = CondPoint(q,H,K)  # punto condizionale 
    #show('T=',T) #ERR: cambia i nomi in visualizzazione
    
    gamma = Circle(C,T).config(name='c',state=DRAGABLE,width=1,color='red')
    return gamma

#-- problema del compasso molle -- ok 26gen23
mess = 'seleziona il segmento-raggio della circonferenza...'
s = Segment(INPUT,msg=mess,name='s',color='orange',state=DRAGABLE)
A = head(s)
A.config(name='A',state=DRAGABLE,color='green')
B = tail(s)
B.config(name='B',state=DRAGABLE,color='green')
mess = 'seleziona il centro della circonferenza...'
C = Point(INPUT,msg=mess,name='C',color='blue',state=DRAGABLE)
alfa = circompmolle(C,A,B) 
#alfa.config(color='red',state=SENSIBLE,width=MEDIUM) #,expand=False)
alfa.config(color='red',state=DRAGABLE,width=MEDIUM) #,expand=False)
#alfa.dump('circ compasso:')



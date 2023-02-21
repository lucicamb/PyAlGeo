# File: colleg_min.py - ok
# Date: 11 feb 23 
# Note: collegamento minimo Punto-Retta-Punto 
#       (anche come test per oggetti condizionali)

from costruzioni import * #piede 

grid()

s = 'seleziona una retta ...'
r = Line(INPUT,msg=s,name='r',color='blue',state=DRAGABLE)
s = 'seleziona un punto ...'
P = Point(INPUT,msg=s,name='P',color='blue',state=DRAGABLE)
s = 'seleziona un altro punto ...'
Q = Point(INPUT,msg=s,name='Q',color='blue',state=DRAGABLE)

#S = speculare(P,Q,r).config(color='red',name='S',width=3,state=VISIBLE)
K = hom(Q,piede(Q,r),2) #speculare di Q rispetto a r - usare simm
#K.config(name='K',width=3,color='brown',state=VISIBLE) #inibire il width=3

K.config(name='K',color='brown',state=VISIBLE)

stessaparte = dist(P,Q)<dist(P,K) #e' DataObject (True,False)
show('stessaparte=',stessaparte)
print('stessaparte =',stessaparte)
s = Line(P,K,width=1,color='blue',name='s',state=VISIBLE)
show('s=',s)

M = Intersection(r,s,name='M',color='brown',state=SENSIBLE)
#M = Intersection(r,s,name='M',color='brown',state=DRAGABLE)

#T = M if stessaparte else P # NON COSI': T deve essere dinamico
T = CondPoint(stessaparte,M,P) #punto condizionale  ok 26gen23

#---- zona di prova 
#Circle(T,M,color='green',state=VISIBLE,width=MEDIUM) #T si sovrappone a P ed inibisce i drag
##Circle(T,M,color='green',state=DRAGABLE,width=MEDIUM) #il problema rimane
#Segment(T,M,color='green',state=VISIBLE,width=MEDIUM) #per test: ok
#Ray(T,M,color='green',state=VISIBLE,width=MEDIUM) #per test: ok
d1 = dist(T,M)
d2 = T.dist(M)

#''' rimettere le show
show('d1=',d1)
show('d2=',d2)
show('M=',M) 
show('P=',P)
show('Q=',Q)
show('T=',T)
#'''

#s1 = Segment(P,T,width=2,color='red',state=VISIBLE)
#s1 = Segment(P,T,color='red',state=VISIBLE)
s1 = Segment(P,T,color='red',width=3,state=SENSIBLE)
show('s1=',s1)   #rimettere
#s2 = Segment(T,Q,color='red',state=VISIBLE)
s2 = Segment(T,Q,color='red',width=3,state=SENSIBLE)

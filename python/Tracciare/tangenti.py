# File: tangenti.py - ok
# Date: 11 feb 23 
# Note: modulo che importa il modulo 'costruzioni.py'

from costruzioni import * 

#_cons_color = 'gray' # colore delle linee di costruzione


'''
#tangenti esterne ad una circonferenza per un punto [metodo 1] - ok 11feb23
mes = 'seleziona una circonferenza...'
a = Circle(INPUT,msg=mes,color='blue',name='a',state=DRAGABLE)
show('circ a = ',a)  
C = center(a)
mes = 'seleziona un punto esterno ...'
P = Point(INPUT,msg=mes,color='blue',name='P',state=DRAGABLE)
M = med(P,C)
D = pointOn(a)
#S,T = cxc(M,P,C,D)  #ok
S,T = inters(Circle(M,P),Circle(C,D))  #ok
S.config(color='orange',state=DRAGABLE)
T.config(color='orange',state=DRAGABLE)
Line(P,S,color='orange',state=DRAGABLE)
Line(P,T,color='orange',state=DRAGABLE)
'''


#'''
#-- tangenti ad una circ condotte da un punto esterno [metodo 2] -- ok 11feb23
s = 'seleziona una circonferenza ...'
c = Circle(INPUT,msg=s,color='red',width=MEDIUM,state=DRAGABLE)
s = 'seleziona un punto esterno ...'
P = Point(INPUT,msg=s,name='P',color='red',state=DRAGABLE)
S,T = tangenti(c,P)  #nel modulo costruzioni
S.config(color='green',state=VISIBLE)
T.config(color='green',state=VISIBLE)
#t1 = Line(P,S,color='blue',state=VISIBLE)
#t2 = Line(P,T,color='blue',state=VISIBLE)
t1 = Line(P,S,color='blue',state=SENSIBLE)
t2 = Line(P,T,color='blue',state=SENSIBLE)
show('t1 = ',t1)
show('t2 = ',t2)
#setmode(const._DRAG)  #non visibile
#'''



'''
#-- tangenti esterne a 2 circonferenze -- ok 11feb23
mes = 'seleziona una circonferenza ...'
c1 = Circle(INPUT,msg=mes,color='blue',name='c1',state=DRAGABLE)
show('circ c1 = ',c1)  
c2 = Circle(INPUT,msg=mes,color='blue',name='c2',state=DRAGABLE)
show('circ c2 = ',c2) 
C1 = center(c1)
C2 = center(c2)
r1 = radius(c1)
r2 = radius(c2)
show('C1 = ',center(c1))
show('C2 = ',center(c2))
show('radius c1 = ',r1)
show('radius c2 = ',r2)
d = dist(C1,C2)
x = (r1*d)/(r2-r1)
show('x = ',x)
#P = oltre(C2,C1,x)  #ok
P = hom(C2,C1,1+x*~dist(C1,C2))   # ~ e' l'inverso (alla -1)
P.config(color='red',state=DRAGABLE)
show('P = ',P)
S, T = tangenti(c1,P)
t1 = Line(P,S,color='blue',state=SENSIBLE)
t2 = Line(P,T,color='blue',state=SENSIBLE)
t1.config(color='orange',state=DRAGABLE)
t2.config(color='orange',state=DRAGABLE)
'''



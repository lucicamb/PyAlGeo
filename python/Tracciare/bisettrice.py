# File: bisettrice.py - ok
# Date: 17 feb 23
# Note: bisettrice di un angolo

grid()

colc = '#AAAAAA' #colore delle linee di costruzione

#input angolo
r = Ray(INPUT,msg='prima semiretta...',color='red',width=2,state=DRAGABLE)
A = head(r)
s = Ray(INPUT,msg='seconda semiretta...',node=A,color='red',width=2,state=DRAGABLE)

c = Circle(A,1,color=colc,state=VISIBLE,width=1) #w=1: linea sottile
P,Q = inters(c,r)
#P.config(color=colc,state=VISIBLE)
#Q.config(color=colc,state=VISIBLE)
R,S = inters(c,s)
#R.config(color=colc,state=VISIBLE)
#S.config(color=colc,state=VISIBLE)

c1 = Circle(P,1,color=colc,state=VISIBLE,width=1)
c2 = Circle(R,1,color=colc,state=VISIBLE,width=1)
C,D = inters(c1,c2)
#C.config(color=colc,state=VISIBLE)
#D.config(color=colc,state=VISIBLE)

b = Line(C,D,color='blue',state=VISIBLE)


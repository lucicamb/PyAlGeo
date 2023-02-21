# File: trasla_seg.py - ok
# Date: 11 feb 23
# Note: traslazione di un segmento sulla semiretta OX
#       ... rifare evitando l'uso di ang

# trasla il segmento AB sulla semiretta OX, ritornando il punto sull'asse X
def trasla_seg(A:Point,B:Point) -> Point:
    a = ang(A,B)
    b = ang(O,A)
    show('a=',a) #debug
    B1 = rot(A,B,-a) #.config(color='blue',state=VISIBLE)  #-debug
    r = Line(B1,b)
    P = inters(r,Line(O,U))
    return P

#---- main ----
s = Segment(INPUT,color='red',state=DRAGABLE)
M = head(s)
N = tail(s)
T = trasla_seg(M,N)
#T.config(color='green',state=VISIBLE)
t = Segment(O,T,color='green',state=VISIBLE,width=THICK)



# File: duplica_seg.py - ok
# Date: 11 feb 23
# Note: duplicazione segmento usando solo il compasso
#       cfr. alg nel cap. Tracciare

# duplica il segmento AB, ritornando il secondo estremo
def duplica_seg(A:Point,B:Point) -> Point:
    alfa = Circle(A,B)
    beta = Circle(B,A)
    C, D = inters(alfa,beta)
    gamma = Circle(C,D)
    delta = Circle(D,C)
    F, _ = inters(gamma,delta)
    alfa.config(color='gray',state=VISIBLE,width=THIN)  #debug
    beta.config(color='gray',state=VISIBLE,width=THIN)  #debug
    gamma.config(color='gray',state=VISIBLE,width=THIN)  #debug
    delta.config(color='gray',state=VISIBLE,width=THIN)  #debug
    return F

# duplica il segmento AB, ritornando il secondo estremo - ver.2
def duplica_seg2(A:Point,B:Point) -> Point:
    alfa = Circle(A,B)
    beta = Circle(B,A)
    C, _ = inters(alfa,beta)
    gamma = Circle(C,B)
    D, _ = inters(gamma,beta)
    delta = Circle(D,B)
    F, _ = inters(delta,beta)
    alfa.config(color='orange',state=VISIBLE,width=THIN)  #debug
    beta.config(color='orange',state=VISIBLE,width=THIN)  #debug
    gamma.config(color='orange',state=VISIBLE,width=THIN)  #debug
    delta.config(color='orange',state=VISIBLE,width=THIN)  #debug
    return F

#---- main ----
s = Segment(INPUT,color='red',state=DRAGABLE,width=MEDIUM)
M = head(s)
N = tail(s)
T = duplica_seg(M,N)  #ok
#T = duplica_seg2(M,N)  #ok
T.config(color='green',state=VISIBLE)
t = Segment(N,T,color='green',state=VISIBLE,width=MEDIUM)
show('T=',T)



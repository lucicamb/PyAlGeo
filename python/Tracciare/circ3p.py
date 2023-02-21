# File: circ3p.py - ok
# Date: 11 feb 23 
# Note: circonferenza passante per 3 dati punti

_cons_color = 'gray' # colore delle linee di costruzione

# asse di un segmento
# cfr. Alg.153, pag. 499
def asse(s:Segment) -> Line:
    global _cons_color
    A = head(s)
    B = tail(s)
    a = Circle(A,B,color=_cons_color,state=VISIBLE,width=THIN)
    b = Circle(B,A,color=_cons_color,state=VISIBLE,width=THIN)
    P, Q = inters(a,b)
    return Line(P,Q)

# circonferenza per 3 punti 
def circolo(A:Point,B:Point,C:Point) -> Circle:  
    #a1 = asse(Segment(A,B).config(color=_cons_color)).config(color=_cons_color) #ok
    a1 = asse(Segment(A,B).config(color=_cons_color,state=VISIBLE,width=THIN))
    a2 = asse(Segment(B,C).config(color=_cons_color,state=VISIBLE,width=THIN))
    C = inters(a1,a2)
    #return Circle(C,dist(C,A))
    return Circle(C,A)

#---- main ----
mes = "seleziona primo punto ..."
P1 = Point(INPUT,msg=mes,color='blue',state=DRAGABLE)
mes = "seleziona secondo punto ..."
P2 = Point(INPUT,msg=mes,color='blue',state=DRAGABLE)
mes = "seleziona terzo punto ..."
P3 = Point(INPUT,msg=mes,color='blue',state=DRAGABLE)
c = circolo(P1,P2,P3)
c.config(name='c',color='red',state=SENSIBLE)

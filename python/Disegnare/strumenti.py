# File: strumenti.py
# Date: 10 gen 23
# Note: uso della t. come strumento di disegno, di calcolo e di punti

# disegno di un segmento di dati estremi
def segmento(A:Point,B:Point) -> None:
    move(A)
    draw(B)
   
# distanza fra due dati punti (statica)
def distanza(A:Point,B:Point) -> float:
    move(A)
    return dist(B)

# punto medio fra due dati punti
def medio(A:Point,B:Point) -> Point:
    move(A)
    look(B)
    #d = dist(B)/2.
    #print('-------> d=',d,'   type(d)=',type(d))
    jump(dist(B)/2.)  
    #jump(2.)  #cosi' SI
    #jump(d)
    return here()

           
#---- main ----
#A = Point(1,2,color='blue',state=DRAGABLE)  #ok: sono slegati dal segmento
#B = Point(4,1,color='blue',state=DRAGABLE)

#A = Point(1,2) #ok
#B = Point(4,1)

A = Point(INPUT,state=INVISIBLE) #ok
B = Point(INPUT,state=INVISIBLE)

color('red')
segmento(A,B)
d = distanza(A,B)
M = medio(A,B)
#M.config(color='orange',state=DRAGABLE) #e' dragabile
M.config(color='orange',state=VISIBLE)
write('distanza(A,B)=',d)
Writing((80,50),"distanza(A,B)={0}",variables=[d],state=DRAGABLE)
Writing((80,70),"distanza(A,B)="+str(d),state=DRAGABLE)
Writing((80,90),"M="+str(d),state=DRAGABLE) 

       

    



    

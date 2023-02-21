# File: triangolo.py
# Date: 17 feb 23
# Note: disegno di stelle

# triangolo di dati vertici
def triangolo(A:Point,B:Point,C:Point) -> None:
    move(A)
    draw(B)
    draw(C)
    draw(A)
   

# triangolo rettangolo di cateti a e b
def triangoloRettangolo(a:float,b:float) -> None:
    P = pos()
    setang(90)
    forward(a)
    A = pos()
    move(P)
    right(90)
    forward(b)
    draw(A)
   

       
#---- main ----
A = Point(1,2)
B = Point(4,1)
C = Point(2,4)
setcol('red')
triangolo(A,B,C)
#color('green')
#forward(2)
jump(2)
setcol('blue')
triangoloRettangolo(2,3)

       

    



    

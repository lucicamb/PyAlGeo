# File: poligoni.py
# Date: 17 feb 23
# Note: disegno di poligoni

# disegno di un poligono
# di n lati di lunghezza l
def poligono(l:float,n:int) -> None:
    for _ in range(n):
        forward(l)
        left(360/n)

# disegno di un poligono in modalita' OO
# di n lati di lunghezza l
def poligonoOO(l:float,n:int,t:Turtle) -> None:
    for _ in range(n):
        t.forward(l)
        t.left(360/n)
       
#===========================================
setcol('red')
poligono(2,6) #esagono di lato 2
nina = Turtle(color='blue')
#nina.move(Point((2,2)))   #ok
nina.move(Point(2,2))
poligonoOO(2,6,nina)



    



    

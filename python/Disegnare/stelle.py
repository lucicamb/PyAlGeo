# File: stelle.py
# Date: 17 feb 23
# Note: disegno di stelle

# disegno di una stella a 5 punte
# con lato di lunghezza l
def stella(l:float) -> None:
    for _ in range(5):
        forward(l)
        right(144)
        forward(l)
        left(72)

# disegno di una stella incrociata a 5 punte
# con lato di lunghezza l
def stellaincrociata(l:float) -> None:
    for _ in range(5):
        forward(l)
        right(144)
       
#---- main ----
setcol('red')
#stella(3)
stellaincrociata(3) 
       

    



    

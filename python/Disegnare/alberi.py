# File: alberi.py
# Date: 17 feb 23
# Note: disegno di alberi binari

# albero binario
def albero(lato:int,n:int) -> None:
    forward(lato)
    if n>0:
        left(45)
        albero(lato/2,n-1)
        right(90)
        albero(lato/2,n-1)
        left(45)
    #riporta alla base dell'albero
    penup()
    left(180)
    forward(lato)
    right(180)
    pendown()

# albero binario - ver.2
def albero2(lato:int,n:int) -> None:
    push()
    forward(lato)
    if n>0:
        left(45)
        albero(lato/2,n-1)
        right(90)
        albero(lato/2,n-1)
        left(45)
    pop() #riporta alla base dell'albero

       
#---- main ----
left(90)
pendown()
setcol('green')
albero(4,5)
setcol('black')
albero2(5,4)


    



    

# File: hilbert.py
# Date: 17 feb 23
# Note: curve di Hilbert

# cfr. Turtle Geometry: The Computer as a Medium for Exploring Mathematics
# by Harold Abelson and Andrea diSessa p. 96-98
def hilbert(l:float, n:int, k=1):
    if n > 0:
        left(k*90)
        hilbert(l,n-1,-k)
        forward(l)
        right(k*90)
        hilbert(l,n-1,k)
        forward(l)
        hilbert(l,n-1,k)
        right(k*90)
        forward(l)
        hilbert(l,n-1,-k)
        left(k*90)
       
#---- main ----
setcol('red')
show()
hilbert(.5,4)
hide()



    



    

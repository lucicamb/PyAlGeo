# File: vonkock.py
# Date: 17 feb 23
# Note: disegno di curve di von Kock

# disegno della curva di von kock lato l ed ordine n 
def vonkock(l:float,n:int) -> None:
    if n==0:
        forward(l)
    else:
        vonkock(l/3,n-1)
        left(60)
        vonkock(l/3,n-1)
        right(120)
        vonkock(l/3,n-1)
        left(60)
        vonkock(l/3,n-1)
       
#---- main ----
setcol('red')
vonkock(8,4)
       

    



    

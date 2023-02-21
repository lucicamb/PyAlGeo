# File: triangric.py
# Date: 17 feb 23
# Note: disegno di triangoli ricorsivi ed iterativi

# triangoli - modalita' ricorsiva  
def triangoli(l:float,n:int):
    forward(l)        
    left(120)
    forward(l/2)        
    left(60)
    if n>1:
        triangoli(l/2,n-1)
    right(60)
    forward(l/2)        
    left(120)
    forward(l)        
    left(120)

# triangoli - modalita' iterativa  
def triangoli2(l:float,n:int):
    for i in range(n):
        for j in range(3):
            forward(l)        
            left(120)
        l = l/2
        forward(l)
        left(60)
           
#---- main ----
pendown()
setcol('red')
triangoli(4,5)
penup()
forward(3.5)
pendown()
setcol('black')
triangoli2(5,7)


    



    

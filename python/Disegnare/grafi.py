# File: grafi.py 
# Date: 17 feb 23
# Note: disegno di un grafo completo 

# disegno di un grafo completo
# di n lati di lunghezza l
def grafo(n:int,l:float):
    # calcolo dei vertici del grafo,
    # memorizzati nella sequenza P
    P = n*[None]  
    for i in range(n):
        #P[i] = dpos()  #riferimento dinamico: NO
        P[i] = pos()
        #forward(l)
        jump(l)
        left(360/n)
        #write('Pi=',P[i])
        #point()

    #for i in range(n): print(' ->P[i]=',coordsvalues(P[i]))
    #print('---->  P[3]=',coordsvalues(P[3]))

    # disegno del grafo
    for i in range(n):
        for j in range (i+1,n):
            #write('Px=',P[i])
            #write('  Py=',P[j])
            #print('i=',i,'  Pi=',coordsvalues(P[i]))
            #print('j=',j,'  Pj=',coordsvalues(P[j]))
            move(P[i])
            draw(P[j])            
  

# disegno di un grafo completo di n lati di lunghezza l - ok
def grafo2(n:int,l:float):
    # punti base
    A = pos()
    forward(l)
    B = pos()
    for i in range(n):
        for j in range(n):
            move(A)
            look(B) 
            for k in range(j):
                forward(l)
                left(360/n)
            draw(A) #disegno
        A = B
        look(B)
        forward(l)
        left(360/n)
        forward(l)
        B = pos()

# disegno di un grafo completo di n lati di lunghezza l - ok
def grafo3(n:int,l:float):
    for i in range(n):
        P = pos()
        a = getang()
        for j in range(i+1,n+1):
            for _ in range(j-i):
                jump(l)
                left(360/n)
            draw(P) #disegno
            setang(a)
        jump(l)
        left(360/n)
    
# disegno di un grafo completo di n lati di lunghezza l - ok
def grafo4(n:int,l:float):
    a = 360/n
    for i in range(n):
        P = pos()
        jump(l)
        left(a)
        push()
        for j in range(i+1,n+1):
            push()
            draw(P)
            pop()
            jump(l)
            left(a)
        pop()
    
    
#---- main ----
setcol('blue')
grafo(7,3)
setcol('black')
grafo2(9,3.2)
setcol('red')
grafo3(7,3.2)
setcol('brown')
grafo4(9,3.2)




    



    

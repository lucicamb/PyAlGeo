# File: turtles.py - ok
# Date: 17 feb 23
# Note: la grafica della tartaruga e calcoli
#       modalita' object-oriented
#       argomenti: tartarughe, oggetti, array
#
# Accetta comandi dalla linea di comando:
#   t1.move(Point(2,3))
#   t1.draw(Point(4,1))
#   t1.left(45)

# radice di 2
def radice2() -> float:
    #P = pos()
    move(Point(0,0))
    #P = Point(dpos())
    P = pos()
    show('P=',P)
    jump(1)
    left(90)
    jump(1)
    Q = pos()
    show('Q=',Q)
    return dist(P)
    #return distfrom(P)  #ok

# radice di n
def radice(n:int) -> float:
    P = pos()  #SERVE FARE UN clone? 
    #P = Point(pos())  #clone
    for _ in range(n):
        look(P)
        right(90)
        jump(1)
    #x = dist(P)
    #write('x=',x)
    return dist(P)

# inseguimento fra 2 t.
def inseguimento():
    t1 = Turtle(color='red')  
    t2 = Turtle(color='blue')
    
    #t1.move(Point(-2,1,state=VISIBLE,color=t1.getcolor()))
    #t1.move(Point(-2,1,state=DRAGABLE,color=t1.getcolor()))
    
    #message('seleziona punto di partenza della tartaruga...')
    mes = 'seleziona punto di partenza della tartaruga...'
    t1.move(Point(INPUT,msg=mes,state=DRAGABLE,color=t1.getcolor())) #trascinabile
    #t1.move(Point(-2,1))
    
    message('')
    setmode(0) #esce dal modo INPUT e permette il drag del punto
    t2.move(Point(7,3))
    
    #t1.write('t1 parte da qui')  #da implementare in Pen [13mag22]
    #t2.write('t2 parte da qui')
    
    #t2.point()
   
    t1.show()
    t2.show()
    #print('------ turtles: prima di assegnazione ----')
    p = t2.pos()
    #print('------ turtles: passata assegnazione ----')
    #write('DIST t1-t2 =',t1.dist(t2.pos())) #basta qui: e' un valore dinamico
    while t1.dist(t2.pos())>.01:
        #write('DIST t1-t2 =',t1.dist(t2.pos())) #non e' dinamico
        #t1.forward(.1)     # piu' lenta
        #t2.forward(.11)    # piu' veloce
        t1.forward(.05)     # piu' lenta - OK .05
        t2.forward(.06)    # piu' veloce
        t1.left(1)          # ruota di poco - era 3
        t2.look(t1.pos())   # orienta verso t1
        #t2.write('o')     # marker
       
def ciaot():
    print('ciao dalla funzione ciaot() di turtles.py')


#---- spirale di tartarughe ---- ok
# n: numero di t.
def spiraletar(n:int):
    #t = n*[Turtle()]  #riferimenti ad uno stesso oggetto
    t = n*[None]
    colors = ['red','green','blue','orange','brown']
    for i in range(n):
        t[i] = Turtle()
        t[i].setcol(colors[i % len(colors)])
        t[i].left(360/n*i)
        t[i].show()

    for _ in range(40):
        for i in range(n):
           t[i].forward(.2)
           t[i].left(5)

#quadrato con diagonali con uso di push e pop
def quadratocondiagonali(lato:int):
    left(45)
    setcol('red')
    for _ in range(4):
        push()
        push()
        jump(lato)
        P = pos()
        pop()
        right(90)
        forward(lato)
        draw(P)
        pop()
        right(90)

#croce a 4 braccia
def croce4braccia(lato:int):
    for _ in range(4):  
        push()
        forward(lato)
        push()
        right(45)
        forward(lato)
        pop()   #esercizio: cosa avviene togliendo questa pop?
        #pop() x   # ERRORE segnalato correttamente
        #x = y     # ERRORE segnalato correttamente
        left(45)
        forward(lato)
        pop()
        left(90)


#calcoli con la t.
def calcoli() -> None:
    for k in range(10):
        write('radice('+str(k)+')='+str(radice(k)))

#disegno di un grafo completo di n vertici e dato lato
def grafo(n:int,lato:float) -> None:
    a = [] # array dei vertici
    #move((-2,-2))
    move(Point(-2,-2))
    penup()
    for i in range(n):
        a += [pos()]
        forward(lato)  
        left(360/n)
    pendown()
    setcol('red')
    #show()
    for i in range(n):
        for j in range(i+1,n):
            move(a[i])
            draw(a[j])

#---- main ----
grid()         #attiva il grid


'''
#-- inseguimento e spirale -- ok 17feb23
inseguimento() #inseguimento di 2 tartarughe ok
#quadratocondiagonali(5) #ok
#croce4braccia(3) #ok
#grafo(7,3)  #ok
#spiraletar(7)  #ok
'''

'''
#-- calcoli -- ok 17feb23
show('radice di 2=',radice2())  #ok
calcoli()
'''


'''
#---- esempio base ---- ok  17feb23
t1 = Turtle()
t1.setcol('red')
t1.show()

t2 = Turtle()
P = Point(0,0) #,state=INVISIBLE)
Q = Point(3,4) #,state=INVISIBLE)
t1.move(P)
t2.move(Q)

#t2.show()
for _ in range(4):
   t1.forward(2)
   t2.forward(2.5)
   t1.left(90)
   t2.right(90)
#t1.look(Q)
t1.look(t2.pos())
#t1.write('sono qui')
#t1.write('T1: io sono qui')  #abilitare! [17feb23]
#t2.write('T2: io sono qua')
'''


#---- figure con push e pop ----

'''
#sole con raggi - ok 17feb23
n = 11 # numero raggi
l = 3  # lunghezza raggi
for _ in range(n):
    push()
    forward(l)
    pop()
    left(360/n)
'''

#'''
#---- 3 esagono --  ok 17feb23
# commentando le linee # si ottiene una figura aperta
l = 3  # lunghezza tratti
for _ in range(3):   #6
    push()
    forward(l)
    push()
    right(60)
    forward(l)
    right(60)  #
    forward(l) #
    pop()
    left(60)
    forward(l)
    left(60)   #
    forward(l) #
    pop()
    left(120)
#'''

#'''    
#altra modalita': - ok 17feb23
for _ in range(3):   
    push()
    for _ in range(5):
        forward(l)
        left(60)
    pop()
    left(120)
#'''    



''' DA CONTROLLARE DA UQI IN POI [3ott21]
P = Point(INPUT,name='P',msg='inserisci punto...',color='red',state=DRAGABLE)
write("P=",P)
#move(P)  #attenzione!!!

Q = pos()
Q.config(name='Q',color='blue',state=VISIBLE)
write("Q=",Q)
forward(1.5)
show()

write('dist1(Turtle,P) =',dist(P,pos()))
write('dist2(Turtle,P) =',dist(P,dpos()))
'''


'''
#prove del 25apr22 - ok, MA muovendo il punto la t. non si volta
t = Turtle(color='red')  
#t.move(Point(-2,1))
t.move(Point(-2,1,state=VISIBLE,color=t.getcolor()))
t.show()
#t1.move(Point(-2,1,state=DRAGABLE,color=t1.getcolor()))
message('seleziona un punto da guardare...')
t.look(Point(INPUT,state=DRAGABLE,color=t.getcolor())) #trascinabile
setmode(0) #esce dal modo INPUT e permette il drag del punto
'''

    
    








   

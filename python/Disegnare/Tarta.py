# File: Tarta.py - ok
# Date: 17 feb 23
# Note: esempio con la grafica della tartaruga object-oriented
#       argomenti: tartarughe, oggetti, array

#from graph import _Value

#-------------------------------------------------
# estensione della classe Turtle:
# una Tarta e' una Turtle che non cambia colore
# e che ha un contatore dei passi
#
class Tarta(Turtle):

    # costruttore
    def __init__(self,col='black'):
        Turtle.__init__(self)
        #self.color(col) #non ha effetto
        super().setcol(col)  
        #Turtle.color(col)   #ERR
        self.show()
        self._passi = 0 # numero di passi percorsi
        Writing((80,70),"passi=[{0}]",variables=[self.npassi()],state=DRAGABLE)  
       
    # metodo ridefinito   
    def forward(self, passi:float):  
        super().forward(passi)  
        #Turtle.forward(passi)  #ERR
        self._passi += passi  
        
    # numero passi - valore dinamico  
    def npassi(self):
        #return _Value(self._pos,self.percorso,'percorso')  #ok
        #return _Value(self.dpos(),self.percorso,'percorso')  #ok
        #return _Value(self.dpos(),lambda:self._passi,'npassi')  #definito in graph
        return Value(lambda:self._passi,self.dpos())  #definito in kinter
               
    # percorso fatto - valore statico   
    def percorso(self):
        return self._passi 
     
    # metodo aggiunto   
    def poligono(self, n:int, lato:float):
        for _ in range(n):
             self.forward(lato)
             self.left(360/n)
        
    # metodo disinnescato   
    def setcol(self, col:str):
        pass
        '''
        if col in ('red','blue'):
            super().setcol(col)
        '''
       
#---- main ----
#grid()
P = Point(INPUT,color='red',state=DRAGABLE)

t = Tarta('red')

t.move(Point(-3,-2))
t.draw(Point(1,4))
t.draw(Point(-1,2))
#t.move((-3,-2))
t.forward(2.5)

show('percorso:',t.percorso()) #valore statico
show('npassi:',t.npassi())     #valore dinamico

t.setcol('blue') # ha effetto
t.setcol('green') # non ha effetto
t.poligono(7,3)

#write('distanza:',t.dist(P))
d = t.dpos().dist(P)
show('distanza dinamica:',d)
show('distanza statica:',val(d))

T = t.pos()  #posizione fissa
show('distanza2:',T.dist(P))
D = t.pos()  #posizione dinamica
show('T = ',T)
show('D = ',D)  #posizione dinamica

#circ. di raggio var. che segue la t
c = Circle(D,d,color='blue',state=VISIBLE,width=MEDIUM)

k = 1
for _ in range(100):
    t.forward(k)
    t.left(90)
    k += .1

t.look(P)

   

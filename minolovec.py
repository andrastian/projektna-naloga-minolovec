import tkinter as tk
from random import randint
import time


okno = tk.Tk()
igralnopolje = tk.Frame(okno)
zgornjavrstica = tk.Frame(okno)
spodnjavrstica = tk.Frame(okno)

class podatki:
    def __init__(self,velikost,stMin):
        self.velikost = velikost
        self.mine = stMin
        self.preverjenapolja = 0
        self.igra = True
        self.pretecencas = time.clock()
        
podatki = podatki(5,10)

class CeloPolje:
    def __init__(self):
        self.mina = False
    def naredi_gumb(self,x,y):
        def pritisni():
            self.preveri()
        self.x=x
        self.y=y
        self.gumb = tk.Button(igralnopolje, text='',bg = 'mint cream', height=1, width=2, command=pritisni)
        self.gumb.grid(row=y, column=x)
        igralnopolje.grid(row=1, column=0, columnspan=2)

    def preveri(self):
        if podatki.igra == False:
            if self.mina == True:
                self.gumb.config(text='x',bg = 'tomato', state='disabled')
            else:
                x = self.x
                y = self.y
                z = 0
                for(n,m) in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
                    if 0 <= x+n <= podatki.velikost-1 and 0 <= y+m <= podatki.velikost-1:
                        if polje[x+n][y+m].mina == True:
                            z += 1
                self.gumb.config(text='{0}'.format(z), bg = 'mint cream', state='disabled')
        if zastave.postavljazastave == False:
            podatki.preverjenapolja += 1
            if self.mina == True:
                self.gumb.config(text='x',bg = 'tomato', state='disabled')
                self.konec()
            else:
                x = self.x
                y = self.y
                z = 0
                for(n,m) in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
                    if 0 <= x+n <= podatki.velikost-1 and 0 <= y+m <= podatki.velikost-1:
                        if polje[x+n][y+m].mina == True:
                            z += 1
                self.gumb.config(text='{0}'.format(z), bg = 'mint cream', state='disabled')
                if podatki.preverjenapolja == podatki.velikost**2 - podatki.mine:
                    self.zmaga()
                if z == 0:
                    for(n,m) in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
                        if 0 <= x+n <= podatki.velikost-1 and 0 <= y+m <= podatki.velikost-1:
                            polje[x+n][y+m].gumb.invoke()
                        
        else:
            self.gumb.config(text='z', bg = 'lightgoldenrod1')
    

#endshit
    
        

        
    def reset(self):
        resetnipolje()
        podatki.preverjenapolja = 0
        podatki.igra = True
        podatki.pretecencas = time.clock()
        zgornjavrstica.grid_remove()
        cas=Timer()
        
    def zmaga(self):
        for x in range(podatki.velikost):
            for y in range(podatki.velikost):
                polje[x][y].gumb.config(state='disabled')
        self.zmagasporocilo = tk.Label(spodnjavrstica, text='čestitke, našli ste vse mine',bg = 'mint cream', height=1, width=20)
        self.zmagasporocilo.grid(row=0, column=0)
        spodnjavrstica.grid(row=2, column=0, columnspan=2)
        podatki.igra = False
        self.resetgumb = tk.Button(spodnjavrstica, text='poskusi ponovno',bg = 'mint cream', height=1, width=20, command=self.reset)
        self.resetgumb.grid(row=0, column=1)
        spodnjavrstica.grid(row=2, column=0, columnspan=2) 
        
    def konec(self):
        podatki.igra = False
        for x in range(podatki.velikost):
            for y in range(podatki.velikost):
                polje[x][y].gumb.invoke()
        self.sporocilo = tk.Label(spodnjavrstica, text='razneslo vas je',bg = 'mint cream', height=1, width=20)
        self.sporocilo.grid(row=0, column=0)
        spodnjavrstica.grid(row=2, column=0, columnspan=2)
        self.resetgumb = tk.Button(spodnjavrstica, text='poskusi ponovno',bg = 'mint cream', height=1, width=20, command=self.reset)
        self.resetgumb.grid(row=0, column=1)
        spodnjavrstica.grid(row=2, column=0, columnspan=2)
        
class Zastave:
    def __init__(self):
        self.postavljazastave = False

        def postavljajZastave():
            if self.postavljazastave == False:
                self.postavljazastave = True
                self.zastave.configure(bg = 'spring green')
            elif self.postavljazastave == True:
                self.postavljazastave = False
                self.zastave.configure(bg = 'mint cream')
    
        self.zastave = tk.Button(zgornjavrstica, text='postavljanje zastav',bg = 'mint cream', height=1, width=20, command=postavljajZastave)
        self.zastave.grid(row=0, column=0)
        zgornjavrstica.grid(row=0, column=0, columnspan=2)

#timer

class Timer():
    def __init__(self):
        self.ura = tk.Label(zgornjavrstica, text="")
        self.ura.grid(row=0, column=1)
        zgornjavrstica.grid(row=0, column=1, columnspan=2)
        self.osvezi()
    def osvezi(self):
        casomer =  time.clock()
        self.ura.configure(text='Pretečen čas: {0} sekund'.format( round (casomer - podatki.pretecencas)))
        if podatki.igra == True:
            self.ura.after(1000, self.osvezi)
            

def resetnipolje():
    for x in range(podatki.velikost):
        for y in range(podatki.velikost):
            polje[x][y].gumb.configure(text='', state ='active',bg = 'mint cream')
            if polje[x][y].mina == True:
                polje[x][y].mina = False
    for n in range(podatki.mine):
        while True:
            x = randint(0, podatki.velikost-1)
            y = randint(0, podatki.velikost-1)
            if polje[x][y].mina == False:
                polje[x][y].mina = True
                break


                
def ustvaripolje():
#postavljanje min
    for n in range(podatki.mine):
        while True:
            x = randint(0, podatki.velikost-1)
            y = randint(0, podatki.velikost-1)
            if polje[x][y].mina == False:
                polje[x][y].mina = True
                break
    for x in range(podatki.velikost):
        for y in range(podatki.velikost):
            polje[x][y].naredi_gumb(x,y)

cas=Timer()

polje = [ [CeloPolje() for y in range(20)] for x in range(20)]



zastave = Zastave()


ustvaripolje()
okno.mainloop()


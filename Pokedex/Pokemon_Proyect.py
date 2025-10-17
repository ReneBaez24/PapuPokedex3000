#saquenme de latinoamerica

from abc import ABC, abstractmethod

class Pokemon_Base(ABC):
    def __init__(self,nombre="sin pokemon",descripcion="no descripcion",ataque=0
                 ,vida=0,defensa=0,lvl=0,evolucion=1,next_evo=""
                 ,last_evo="",atrapado=False):
        self.nombre= nombre
        self.descripcion = descripcion
        self.ataque = ataque
        self.vida = vida
        self.defensa = defensa
        self.lvl = lvl
        self.evolucion= evolucion
        self.next_evo= next_evo
        self.last_evo= last_evo
        self.atrapado = atrapado
    @abstractmethod
    def hablar(self):
        pass
    @abstractmethod
    def actualizar(self):
        pass
    @abstractmethod
    def detallesPokemon(self):
        pass
    
class Pokemon(Pokemon_Base):
    def __init__(self, nombre="sin pokemon", descripcion="no descripcion", ataque=0, vida=0, defensa=0, lvl=0, evolucion=1, next_evo="", last_evo="", atrapado=False):
        super().__init__(nombre, descripcion, ataque, vida, defensa, lvl, evolucion, next_evo, last_evo, atrapado)

    def hablar(self):
        print(f"!{self.nombre}!")


    #cambiar esta wea    
    def actualizar(self):
        print("eldiablo")

    
    def detallesPokemon(self):
        print(f"\n nombre del pokemon {self.nombre} ")
        print(f"\n descripcion del pokemon {self.descripcion} ")
        print(f"\n ataque del pokemon {self.ataque} ")
        print(f"\n vida del pokemon {self.vida} ")
        print(f"\n defensa del pokemon {self.defensa} ")
        print(f"\n nivel del pokemon {self.lvl} ")
        print(f"\n evolucion del pokemon {self.evolucion} ")
        print(f"\n atrapado = {self.atrapado} ")

    def entrenar(self):
        self.ataque+=10
        self.defensa+=10
        self.vida+=10
        self.lvl+=10
        print("pokemon entrenado")
        print(f"ataque = {self.ataque}")
        print(f"defensa = {self.defensa}")
        print(f"vida del pokemon {self.vida} ")
        print(f"nivel del pokemon {self.lvl} ")


        if self.lvl >= 100:
            if self.evolucion < 3:
                self.lvl=0
                self.evolucion+=1
                print(f"la wea fome evoluciono y se convirtio en {self.next_evo}")
                self.nombre=self.next_evo
                self.next_evo=self.last_evo
    def subirAtaque(self):
        self.ataque+=20
    def subirDefensa(self):
        self.defensa+=20
    def subirVida(self):
        self.vida+=20
    
    def boostAll(self):
        self.ataque+=20
        self.defensa+=20
        self.vida+=20

class Agua (Pokemon):
    def __init__(self, nombre="sin pokemon", descripcion="no descripcion", ataque=0, vida=0, defensa=0, lvl=0, evolucion=1, next_evo="", last_evo="", atrapado=False):
        super().__init__(nombre, descripcion, ataque, vida, defensa, lvl, evolucion, next_evo, last_evo, atrapado)
        self.ataque_especial ="hidro bomba" 

class Fuego(Pokemon):
    def __init__(self, nombre="sin pokemon", descripcion="no descripcion", ataque=0, vida=0, defensa=0, lvl=0, evolucion=1, next_evo="", last_evo="", atrapado=False):
        super().__init__(nombre, descripcion, ataque, vida, defensa, lvl, evolucion, next_evo, last_evo, atrapado)
        self.ataque_especial ="lanza llamas"
    
class Electrico(Pokemon):
    def __init__(self, nombre="sin pokemon", descripcion="no descripcion", ataque=0, vida=0, defensa=0, lvl=0, evolucion=1, next_evo="", last_evo="", atrapado=False):
        super().__init__(nombre, descripcion, ataque, vida, defensa, lvl, evolucion, next_evo, last_evo, atrapado)
        self.ataque_especial ="Ataque Tesla "
    
class Planta(Pokemon): 
    def __init__(self, nombre="sin pokemon", descripcion="no descripcion", ataque=0, vida=0, defensa=0, lvl=0, evolucion=1, next_evo="", last_evo="", atrapado=False):
        super().__init__(nombre, descripcion, ataque, vida, defensa, lvl, evolucion, next_evo, last_evo, atrapado)
        self.ataque_especial ="rayo solar"



class Entrenamiento(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def subirAtaque(self):
        pass
    @abstractmethod
    def subirDefensa(self):
        pass
    @abstractmethod
    def subirVida(self):
        pass

class Pokemon_Entrenamiento(Entrenamiento, Pokemon):
    def __init__(self):
        pass
    def subirAtaque(self):
        self.ataque += 20
    def subirVida(self):
        self.vida+= 20
    def subirDefensa(self):
        self.defensa += 20
    
#(self,nombre="sin pokemon",descripcion="no descripcion",ataque=0,vida=0,defensa=0,lvl=0,evolucion=1,next_evo="",last_evo="",atrapado=False):
mudkip=Agua("Mudkip","poquemon aguado",70,50,50,5,1,"marshtomp","swampert",False)
mudkip.detallesPokemon()

chimchar=Fuego("Chimchar","Macaco du Fogo",58,44,44,5,1,"Monferno","Infernape",False)
chimchar.detallesPokemon()

Zapdos=Electrico("Zapdos","Pajarraco Culiao",90,90,85,70,3,"","",False)
Zapdos.detallesPokemon()

Roserade=Planta("Roserade","Inserta musica de piano",125,60,105,74,3,"","",False)
Roserade.detallesPokemon()

nombrepacomon = input("Ingresa el nombre del enemigo: ")
desc = input("Ingresa la descipcion del pokemnon: ")
ata = int(input("Ingresa el ataque: "))
vid = int(input("Ingresa la vida: "))
defen = int(input("Ingresa el defensa: "))
level = int(input("Ingresa el nivel: "))
tipe = int(input("Cual es el tipo de pokemon?\n[1] Agua\n[2] Fuego\n[3]Electrico\n[4] Planta)"))
des = int(input("Cuantas evoluciones tiene? "))

if tipe == 1:
    if des == 0:
        pacomonEnemigo = Agua(nombrepacomon,desc,ata,vid,defen,level,3,"","",False)
    elif des == 1 :
        evo1 = input("Ingresa el nombre de la primera evolucion: ")
        pacomonEnemigo = Agua(nombrepacomon,desc,ata,vid,defen,level,2,evo1,"",False)
    elif des == 2:
        evo1 = input("Ingresa el nombre de la primera evolucion: ")
        evo2 = input("Ingresa el nombre de la segunda evolucion: ")
        pacomonEnemigo = Agua(nombrepacomon,desc,ata,vid,defen,level,1,evo1,evo2,False)
elif tipe == 2:
    if des == 0:
        pacomonEnemigo = Fuego(nombrepacomon,desc,ata,vid,defen,level,3,"","",False)
    elif des == 1 :
        evo1 = input("Ingresa el nombre de la primera evolucion: ")
        pacomonEnemigo = Fuego(nombrepacomon,desc,ata,vid,defen,level,2,evo1,"",False)
    elif des == 2:
        evo1 = input("Ingresa el nombre de la primera evolucion: ")
        evo2 = input("Ingresa el nombre de la segunda evolucion: ")
        pacomonEnemigo = Fuego(nombrepacomon,desc,ata,vid,defen,level,1,evo1,evo2,False)
elif tipe == 3:
    if des == 0:
        pacomonEnemigo = Electrico(nombrepacomon,desc,ata,vid,defen,level,3,"","",False)
    elif des == 1 :
        evo1 = input("Ingresa el nombre de la primera evolucion: ")
        pacomonEnemigo = Electrico(nombrepacomon,desc,ata,vid,defen,level,2,evo1,"",False)
    elif des == 2:
        evo1 = input("Ingresa el nombre de la primera evolucion: ")
        evo2 = input("Ingresa el nombre de la segunda evolucion: ")
        pacomonEnemigo = Electrico(nombrepacomon,desc,ata,vid,defen,level,1,evo1,evo2,False)
elif tipe == 4:
    if des == 0:
        pacomonEnemigo = Planta(nombrepacomon,desc,ata,vid,defen,level,3,"","",False)
    elif des == 1 :
        evo1 = input("Ingresa el nombre de la primera evolucion: ")
        pacomonEnemigo = Planta(nombrepacomon,desc,ata,vid,defen,level,2,evo1,"",False)
    elif des == 2:
        evo1 = input("Ingresa el nombre de la primera evolucion: ")
        evo2 = input("Ingresa el nombre de la segunda evolucion: ")
        pacomonEnemigo = Planta(nombrepacomon,desc,ata,vid,defen,level,1,evo1,evo2,False)
else:
    print("Mi loco, elige una opcion valida")

pacomonEnemigo.detallesPokemon()




"""
pikachu=Pokemon()
pikachu.detallesPokemon()
pikachu.next_evo="raichu"
for i in range(12):
    pikachu.entrenar()

"""



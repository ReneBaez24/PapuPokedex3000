#saquenme de latinoamerica

from abc import ABC, abstractmethod

class Pokemon_Base(ABC):
    def __init__(self,):
        self.nombre= "sin pokemon"
        self.descripcion = "no descripcion"
        self.ataque = 0
        self.vida = 0
        self.defensa = 0
        #lvl acronimo de level que es nivel en ingles
        self.lvl = 0
        self.evolucion= 1
        self.next_evo=""
        self.last_evo=""
        self.atrapado = False
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
    def __init__(self):
        super().__init__()

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

class Agua (Pokemon_Base):# actualizar metodo
    def __init__(self):
        self.ataque_especial ="hidro bomba" 

class Fuego(Pokemon_Base):# actualizar 
    def __init__(self):
        self.ataque_especial ="lanza llamas"
    
class Electrico(Pokemon_Base):# actualizar 
    def __init__(self):
        self.ataque_especial ="tacleada de vulteos "
    
class Planta(Pokemon_Base): # actualizar 
    def __init__(self):
        self.ataque_especial ="rallo solar😍"

#clase de herenria multiple

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
    


    



#pruebas
pikachu=Pokemon()
pikachu.detallesPokemon()
pikachu.next_evo="raichu"
for i in range(12):
    pikachu.entrenar()





#saquenme de latinoamerica

from abc import ABC, abstractmethod
import random 
from rich.table import Table
from rich.console import Console

console = Console()

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

    def actualizar(self):
        print("eldiablo")

    def detallesPokemon(self):
        table = Table(title="🎮 DETALLES DEL POKÉMON 🎮", show_header=True, header_style="bold magenta")

        
        table.add_column("Atributo", style="cyan", width=20)
        table.add_column("Valor", style="yellow", width=30)
        
        table.add_row("Nombre", str(self.nombre))
        table.add_row("Descripción", str(self.descripcion))
        table.add_row("Ataque", f"[red]{self.ataque}[/red]")
        table.add_row("Vida", f"[green]{self.vida}[/green]")
        table.add_row("Defensa", f"[blue]{self.defensa}[/blue]")
        table.add_row("Nivel", f"[magenta]{self.lvl}[/magenta]")
        table.add_row("Evolución", str(self.evolucion))
        table.add_row("Atrapado", "Sí" if self.atrapado else " No")
        
        console.print(table)

    def detallesCombate(self):
        table = Table(title="⚔️  DETALLES DE COMBATE ⚔️", show_header=True, header_style="bold red")
        
        table.add_column("Atributo", style="cyan", width=20)
        table.add_column("Valor", style="yellow", width=30)
         
        table.add_row("Nombre", f"[bold]{self.nombre}[/bold]")
        table.add_row("Ataque", f"[red bold]{self.ataque}[/red bold] 🗡️")
        table.add_row("Vida", f"[green bold]{self.vida}[/green bold] ❤️")
        table.add_row("Defensa", f"[blue bold]{self.defensa}[/blue bold] 🛡️")
        
        console.print(table)

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

def Combate(pkmn1,pkmn2):
    print(f"Pokemon {pkmn2.nombre} busca pelea! ")
    print("detalles de tu pokemon")
    pkmn1.detallesCombate()
    print("detalles del pokemon rival")
    pkmn2.detallesCombate()
    faint = False
    eleccion=0
    vidaCombate1=pkmn1.vida
    vidaCombate2=pkmn2.vida
    while faint == False :
        table = Table(title="⚔️ pokemon hp ⚔️", show_header= False, header_style="bold red")
        table.add_row(f"[green bold]{pkmn1.nombre}: HP {vidaCombate1}❤️[/green bold]  vs [green bold]{pkmn2.nombre}: HP {vidaCombate2}❤️[/green bold] ")

        console.print(table)

        huida=False
        while eleccion == 0:
            print(f"Opciones de combate ")
            print(f"[1] Ataque normal")
            print(f"[2] Ataque especial ")
            print(f"[3] Pasar turno ")
            print(f"[4] Huir ")
            eleccion=int(input(""))

            winner=""
            if eleccion == 1:
                print(f"{pkmn1.nombre} ataca! ")
                dmg1=pkmn1.ataque - pkmn2.defensa
                if dmg1<=0:
                    dmg1=5
                vidaCombate2-=dmg1
                if vidaCombate2 <= 0:
                    vidaCombate2 = 0
                    winner=pkmn1.nombre
                    break
            elif eleccion == 2:
                print(f"{pkmn1.nombre} realiza su ataque especial: {pkmn1.ataque_especial}! ")
                dmg1=(pkmn1.ataque*1.5) - pkmn2.defensa

                if dmg1<=0:
                    dmg1=5
                vidaCombate2-=dmg1
                if vidaCombate2 <= 0:
                    vidaCombate2 = 0
                    winner=pkmn1.nombre
                    break
            elif eleccion == 3:
                print(f"{pkmn1.nombre} descansa y recupera 5 hp")
                vidaCombate1+=5
            elif eleccion ==4:
                huir=random.randrange(3)
                if huir != 1:
                    print(f"huiste de la batalla")
                    huida=True
                else:
                    print("llora")

        if huida == True:
            faint= True
            return
        if vidaCombate2 > 0:
            print(f"Turno del rival")
            rivalwea=random.randrange(1,4)
            if rivalwea ==1:
                print(f"{pkmn2.nombre} ataca! ")
                dmg2=pkmn2.ataque - pkmn1.defensa
                if dmg2<=0:
                    dmg2=5
                vidaCombate1-=dmg2
                if vidaCombate1 <= 0:
                    vidaCombate1 = 0
                    winner=pkmn2.nombre
            elif rivalwea == 2:
                    print(f"{pkmn2.nombre} realiza su ataque especial: {pkmn2.ataque_especial}! ")
                    dmg2=(pkmn2.ataque*1.5) - pkmn1.defensa

                    if dmg2<=0:
                        dmg2=5
                    vidaCombate1-=dmg2
                    if vidaCombate1 <= 0:
                        vidaCombate1 = 0
                        winner=pkmn2.nombre
            elif rivalwea == 3:
                print(f"{pkmn2.nombre} descansa y recupera 5 hp")
                vidaCombate2+=5
        
        eleccion=0    
       
        if vidaCombate2 == 0:
            faint= True
            print(f"El ganador del combate es {winner}")
            if pkmn1.vida > pkmn2.vida :
                print("Capturaste al pokemon!")
                pkmn2.atrapado = True
                pkmnAtrapados.append(pkmn2)
            else:
                print("el pokemon se escapo (tu vida base era menor)")

        elif vidaCombate1 == 0:  
            faint= True
            print(f"El ganador del combate es {winner}") 


mudkip=Agua("Mudkip","poquemon aguado",70,50,50,5,1,"marshtomp","swampert",False)
mudkip.detallesPokemon()

chimchar=Fuego("Chimchar","Macaco du Fogo",58,44,44,5,1,"Monferno","Infernape",False)
chimchar.detallesPokemon()

pichu=Electrico("pichu","rata electrica",40,20,35,5,1,"pikachu","raichu",False)
pichu.detallesPokemon()

treeko=Planta("treeko","wea de planta",45,40,35,5,1,"pikachu","raichu",False)
treeko.detallesPokemon()

Zapdos=Electrico("Zapdos","Pajarraco Culiao",90,90,85,70,3,"","",False)
Zapdos.detallesPokemon()

Roserade=Planta("Roserade","Inserta musica de piano",125,60,105,74,3,"","",False)
Roserade.detallesPokemon()

pkmnlista= [mudkip,chimchar,pichu,treeko,Zapdos,Roserade]
pkmnAtrapados= []

def Crear_rival():
    nombrepacomon = input("Ingresa el nombre del enemigo: ")
    desc = input("Ingresa la descipcion del pokemnon: ")
    ata = int(input("Ingresa el ataque: "))
    vid = int(input("Ingresa la vida: "))
    defen = int(input("Ingresa el defensa: "))
    level = int(input("Ingresa el nivel: "))
    tipe = int(input("Cual es el tipo de pokemon?\n[1] Agua\n[2] Fuego\n[3]Electrico\n[4] Planta)\n"))
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
    pkmnlista.append(pacomonEnemigo)
    return pacomonEnemigo

user = input("Bienvenido al simulador de PapuPokedex, Cual es tu nombre: ")
print(f"Es un placer, {user} no tienes pokemones ")
print("[1] mudkip\n[2] Chimchar\n[3] Treeko\n[4] Pichu")
poke_des = 0
while poke_des < 1 or poke_des > 4:
    poke_des = int(input("Cual elegis: "))
    if poke_des == 1:
        mudkip.atrapado = True
        pkmnAtrapados.append(mudkip)
        mudkip.detallesPokemon()
    elif poke_des == 2:
        chimchar.atrapado = True
        pkmnAtrapados.append(chimchar)
        chimchar.detallesPokemon()
    elif poke_des == 3:
        treeko.atrapado = True
        pkmnAtrapados.append(treeko)
        treeko.detallesPokemon()
    elif poke_des == 4:
        pichu.atrapado = True
        pkmnAtrapados.append(pichu)
        pichu.detallesPokemon()
    else:
        print("Eres o te haces?")


des = 0
while des != 5:
    print("\nMENU PRINCIPAL")
    print("[1] Mostrar pokemon atrapados")
    print("[2] Pokemon habla")
    print("[3] Entrenar")
    print("[4] Combatir")
    print("[5] Salir")
    des = int(input("Que deseas hacer? "))
    if des == 1:
        for i in pkmnAtrapados:
            i.detallesPokemon()
    elif des == 2:
        for i, c in enumerate(pkmnAtrapados):
            print(f"{i+1}. {c.nombre}")
        select = int(input("Selecciona tu pokemon para hablar: "))
        c.hablar()
    elif des == 3:
        for i, c in enumerate(pkmnAtrapados):
            print(f"{i+1}. {c.nombre}")
        select = int(input("Selecciona tu pokemon a entrenar: "))
        print("\nMENU DE ENTRENAMIENTO")
        print("[1] Entrenamiento normal")
        print("[2] Entrenamiento individual")
        print("[3] Entrenamiento intensivo")
        print("[4] Entrenamiento personalizado")
        subdes = int(input("Que tipo de entrenamiento deseas realizar? "))
        if subdes == 1:
            c.entrenar()
        elif subdes == 2:
            desx = int(input("Que atributo deseas mejorar? (1. Ataque, 2. Defensa, 3. Vida) "))
            if desx == 1:
                c.subirAtaque()
                print(f"Ataque: [{c.ataque}]")
            elif desx == 2:
                c.subirDefensa()
                print(f"Defensa: [{c.defensa}]")
            elif desx == 3:
                c.subirVida()
                print(f"Vida: [{c.vida}]")
            else:
                print("Error, opcion no valida")
        elif subdes == 3:
            c.boostAll()
            print(f"Ataque: [{c.ataque}]")
            print(f"Defensa: [{c.defensa}]")
            print(f"Vida: [{c.vida}]")
        elif subdes == 4:
            desx = int(input("Que atributo deseas modificar? (1. Ataque, 2. Defensa, 3. Vida, 4. nivel)"))
            if desx == 1:
                nuevo = int(input("Ingresa el nuevo valor para el ataque: "))
                c.ataque = nuevo
                print(f"Ataque de {c.nombre}: [{c.ataque}]")
            elif desx == 2:
                nuevo = int(input("Ingresa el nuevo valor para el defensa: "))
                c.defensa = nuevo
                print(f"Defensa de {c.nombre}: [{c.ataque}]")
            elif desx == 3:
                nuevo = int(input("Ingresa el nuevo valor para el vida: "))
                c.vida = nuevo
                print(f"Vida de {c.nombre}: [{c.vida}]")
            elif desx == 4:
                nuevo = int(input("Ingresa el nuevo valor para el nivel: "))
                c.lvl = nuevo
                print(f"Nivel de {c.nombre}: [{c.lvl}]")
            else:
                print("Tu no aprendes verdad?")
    elif des == 4:
        for i, c in enumerate(pkmnAtrapados):
            print(f"{i+1}. {c.nombre}")
        select = int(input("Selecciona tu pokemon para combatir: "))
        print("\nMENU DE SELECCION DE RIVAL")
        print("[1] Elegir rival")
        print("[2] Rival aleatorio")
        print("[3] Crear rival")
        subdes = int(input("Que eliges? "))
        if subdes == 1:
            for i, c in enumerate(pkmnlista):
                print(f"{i+1}. {c.nombre}")
            rival = int(input("Selecciona el pokemon a enfrentar: "))
            Combate(pkmnAtrapados[select-1],pkmnlista[rival-1])
        elif subdes == 2:
            alazar = random.randrange(1,7)
            Combate(pkmnAtrapados[select-1],pkmnlista[alazar-1])
        elif subdes == 3:
            Combate(pkmnAtrapados[select-1],Crear_rival())
        else:
            print("Otra vez?")
    elif des == 5:
        print("Hasta la proxima. FIN DEL PROGRAMA")
        break
    else:
        print("Error elja una opcion valida ")
#saquenme de latinoamerica
# CILANTRO
# PEREJIL

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
        print(f"\n!{self.nombre}!\n")

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
            while(True):
                try:
                    eleccion=int(input(f"Que deberia hacer {pkmn1.nombre}?  "))
                    if eleccion < 1 or eleccion > 4:
                        print("ERROR. La opcion no es valida")
                    else:
                        break
                except ValueError:
                    print("ERROR. Ingresa un valor numerico valido")

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


mudkip=Agua("Mudkip","pokemon aguado",70,50,50,5,1,"marshtomp","swampert",False)


chimchar=Fuego("Chimchar","Macaco du Fogo",58,44,44,5,1,"Monferno","Infernape",False)


pichu=Electrico("pichu","rata electrica",40,20,35,5,1,"pikachu","raichu",False)


treeko=Planta("treeko","wea de planta",45,40,35,5,1,"groovyle","sceptile",False)


Zapdos=Electrico("Zapdos","Pajarraco Culiao",90,90,85,70,3,"","",False)


Roserade=Planta("Roserade","Inserta musica de piano",125,60,105,74,3,"","",False)


pkmnlista= [mudkip,chimchar,pichu,treeko,Zapdos,Roserade]
pkmnAtrapados= []

def Crear_rival():
    nombrepacomon = input("Ingresa el nombre del enemigo: ")
    desc = input("Ingresa la descipcion del pokemnon: ")
    while(True):
        try:
            ata = int(input("Ingresa el ataque: "))
            break
        except ValueError:
            print("ERROR. Ingresa un valor numerico valido")
    while(True):
        try:
            vid = int(input("Ingresa la vida: "))
            break
        except ValueError:
            print("ERROR. Ingresa un valor numerico valido")
    while(True):
        try:
            defen = int(input("Ingresa el defensa: "))
            break
        except ValueError:
            print("ERROR. Ingresa un valor numerico valido")
    while(True):
        try:
            level = int(input("Ingresa el nivel: "))
            if level < 1 or level > 99:
                print("ERROR. Ingresa un nivel valido (1-99)")
            else:
                break
        except ValueError:
            print("ERROR. EL valor ingresado es un decimal(No valido)")
    while(True):
        try:
            tipe = int(input("Cual es el tipo de pokemon?\n[1] Agua\n[2] Fuego\n[3]Electrico\n[4] Planta)\n"))
            if tipe < 1 or tipe > 4:
                print("ERROR. Ingresa una de las opciones validas mencionadas")
            else:
                break
        except ValueError:
            print("ERROR. Ingresa un valor numerico valido")
    while(True):
        try:
            des = int(input("Cuantas evoluciones tiene? "))
            if tipe < 0 or tipe > 2:
                print("ERROR. Ingresa una de las opciones validas(0-2)")
            else:
                break
        except ValueError:
            print("ERROR. Ingresa un valor numerico valido")

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
    while(True):
        try:
            poke_des = int(input("Cual eliges: "))
            break
        except ValueError:
            print("ERROR. Ingresa un valor numerico valido")
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
        print(f"ERROR. Numero no valido(Opcion {poke_des} no disponible)")


des = 0
while des != 5:
    print("\nMENU PRINCIPAL")
    print("[1] Mostrar pokemon atrapados")
    print("[2] Pokemon habla")
    print("[3] Entrenar")
    print("[4] Combatir")
    print("[5] Salir")
    while(True):
        try:
            des = int(input("Que deseas hacer? "))
            break
        except ValueError:
            print("ERROR. Ingrese un valor numerico valido.")
    if des == 1:
        for i in pkmnAtrapados:
            i.detallesPokemon()
    elif des == 2:
        while(True):
            print("LISTA DE POKEMONES DISPONIBLES")
            print("-" * 30)
            for i, c in enumerate(pkmnAtrapados):
                print(f"{i+1}. {c.nombre}")
            print("Teclee [0] para regresar al menu principal")
            tama = len(pkmnAtrapados)
            while(True):
                try:
                    select = int(input("Selecciona tu pokemon para hablar: "))
                    if select < 0 or select > tama:
                        print(f"ERROR. El pokemon numero {select} no existe.")
                    else:
                        break
                except ValueError:
                    print("ERROR. Ingresa un valor numerico para elegir pokemon")
            if select == 0:
                break
            c.hablar()
    elif des == 3:
        print("LISTA DE POKEMONES DISPONIBLES")
        print("-" * 30)
        for i, c in enumerate(pkmnAtrapados):
            print(f"{i+1}. {c.nombre}")
        tama = len(pkmnAtrapados)
        while(True):
            try:
                select = int(input("Selecciona tu pokemon a entrenar: "))
                if select < 1 or select > tama:
                    print(f"ERROR. El pokemon numero {select} no existe.")
                else:
                    break
            except ValueError:
                print("ERROR. Ingresa un valor numerico para elegir pokemon")
        while(True):
            print("\nMENU DE ENTRENAMIENTO")
            print("[1] Entrenamiento normal")
            print("[2] Entrenamiento individual")
            print("[3] Entrenamiento intensivo")
            print("[4] Entrenamiento personalizado")
            print("[0] Regresar al menu principal")
            while(True):
                try:
                    subdes = int(input("Que tipo de entrenamiento deseas realizar? "))
                    if subdes < 0 or subdes > 4:
                        print("ERROR. Opcion de entrenamiento no valida.")
                    else:
                        break
                except ValueError:
                    print("ERROR. Ingrese un valor numerico valido")
            if subdes == 0:
                print("Regresando.....")
                break
            elif subdes == 1:
                c.entrenar()
            elif subdes == 2:
                while(True):
                    try:
                        desx = int(input("Que atributo deseas mejorar? (1. Ataque, 2. Defensa, 3. Vida) "))
                        if desx < 1 or desx > 3:
                            print("ERROR. Atributo ingresado no valido")
                        else:
                            break
                    except ValueError:
                        print("ERROR. Ingrese un valor numerico valido")
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
                while(True):
                    while(True):
                        try:
                            desx = int(input("Que atributo deseas modificar? (1. Ataque, 2. Defensa, 3. Vida, 4. nivel, 0. Regresar)"))
                            if desx < 0 or desx > 4:
                                print("ERROR. Opcion de atributo seleccionado no valido")
                            else:
                                break
                        except ValueError:
                            print("ERROR. Ingrese solo valores numericos enteros")
                    if desx == 0:
                        break
                    elif desx == 1:
                        while(True):
                            try:
                                nuevo = int(input("Ingresa el nuevo valor para el ataque: "))
                                if nuevo < 1:
                                    print("ERROR. Ingresa un valor numerico positivo")
                                else:
                                    c.ataque = nuevo
                                    print(f"Ataque de {c.nombre}: [{c.ataque}]")
                                    break
                            except ValueError:
                                print("ERROR. Ingresa un valor numerico valido")
                    elif desx == 2:
                        while(True):
                            try:
                                nuevo = int(input("Ingresa el nuevo valor para la defensa: "))
                                if nuevo < 1:
                                    print("ERROR. Ingresa un valor numerico positivo")
                                else:
                                    c.defensa = nuevo
                                    print(f"Defensa de {c.nombre}: [{c.ataque}]")
                                    break
                            except ValueError:
                                print("ERROR. Ingresa un valor numerico valido")
                    elif desx == 3:
                        while(True):
                            try:
                                nuevo = int(input("Ingresa el nuevo valor para la vida: "))
                                if nuevo < 1:
                                    print("ERROR. Ingresa un valor numerico positivo")
                                else:
                                    c.vida = nuevo
                                    print(f"Vida de {c.nombre}: [{c.vida}]")
                                    break
                            except ValueError:
                                print("ERROR. Ingresa un valor numerico valido")
                    elif desx == 4:
                        while(True):
                            try:
                                nuevo = int(input("Ingresa el nuevo valor del nivel (1-99): "))
                                if nuevo < 1 or nuevo > 99:
                                    print("ERROR. Ingresa un valor numerico en el rango dado")
                                else:
                                    c.lvl = nuevo
                                    print(f"Nivel de {c.nombre}: [{c.lvl}]")
                                    break
                            except ValueError:
                                print("ERROR. Ingresa un valor numerico valido")
                    else:
                        print("ERROR. Opcion no valida")
    elif des == 4:
        for i, c in enumerate(pkmnAtrapados):
            print(f"{i+1}. {c.nombre}")
        tama = len(pkmnAtrapados)
        while(True):
            try:
                select = int(input("Selecciona tu pokemon para combatir: "))
                if select < 1 or select > tama:
                    print(f"ERROR. No existe el pokemon numero {select}")
                else:
                    break
            except ValueError:
                print("ERROR. Ingresa un valor numerico valido")
        while(True):
            print("\nMENU DE SELECCION DE RIVAL")
            print("[1] Elegir rival")
            print("[2] Rival aleatorio")
            print("[3] Crear rival")
            print("[0] Regresar")
            while(True):
                try:
                    subdes = int(input("Que eliges? "))
                    if subdes < 0 or subdes > 3:
                        print("ERROR. Ingresa una opcion valida")
                    else:
                        break
                except ValueError:
                    print("ERROR. Ingresa un valor numerico valido")
            if subdes == 0:
                break
            elif subdes == 1:
                for i, c in enumerate(pkmnlista):
                    print(f"{i+1}. {c.nombre}")
                while(True):
                    try:
                        rival = int(input("Selecciona el pokemon a enfrentar: "))
                        if rival < 1 or rival > len(pkmnlista):
                            print(f"ERROR. No existe el rival numero {rival}")
                        else:
                            Combate(pkmnAtrapados[select-1],pkmnlista[rival-1])
                            break
                    except ValueError:
                        print("ERROR. Ingresa un valor numerico valido")
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
        print("ERROR. Elija una opcion valida")
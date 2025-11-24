#saquenme de latinoamerica
# CILANTRO
# PEREJIL

from abc import ABC, abstractmethod
import random 
from rich.table import Table
from rich.console import Console
import sqlite3
import datetime
from datetime import datetime
import os


conta = 0

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
        table = Table(title="🎮 DETALLES DEL POKEMON 🎮", show_header=True, header_style="bold magenta")

        
        table.add_column("Atributo", style="cyan", width=20)
        table.add_column("Valor", style="yellow", width=30)
        
        table.add_row("Nombre", str(self.nombre))
        table.add_row("Descripcion", str(self.descripcion))
        table.add_row("Ataque", f"[red]{self.ataque}[/red]")
        table.add_row("Vida", f"[green]{self.vida}[/green]")
        table.add_row("Defensa", f"[blue]{self.defensa}[/blue]")
        table.add_row("Nivel", f"[magenta]{self.lvl}[/magenta]")
        table.add_row("Evolucion", str(self.evolucion))
        table.add_row("Atrapado", "Si" if self.atrapado else " No")
        
        console.print(table)

    def detallesCombate(self):
        tablecombate = Table(title="⚔️  DETALLES DE COMBATE ⚔️", show_header=True, header_style="bold red")
        
        tablecombate.add_column("Atributo", style="cyan", width=20)
        tablecombate.add_column("Valor", style="yellow", width=30)
         
        tablecombate.add_row("Nombre", f"[bold]{self.nombre}[/bold]")
        tablecombate.add_row("Ataque", f"[red bold]{self.ataque}[/red bold] 🗡️")
        tablecombate.add_row("Vida", f"[green bold]{self.vida}[/green bold] ❤️")
        tablecombate.add_row("Defensa", f"[blue bold]{self.defensa}[/blue bold] 🛡️")
        
        console.print(tablecombate)

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
class RegistroCombate:
    def __init__(self):
        self.log = [] 
        self.fecha_hora = datetime.now().strftime("%d-%m-%Y %H:%M")
        self.nombre_archivo = f"batalla_{datetime.now().strftime('%d-%m-%y_%H-%M')}.txt"
    
    def agregar_turno(self, turno, accion_jugador, accion_rival, stats_jugador, stats_rival):
        self.log.append(f"== TURNO {turno} ==")
        self.log.append(accion_jugador)
        self.log.append(f"Stats del Pokemon Enemigo: Vida {stats_rival['vida']}, Defensa {stats_rival['defensa']}")
        self.log.append(accion_rival)
        self.log.append(f"Stats de mi Pokemon: Vida {stats_jugador['vida']}, Defensa {stats_jugador['defensa']}")
        self.log.append("")
    
    def guardar_combate(self, entrenador, pokemon_jugador, pokemon_rival, resultado):
        try:
            with open(self.nombre_archivo, 'w', encoding='utf-8') as archivo:
                archivo.write("=== COMBATE ===\n")
                archivo.write(f"Entrenador: {entrenador}\n")
                archivo.write(f"pokemon: {pokemon_jugador.nombre}\n")
                archivo.write(f"detalles: Ataque={pokemon_jugador.ataque}, Vida={pokemon_jugador.vida}, Defensa={pokemon_jugador.defensa}\n")
                archivo.write(f"enemigo: {pokemon_rival.nombre}\n")
                archivo.write(f"detalles enemigo: Ataque={pokemon_rival.ataque}, Vida={pokemon_rival.vida}, Defensa={pokemon_rival.defensa}\n")
                archivo.write("\n")
                
                for linea in self.log:
                    archivo.write(linea + "\n")
                
                archivo.write(f"Resultado: {resultado}\n")
                archivo.write(f"Fecha y hora de la batalla: {self.fecha_hora}\n")
                archivo.write("-" * 25)
            
            print(f"Combate guardado en: {self.nombre_archivo}")
            return True
        except IOError as e:
            print(f"Error al guardar el combate: {e}")
            return False

def leer_registro_combate():
    print("REGISTROS DE COMBATE")
    archivos = [f for f in os.listdir() if f.startswith("batalla_") and f.endswith(".txt")]
    
    if not archivos:
        print("No se encontraron registros de combate.")
        return
    
    print("Archivos disponibles:")
    for i, archivo in enumerate(archivos, 1):
        print(f"[{i}] {archivo}")
    
    try:
        seleccion = int(input("selecciona el numero del archivo a leer (0 para cancelar): "))
        if seleccion == 0:
            return
        
        if seleccion < 1 or seleccion > len(archivos):
            print("eliga una opcion valida")
            return
        
        archivo_seleccionado = archivos[seleccion - 1]
        
        try:
            with open(archivo_seleccionado, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                print("\n" + "="*50)
                print(contenido)
                print("="*50)
        except FileNotFoundError:
            print("FileNotFoundError: Archivo no encontrado.")
        except IOError:
            print("IOError: No se pudo leer el archivo.")
            
    except ValueError:
        print("ValueError ingresa un numero valido weon")

def Combate(pkmn1, pkmn2):
    registro = RegistroCombate()
    print(f"Pokemon {pkmn2.nombre} busca pelea! ")
    print("detalles de tu pokemon")
    pkmn1.detallesCombate()
    print("detalles del pokemon rival")
    pkmn2.detallesCombate()
    faint = False
    eleccion = 0
    vidaCombate1 = pkmn1.vida
    vidaCombate2 = pkmn2.vida
    defensaCombate1 = pkmn1.defensa
    defensaCombate2 = pkmn2.defensa
    turno = 1
    resultado = ""
    
    while faint == False:
        huida = False
        accion_jugador = ""
        accion_rival = ""
        
        while eleccion == 0:
            print(f"Opciones de combate ")
            print(f"[1] Ataque normal")
            print(f"[2] Ataque especial ")
            print(f"[3] Pasar turno ")
            print(f"[4] Huir ")
            while(True):
                try:
                    eleccion = int(input(f"Que deberia hacer {pkmn1.nombre}?  "))
                    if eleccion < 1 or eleccion > 4:
                        print("ERROR. La opcion no es valida")
                    else:
                        break
                except ValueError:
                    print("ERROR. Ingresa un valor numerico valido")

            winner = ""
            if eleccion == 1:
                dmg1 = pkmn1.ataque
                print(f"{pkmn1.nombre} usa ataque normal\n{pkmn2.nombre} recibe ataque de {dmg1}! ")
                
                accion_jugador = f"{pkmn1.nombre} usa ataque normal\n{pkmn2.nombre} recibe ataque de {dmg1}"
                
                if defensaCombate2 > 0:
                    defensaCombate2 -= dmg1
                    if defensaCombate2 < 0:
                        residuo = abs(defensaCombate2)
                        vidaCombate2 -= residuo
                        defensaCombate2 = 0
                else:
                    vidaCombate2 -= dmg1
                    
                accion_jugador += f"\nDaño de ataque: {dmg1}"
                
                if vidaCombate2 <= 0:
                    vidaCombate2 = 0
                    winner = pkmn1.nombre
                    resultado = f"Has ganado el combate!"
                    faint = True
                   
                    
            elif eleccion == 2:
                dmg1 = (pkmn1.ataque * 1.5)
                print(f"{pkmn1.nombre} usa ataque especial\n{pkmn2.nombre} recibe ataque de {dmg1}! ")
                
                accion_jugador = f"{pkmn1.nombre} usa ataque especial\n{pkmn2.nombre} recibe ataque de {dmg1}"

                if defensaCombate2 > 0:
                    defensaCombate2 -= dmg1
                    if defensaCombate2 < 0:
                        residuo = abs(defensaCombate2)
                        vidaCombate2 -= residuo
                        defensaCombate2 = 0
                else:
                    vidaCombate2 -= dmg1
                    
                accion_jugador += f"\nDaño de ataque: {dmg1}"
                
                if vidaCombate2 <= 0:
                    vidaCombate2 = 0
                    winner = pkmn1.nombre
                    resultado = f"Has ganado el combate!"
                    faint = True
                    
                    
            elif eleccion == 3:
                print(f"{pkmn1.nombre} descansa y recupera 5 hp")
                vidaCombate1 += 5
                accion_jugador = f"{pkmn1.nombre} descansa y recupera 5 hp"
                
            elif eleccion == 4:
                huir = random.randrange(5)
                if huir != 1:
                    print(f"huiste de la batalla")
                    huida = True
                    resultado = "Huida del combate"
                    faint = True
                else:
                    print("No pudiste huir (llora)") 
                    accion_jugador = f"{pkmn1.nombre} intenta huir pero falla"

        if huida:
            registro.guardar_combate(user, pkmn1, pkmn2, resultado)
            return
            
        if vidaCombate2 > 0 and not faint:
            print(f"Turno del rival")
            rivalwea = random.randrange(1, 4)
            
            if rivalwea == 1:
                dmg2 = pkmn2.ataque
                print(f"{pkmn2.nombre} usa ataque normal\n{pkmn1.nombre} recibe ataque de {dmg2}")
                
                accion_rival = f"{pkmn2.nombre} usa ataque normal\n{pkmn1.nombre} recibe ataque de {dmg2}"

                if defensaCombate1 > 0:
                    defensaCombate1 -= dmg2
                    if defensaCombate1 < 0:
                        residuo = abs(defensaCombate1)
                        vidaCombate1 -= residuo
                        defensaCombate1 = 0
                else:
                    vidaCombate1 -= dmg2
                    
                if vidaCombate1 <= 0:
                    vidaCombate1 = 0
                    winner = pkmn2.nombre
                    resultado = "Haz perdido el combate"
                    faint = True

            elif rivalwea == 2:
                dmg2 = (pkmn2.ataque * 1.5)
                print(f"{pkmn2.nombre} realiza su ataque especial: {pkmn2.ataque_especial}\n{pkmn1.nombre} recibe ataque de {dmg2}! ")
                
                accion_rival = f"{pkmn2.nombre} usa ataque especial: {pkmn2.ataque_especial}\n{pkmn1.nombre} recibe ataque de {dmg2}"
                
                if defensaCombate1 > 0:
                    defensaCombate1 -= dmg2
                    if defensaCombate1 < 0:
                        residuo = abs(defensaCombate1)
                        vidaCombate1 -= residuo
                        defensaCombate1 = 0
                else:
                    vidaCombate1 -= dmg2
                    
                if vidaCombate1 <= 0:
                    vidaCombate1 = 0
                    winner = pkmn2.nombre
                    resultado = "Haz perdido el combate"
                    faint = True
                    
            elif rivalwea == 3:
                print(f"{pkmn2.nombre} descansa y recupera 5 hp")
                vidaCombate2 += 5
                accion_rival = f"{pkmn2.nombre} descansa y recupera 5 hp"

        
        if accion_jugador :
            stats_jugador = {"vida": vidaCombate1, "defensa": defensaCombate1}
            stats_rival = {"vida": vidaCombate2, "defensa": defensaCombate2}
            registro.agregar_turno(turno, accion_jugador, accion_rival, stats_jugador, stats_rival)
            turno += 1
        eleccion = 0
        
        table = Table(title="⚔️ pokemon hp ⚔️", show_header=True, header_style="bold magenta")
        table.add_column("Jugador", style="cyan", width=40)
        table.add_column("Rival", style="yellow", width=40)
        
        table.add_row(f"[green bold]{pkmn1.nombre}: HP {vidaCombate1}❤️[/green bold]  Def {defensaCombate1}🛡️", f"[green bold]{pkmn2.nombre}: HP {vidaCombate2}❤️[/green bold]  Def {defensaCombate2}🛡️")
        
        console.print(table)
        
        if vidaCombate2 == 0:
            faint = True
            print(f"El ganador del combate es {pkmn1.nombre}")
            if pkmn1.vida > pkmn2.vida:
                print("Capturaste al pokemon!")
                pkmn2.atrapado = True
                pkmnAtrapados.append(pkmn2)
                resultado = f"¡Victoria!, Has derrotado al Pokemon enemigo y lo has atrapado!"
            else:
                print("el pokemon se escapo (tu vida base era menor)")
                resultado = "¡Victoria!, Has derrotado al Pokemon enemigo pero no lo atrapaste"

        elif vidaCombate1 == 0:  
            faint = True
            print(f"El ganador del combate es {pkmn2.nombre}")
            resultado = "Derrota, tu Pokemon fue debilitado"
    
    
    registro.guardar_combate(user, pkmn1, pkmn2, resultado)
        


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
            if des < 0 or des > 2:
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

class PokedexBD:
    def __init__(self, conexion, cursor):
        self.conexion = conexion
        self.cursor = cursor

    def crearTabla(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tabla_partidas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            nombre TEXT NOT NULL,
            pk_Inicial TEXT NOT NULL
        )
        """)
        
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemones_atrapados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            partida_id INTEGER NOT NULL,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            ataque INTEGER,
            vida INTEGER,
            defensa INTEGER,
            lvl INTEGER,
            evolucion INTEGER,
            next_evo TEXT,
            last_evo TEXT,
            tipo TEXT NOT NULL,
            FOREIGN KEY (partida_id) REFERENCES tabla_partidas(id)
        )
        """)
        self.conexion.commit()
    
    def guardar_partida(self, nombre, pkh):
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO tabla_partidas (fecha, nombre, pk_Inicial) VALUES (?,?,?)", 
                          (fecha, nombre, pkh))
        self.conexion.commit()
        print("PARTIDA GUARDADA.\n")
        return self.cursor.lastrowid
    
    def guardar_pokemon(self, partida_id, pokemon):
        tipo = type(pokemon).__name__
        
        self.cursor.execute("""
            INSERT INTO pokemones_atrapados 
            (partida_id, nombre, descripcion, ataque, vida, defensa, lvl, evolucion, next_evo, last_evo, tipo)
            VALUES (?,?,?,?,?,?,?,?,?,?,?)
        """, (partida_id, pokemon.nombre, pokemon.descripcion, pokemon.ataque, 
              pokemon.vida, pokemon.defensa, pokemon.lvl, pokemon.evolucion, 
              pokemon.next_evo, pokemon.last_evo, tipo))
        self.conexion.commit()
    
    def eliminar_pokemones_partida(self, partida_id):
        self.cursor.execute("DELETE FROM pokemones_atrapados WHERE partida_id = ?", (partida_id,))
        self.conexion.commit()
    
    def cargar_pokemones(self, partida_id):
        self.cursor.execute("""
            SELECT nombre, descripcion, ataque, vida, defensa, lvl, evolucion, next_evo, last_evo, tipo
            FROM pokemones_atrapados 
            WHERE partida_id = ?
        """, (partida_id,))
        return self.cursor.fetchall()
    
    def eliminar_partida(self, partida_id):
        self.cursor.execute("DELETE FROM pokemones_atrapados WHERE partida_id = ?", (partida_id,))
        self.cursor.execute("DELETE FROM tabla_partidas WHERE id = ?", (partida_id,))
        self.conexion.commit()
        print("PARTIDA ELIMINADA.\n")


def cargar_partida_guardada(partidas, tabla):
    print("\n" + "="*30)
    print("PARTIDAS GUARDADAS")
    print("="*30)
    
    for i, partida in enumerate(partidas):
        print(f"[{i+1}] ID: {partida[0]} | Fecha: {partida[1]}")
        print(f"    Jugador: {partida[2]} | Pokemon inicial: {partida[3]}")
        print("-"*60)
    
    while True:
        try:
            seleccion = int(input("\nSelecciona el numero de partida a cargar (0 para cancelar): "))
            if seleccion == 0:
                return None, []
            if seleccion < 1 or seleccion > len(partidas):
                print(f"ERROR. Selecciona una opcion valida (1-{len(partidas)})")
            else:
                break
        except ValueError:
            print("ERROR. Ingresa un valor numerico valido")
    
    partida_seleccionada = partidas[seleccion - 1]
    partida_id = partida_seleccionada[0]
    nombre_jugador = partida_seleccionada[2]
    
    pokemones_guardados = tabla.cargar_pokemones(partida_id)
    pkmnAtrapados_cargados = []
    
    print(f"\nCargando partida de {nombre_jugador}...")
    global user 
    user = nombre_jugador
    for pkmn_data in pokemones_guardados:
        nombre, desc, ataque, vida, defensa, lvl, evo, next_evo, last_evo, tipo = pkmn_data
        
        if tipo == "Agua":
            pkmn = Agua(nombre, desc, ataque, vida, defensa, lvl, evo, next_evo, last_evo, True)
        elif tipo == "Fuego":
            pkmn = Fuego(nombre, desc, ataque, vida, defensa, lvl, evo, next_evo, last_evo, True)
        elif tipo == "Electrico":
            pkmn = Electrico(nombre, desc, ataque, vida, defensa, lvl, evo, next_evo, last_evo, True)
        elif tipo == "Planta":
            pkmn = Planta(nombre, desc, ataque, vida, defensa, lvl, evo, next_evo, last_evo, True)
        else:
            continue
        
        pkmnAtrapados_cargados.append(pkmn)
    
    print(f"PARTIDA CARGADA")
    print(f"Pokemones cargados: {len(pkmnAtrapados_cargados)}")
    
    return partida_id, pkmnAtrapados_cargados

def crear_nueva_partida(tabla):
    print("\n" + "="*30)
    print("CREAR NUEVA PARTIDA")
    print("="*30)
    global user
    name = input("\nIngresa tu nombre: ")
    user = name
    print("\nLISTA DE POKEMONES A ELEGIR")
    print("="*35)
    print("[1] Mudkip")
    print("[2] Chimchar")
    print("[3] Treeko")
    print("[4] Pichu")
    
    poke_des = 0
    pokemon_inicial = ""
    pokemon_elegido = None
    
    while poke_des < 1 or poke_des > 4:
        try:
            poke_des = int(input("\n¿Cual eliges?: "))
        except ValueError:
            print("ERROR. Ingresa un valor numerico valido")
            continue
            
        if poke_des == 1:
            mudkip.atrapado = True
            pokemon_elegido = mudkip
            pokemon_inicial = "Mudkip"
            mudkip.detallesPokemon()
            break
        elif poke_des == 2:
            chimchar.atrapado = True
            pokemon_elegido = chimchar
            pokemon_inicial = "Chimchar"
            chimchar.detallesPokemon()
            break
        elif poke_des == 3:
            treeko.atrapado = True
            pokemon_elegido = treeko
            pokemon_inicial = "Treeko"
            treeko.detallesPokemon()
            break
        elif poke_des == 4:
            pichu.atrapado = True
            pokemon_elegido = pichu
            pokemon_inicial = "Pichu"
            pichu.detallesPokemon()
            break
        else:
            print(f"ERROR. Opcion {poke_des} no disponible")
    
    partida_id = tabla.guardar_partida(name, pokemon_inicial)
    print(f"\nPartida creada. ID: {partida_id}")
    print(f"Que empiezen los juegos, {name}!\n")
    
    return partida_id, [pokemon_elegido]


conexion = sqlite3.connect("pokedex.db")
cursor = conexion.cursor()
tabla = PokedexBD(conexion, cursor)
tabla.crearTabla()
cursor.execute("SELECT * FROM tabla_partidas")
partidas = cursor.fetchall()

partida_actual_id = None
pkmnAtrapados = []



if len(partidas) == 0:
    print("\n" + "="*30)
    print("BIENVENIDO")
    print("="*30)
    print("\nNo hay partidas guardadas.")
    
    while True:
        des = input("\n¿Quieres iniciar una nueva partida? (s/n): ").lower()
        if des == "s":
            partida_actual_id, pkmnAtrapados = crear_nueva_partida(tabla)
            break
        elif des == "n":
            print("\n¡Hasta luego!")
            conexion.close()
            exit()
        else:
            print("ERROR. Ingresa 's' para si o 'n' para no")
else:
    print("\n" + "="*30)
    print("BIENVENIDO")
    print("="*30)
    print(f"\nSe encontraron {len(partidas)} partida(s) guardada(s)")
    
    while True:
        print("\n" + "="*60)
        print("MENU DE INICIO")
        print("="*60)
        print("[1] Cargar partida existente")
        print("[2] Crear nueva partida")
        print("[3] Eliminar partida")
        print("[0] Salir")
        try:
            opcion_inicio = int(input("\n¿Que deseas hacer?: "))
        except ValueError:
            print("ERROR. Ingresa un valor numerico valido")
            continue

        if opcion_inicio == 1:
            partida_actual_id, pkmnAtrapados = cargar_partida_guardada(partidas, tabla)
            conta = 1
            if partida_actual_id is not None:
                break
            else:
                print("\nCarga cancelada")
                
        elif opcion_inicio == 2:
            partida_actual_id, pkmnAtrapados = crear_nueva_partida(tabla)
            break
            
        elif opcion_inicio == 3:
            print("\n" + "="*30)
            print("ELIMINAR PARTIDA")
            print("="*30)
            
            for i, partida in enumerate(partidas):
                print(f"[{i+1}] ID: {partida[0]} | Jugador: {partida[2]} | Fecha: {partida[1]}")
            
            try:
                seleccion = int(input("\nSelecciona el numero de partida a eliminar (0 para cancelar): "))
                if seleccion == 0:
                    continue
                if seleccion < 1 or seleccion > len(partidas):
                    print(f"ERROR. Selecciona una opcion valida (1-{len(partidas)})")
                    continue
                
                confirmacion = input(f"\n¿Estas seguro de eliminar esta partida? (s/n): ").lower()
                if confirmacion == "s":
                    partida_id_eliminar = partidas[seleccion - 1][0]
                    tabla.eliminar_partida(partida_id_eliminar)
                    cursor.execute("SELECT * FROM tabla_partidas")
                    partidas = cursor.fetchall()
                    if len(partidas) == 0:
                        print("\nNo quedan partidas guardadas.")
                        des = input("¿Quieres crear una nueva partida? (s/n): ").lower()
                        if des == "s":
                            partida_actual_id, pkmnAtrapados = crear_nueva_partida(tabla)
                            break
                        else:
                            print("\nNos vemos")
                            conexion.close()
                            exit()
                else:
                    print("Eliminacion cancelada")
            except ValueError:
                print("ERROR. Ingresa un valor numerico valido")
                
        elif opcion_inicio == 0:
            print("\nNos vemos")
            conexion.close()
            exit()
        else:
            print("ERROR. Selecciona una opcion valida")


if partida_actual_id is None or len(pkmnAtrapados) == 0:
    print("\nERROR. No se pudo iniciar el programa")
    conexion.close()
    exit()

print("\n" + "="*30)
print("QUE EMPIEZE EL JUEGO")
print("="*30)

des = 99

while(True):
    print("\nMENU PRINCIPAL")
    print("[1] Mostrar pokemon atrapados")
    print("[2] Pokemon habla")
    print("[3] Entrenar")
    print("[4] Combatir")
    print("[5] Guardar partida")
    print("[6] prueva de manejo de errores")
    print("[7] Registros de batallas")
    print("[0] Salir")
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
                                    print(f"Defensa de {c.nombre}: [{c.defensa}]")
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
        if partida_actual_id is not None:
            print("\nGuardando progreso...")
            tabla.eliminar_pokemones_partida(partida_actual_id)
            for pokemon in pkmnAtrapados:
                tabla.guardar_pokemon(partida_actual_id, pokemon)
            print(f"Progreso guardado")
            print(f"Pokemones guardados: {len(pkmnAtrapados)}")
            conta = 1
        else:
            print("ERROR. No hay una partida activa.")
        
    elif des == 6:
        while(True):
            print("\n=== PRUEBAS DE MANEJO DE ERRORES ===")
            print("[1] Division por cero")
            print("[2] Acceso a indice fuera de rango")
            print("[3] Conversion de tipo invalida")
            print("[4] Acceso a atributo inexistente")
            print("[5] Operacion con pokemon sin atributo especial")
            print("[6] Error de tipo en operaciones")
            print("[0] Regresar al menu principal")

            while(True):
                try:
                    prueba = int(input("Selecciona la prueba de error: "))
                    if prueba < 0 or prueba > 6:
                        print("ERROR. Selecciona una opcion valida")
                    else:
                        break
                except ValueError:
                    print("ERROR. Ingresa un valor numerico valido")
            
            if prueba == 0:
                print("Regresando al menu principal...")
                break
            elif prueba == 1:
                try:
                    print("\n[PRUEBA 1: Division por cero]")
                    print("Intentando dividir el ataque de un pokemon entre 0...")
                    resultado = pkmnAtrapados[0].ataque / 0
                    print(f"Resultado: {resultado}")
                except ZeroDivisionError as e:
                    print(f"ERROR CAPTURADO: {type(e).__name__}")
                    print(f"Descripcion: No se puede dividir entre cero")
                    print("Manejo: La operacion fue cancelada y el programa continua normalmente")
            elif prueba == 2:
                try:
                    print("\n[PRUEBA 2: Acceso a indice fuera de rango]")
                    print(f"Intentando acceder al pokemon en la posicion 999...")
                    pokemon_inexistente = pkmnAtrapados[999]
                    print(f"Pokemon: {pokemon_inexistente.nombre}")
                except IndexError as e:
                    print(f"ERROR CAPTURADO: {type(e).__name__}")
                    print(f"Descripcion: El indice solicitado no existe en la lista")
                    print(f"Manejo: Se verifico que solo existen {len(pkmnAtrapados)} pokemon(s) atrapado(s)")
            elif prueba == 3:
                try:
                    print("\n[PRUEBA 3: Conversion de tipo invalida]")
                    print("Intentando convertir el nombre del pokemon a numero...")
                    numero = int(pkmnAtrapados[0].nombre)
                    print(f"Numero: {numero}")
                except ValueError as e:
                    print(f"ERROR CAPTURADO: {type(e).__name__}")
                    print(f"Descripcion: No se puede convertir un texto a numero")
                    print(f"Manejo: El nombre '{pkmnAtrapados[0].nombre}' permanece como texto")
            elif prueba == 4:
                try:
                    print("\n[PRUEBA 4: Acceso a atributo inexistente]")
                    print("Intentando acceder a un atributo que no existe...")
                    atributo_falso = pkmnAtrapados[0].poder_magico_supremo
                    print(f"Atributo: {atributo_falso}")
                except AttributeError as e:
                    print(f"ERROR CAPTURADO: {type(e).__name__}")
                    print(f"Descripcion: El pokemon no tiene ese atributo")
                    print(f"Manejo: Se confirma que {pkmnAtrapados[0].nombre} solo tiene atributos validos")
            elif prueba == 5:      
                try:
                    print("\n[PRUEBA 5: Operacion con pokemon sin ataque especial]")
                    print("Creando un pokemon base sin ataque especial...")
                    pokemon_base = Pokemon("TestMon","Pokemon de prueba",50,50,50,10,1,"","",True)
                    print(f"Intentando usar ataque especial de {pokemon_base.nombre}...")
                    print(f"Ataque especial: {pokemon_base.ataque_especial}")
                except AttributeError as e:
                    print(f"ERROR CAPTURADO: {type(e).__name__}")
                    print(f"Descripcion: El pokemon base no tiene ataque especial definido")
                    print(f"Manejo: Solo los pokemon de tipo especifico (Agua, Fuego, etc) tienen ataques especiales")
            elif prueba == 6:
                try:
                    print("\n[PRUEBA 6: Error de tipo en operaciones]")
                    print("Intentando sumar el ataque del pokemon con su nombre...")
                    resultado = pkmnAtrapados[0].ataque + pkmnAtrapados[0].nombre
                    print(f"Resultado: {resultado}")
                except TypeError as e:
                    print(f"ERROR CAPTURADO: {type(e).__name__}")
                    print(f"Descripcion: No se puede realizar operaciones aritmeticas entre numeros y texto")
                    print(f"Manejo: El ataque ({pkmnAtrapados[0].ataque}) y el nombre ('{pkmnAtrapados[0].nombre}') son tipos incompatibles")
            
            print("\n=== FIN DE LA PRUEBA ===")
    elif des == 7:
        leer_registro_combate()
    elif des == 0:
        des2 = "s"
        while(True):
            if conta == 0:
                des2 = input("Seguro que quieres salir sin guardar? (s/n): ")
                if des2 == "s":
                    tabla.eliminar_partida(partida_actual_id)
                    break
                elif des2 == "n":
                    break
                else:
                    print("ERROR. Ingresa una opcion valida")
                    continue
            else:
                break
        if des2 == "n":
            continue
        print("Hasta la proxima. FIN DEL PROGRAMA")
        break
    else:
        print("ERROR. Elija una opcion valida")
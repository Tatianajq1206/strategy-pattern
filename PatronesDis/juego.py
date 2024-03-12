'''Supongamos que estás desarrollando un juego de estrategia en el que los jugadores pueden elegir entre diferentes 
tipos de unidades militares, como soldados, arqueros y caballeros. Cada tipo de unidad tiene diferentes 
comportamientos de ataque y movimiento. Utiliza el patrón Strategy para implementar estos comportamientos de manera flexible.'''

class armaStrategy:
    def atacar(self, n):
        pass

class Espadas(armaStrategy):
    def atacar(self, n):
        return "Los Caballeros ataca con su espada" + str(n) + " veces."

class ballestas(armaStrategy):
    def atacar(self, n):
        return "Los arqueros disparan con ballestas " + str(n) + " flechas."

class Fuego(armaStrategy):
    def atacar(self, n):
        return "Los Soldados aracan con armas de fuego " + str(n) + " veces."

class unidades():
    def __init__(self, arm_stratrgy):
        self.arm_stratrgy = arm_stratrgy
    def atacar(self, enemi):
        pass
    def moverse(self):
        print('La unidad militares se mueve caminando o corriendo')

class Soldados(unidades):
    def atacar(self, enemi):
        #super().atacar(enemi)
        print('Los soldados atacan con', self.arm_stratrgy.atacar(5))
    
class Arqueros(unidades):
    def atacar(self, enemi):
        #super().atacar(enemi)
        print('Los arqueros atacan con', self.arm_stratrgy.atacar(3))

class Caballeros(Soldados):
    def atacar(self, enemi):
        #super().atacar(enemi)
        print('Los caballeros atacan con', self.arm_stratrgy.atacar(10))

Espada =  Espadas()
Ballesta = ballestas()
FuegoArma = Fuego()
soldado = Soldados(Espada)
caballero = Caballeros(FuegoArma)
arqueiro = Arqueros(Ballesta)


soldado.atacar("infanteria")
arqueiro.atacar("caballereria")
caballero.atacar("infanteria")

soldado.moverse()

#Se calculen los impuestos de estados unidos o europa, con base al salario que uno resive, pero varia segun el pais de la union europea o el estado 
#Variables, cuanto gana, lugar en donde trabaja
#10% de lo que gana

class  impuesto_estado():
    def porcentaje():
        pass
class estados(impuesto_estado):
    def porcentajegen():
        print('Se le quitara el 10 de su salario')

class union (impuesto_estado):
    def porcentajegen():
        print('Se le quita el 40%')
        
class  lugar():
    def __init__(self,eurosalario):
        self.eurosalario= eurosalario
    
    def  trabajador(self):
        #self.impuestos.porcentajegen()
        self.eurosalario -= self.eurosalario*0.1
        print("El trabajador debe pagar un impuesto de: ",self.eurosalario)

class   empresero(lugar):
    def __init__(self,eurosalario,tipodeempresa):
        super().__init__(eurosalario)
        self.impuestos= tipodeempresa()

if  __name__ == "__main__":
    empresa="union"
    salario=150000
    if empresa=="estado":
        trabajador=estados(salario)
    elif empresa=="union":
        trabajador=empresero(salario,union)
    else :
        raise ValueError ("No es una opcion valida")
    trabajador.trabajador()



def interface():
    def fly():
        pass
class formfly(interface):
    def fly():
        print('Tengo alas y puedo volar')
class flytoday(interface):
    def  fly():
        print('Puedo volar hoy')
class Duck:
    def __init__(self, fly_behavior: interface):
        self.fly_behavior = fly_behavior
    def perform(self):
        self._fly_behavior.fly()

    def quak():
        print('bffhfh')
    def swim():
        print('hhfsjkdhfh')
    def display():
        print('Soy un pato')

class tipoduck(Duck):
    def __init__(self):
        super().__init__(formfly())
    def display():
        print('Soy un pato real')

class formaDuck(Duck):
    def __init__(self):
        super().__init__(flytoday())
    def display():
        print('Soy un pato rojo')

class anatommyDuck(Duck):
    def display():
        print('Es un pato de goma')
    def fly():
        print("No puedo volar")
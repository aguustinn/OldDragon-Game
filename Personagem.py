from Atributos import Atributos
class Personagem:

    a = Atributos()


    def __init__(self):
        self.nome = None
        self.idade = None
        self.a.AtributosRandom = None


    def mostrar(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
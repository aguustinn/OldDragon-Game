from .atributos import Atributos
from .raca import Raca
from .classe import Classe

class Personagem:
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.raca = None
        self.classe = None
        self.atributos = Atributos()
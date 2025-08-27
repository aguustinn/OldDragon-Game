class Personagem:
        
    def __init__(self):
        self.nome = None
        self.idade = None
      
    def mostrar(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
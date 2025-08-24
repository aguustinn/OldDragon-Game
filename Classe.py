class Classe:


    def __init__(self):
        self.tipo = None
       

    def escolhaClasse(self, escolha):
        if escolha == 1:
            self.tipo = "Guerreiro"
        elif escolha == 2:
            self.tipo = "Mago"
        elif escolha == 3:
            self.tipo = "Ladrão"
        else:
            self.tipo = "Desconhecida"

    def mostrarClasse(self):
        print(f"A classe escolhida foi: {self.tipo}")
        
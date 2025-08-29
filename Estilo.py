import random

class Estilo:
    atributos = ["FOR", "DES", "CON", "INT", "SAB", "CAR"]

    def rolar_3d6(self):
        return sum(random.randint(1, 6) for _ in range(3))

    def rolar_4d6_descarta(self):
        dados = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(dados)[1:])
    
class Classico (Estilo):
    def gerar (self):
        valores = [self.rolar_3d6() for _ in range(6)]
        return dict(zip(self.atributos, valores))
    
class Aventureiro(Estilo):
     def gerar(self):
        valores = [self.rolar_3d6() for _ in range(6)]
        print("Valores rolados:", valores)
        atributos = {}
        for a in self.atributos:
            while True:
                try:
                    escolha = int(input(f"Escolha valor para {a}: "))
                    if escolha in valores:
                        atributos[a] = escolha
                        valores.remove(escolha)
                        break
                    else:
                        print("Valor não disponível!")
                except ValueError:
                    print("Digite um número válido!")
        return atributos
     
class Heroico(Estilo):
    def gerar(self):
        # Rola 4d6 descarta o menor
        valores = [self.rolar_4d6_descarta() for _ in range(6)]
        print("Valores rolados:", valores)
        atributos = {}
        for a in self.atributos:
            while True:
                try:
                    escolha = int(input(f"Escolha valor para {a}: "))
                    if escolha in valores:
                        atributos[a] = escolha
                        valores.remove(escolha)
                        break
                    else:
                        print("Valor não disponível!")
                except ValueError:
                    print("Digite um número válido!")
        return atributos

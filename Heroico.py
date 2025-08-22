from Estilo import Estilo


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
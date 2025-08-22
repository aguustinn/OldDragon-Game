from JogarDado import JogarDado

class Atributos:
    def __init__(self):
        self.j = JogarDado()
        self.AtributosRandom = {
            "forca": None,
            "destreza": None,
            "constituicao": None,
            "inteligencia": None,
            "sabedoria": None,
            "carisma": None
        }

    def gerar_clássico(self):
        print("Estilo Clássico selecionado: 3d6 na ordem dos atributos.")
        for nome in self.AtributosRandom.keys():
            self.AtributosRandom[nome] = self.j.jogarTresDadosESomar()

    def gerar_aventureiro(self):
        print("Estilo Aventureiro selecionado: 3d6 com distribuição livre.")
        valores = [self.j.jogarTresDadosESomar() for _ in range(6)]
        print(f"Resultados: {valores}")
        self.distribuir_valores(valores)

    def gerar_heroico(self):
        print("Estilo Heroico selecionado: 4d6 descartando o menor, com distribuição livre.")
        valores = []
        for _ in range(6):
            resultado = self.j.valorDado()
            resultado.remove(min(resultado))
            valores.append(sum(resultado))
        print(f"Resultados: {valores}")
        self.distribuir_valores(valores)

    def distribuir_valores(self, valores):
        atributos = list(self.AtributosRandom.keys())
        for valor in valores:
            while True:
                print(f"\nAtributos disponíveis: {', '.join([a for a in atributos if self.AtributosRandom[a] is None])}")
                destino = input(f"Para qual atributo deseja atribuir o valor {valor}? ").lower()
                if destino in atributos and self.AtributosRandom[destino] is None:
                    self.AtributosRandom[destino] = valor
                    break
                else:
                    print("Atributo inválido ou já preenchido. Tente novamente.")

    def descricao(self, atributo, valor):
        descricoes = {
            "forca": {
                (3, 8): "Fraco",
                (9, 12): "Mediano",
                (13, 16): "Forte",
                (17, 18): "Muito Forte"
            },
            "destreza": {
                (3, 8): "Letárgico",
                (9, 12): "Mediano",
                (13, 16): "Ágil",
                (17, 18): "Preciso"
            },
            "constituicao": {
                (3, 8): "Frágil",
                (9, 12): "Mediano",
                (13, 16): "Resistente",
                (17, 18): "Vigoroso"
            },
            "inteligencia": {
                (3, 8): "Inepto",
                (9, 12): "Mediano",
                (13, 16): "Inteligente",
                (17, 18): "Gênio"
            },
            "sabedoria": {
                (3, 8): "Tolo",
                (9, 12): "Mediano",
                (13, 16): "Intuitivo",
                (17, 18): "Presciente"
            },
            "carisma": {
                (3, 8): "Descortês",
                (9, 12): "Mediano",
                (13, 16): "Carismático",
                (17, 18): "Magnético"
            }
        }

        for (inicio, fim), desc in descricoes[atributo].items():
            if inicio <= valor <= fim:
                return desc
        return "Indefinido"

from .jogar_dado import JogarDado

class Atributos:
    def __init__(self):
        self.j = JogarDado()
        self.valores = {
            "forca": 0, "destreza": 0, "constituicao": 0,
            "inteligencia": 0, "sabedoria": 0, "carisma": 0
        }

    def gerar_classico(self):
        """ Gera 3d6 na ordem e retorna o dicionário de atributos preenchido. """
        for nome in self.valores.keys():
            self.valores[nome] = self.j.jogarTresDadosESomar()
        return self.valores

    def gerar_aventureiro(self):
        """ Retorna uma lista com 6 valores rolados com 3d6. """
        return [self.j.jogarTresDadosESomar() for _ in range(6)]

    def gerar_heroico(self):
        """ Retorna uma lista com 6 valores (4d6, descarta o menor). """
        valores_gerados = []
        for _ in range(6):
            rolagens = self.j.valorDado()
            rolagens.remove(min(rolagens))
            valores_gerados.append(sum(rolagens))
        return valores_gerados

    def descricao(self, atributo, valor):
        descricoes = {
            "forca": {(3, 8): "Fraco", (9, 12): "Mediano", (13, 16): "Forte", (17, 18): "Muito Forte"},
            "destreza": {(3, 8): "Letárgico", (9, 12): "Mediano", (13, 16): "Ágil", (17, 18): "Preciso"},
            "constituicao": {(3, 8): "Frágil", (9, 12): "Mediano", (13, 16): "Resistente", (17, 18): "Vigoroso"},
            "inteligencia": {(3, 8): "Inepto", (9, 12): "Mediano", (13, 16): "Inteligente", (17, 18): "Gênio"},
            "sabedoria": {(3, 8): "Tolo", (9, 12): "Mediano", (13, 16): "Intuitivo", (17, 18): "Presciente"},
            "carisma": {(3, 8): "Descortês", (9, 12): "Mediano", (13, 16): "Carismático", (17, 18): "Magnético"}
        }
        for (inicio, fim), desc in descricoes.get(atributo, {}).items():
            if inicio <= valor <= fim:
                return desc
        return "Indefinido"
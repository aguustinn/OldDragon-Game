import random

class JogarDado:

    def valorDado(self):
        # Rola 4d6
        return [random.randint(1, 6) for _ in range(4)]

    def jogarTresDadosESomar(self):
        # Rola 3d6
        return sum(random.randint(1, 6) for _ in range(3))

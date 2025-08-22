class Raca:
    
    def __init__(self):
        self.raca = None 

    def escolhaRaca(self, raca):
        if raca == 1:
            self.raca = "Elfo"
        elif raca == 2:
            self.raca = "Anão"
        elif raca == 3:
            self.raca = "Humano"
        elif raca == 4:
            self.raca = "Gnomo"
        elif raca == 5:
            self.raca = "Meio Elfo"
        elif raca == 6:
            self.raca = "Halfing"
        else:
            self.raca = "Desconhecida"
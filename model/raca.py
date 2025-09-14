class Raca:
    def __init__(self, nome=""):
        self.nome = nome
        self.movimento = None
        self.infravisao = None
        self.alinhamento = None
        self.peso = None
        self.faixa_etaria = None
        if nome:
            self._definir_atributos_base()

    def _definir_atributos_base(self):
        dados_racas = {
            "Humano": {"mov": "9m", "infra": "Não", "alin": "Qualquer", "peso": 80},
            "Elfo": {"mov": "9m", "infra": "18m", "alin": "Neutro", "peso": 60},
            "Anão": {"mov": "6m", "infra": "18m", "alin": "Ordem", "peso": 75},
            "Gnomo": {"mov": "6m", "infra": "18m", "alin": "Neutro", "peso": 40},
            "Meio Elfo": {"mov": "9m", "infra": "9m", "alin": "Caos", "peso": 65},
            "Halfling": {"mov": "6m", "infra": "Não", "alin": "Neutro", "peso": 35}
        }
        if self.nome in dados_racas:
            info = dados_racas[self.nome]
            self.movimento = info["mov"]
            self.infravisao = info["infra"]
            self.alinhamento = info["alin"]
            self.peso = info["peso"]

    def definir_faixa_etaria(self, idade):
        limites = {
            "Humano": (15, 45, 90),
            "Elfo": (120, 450, 900),
            "Anão": (50, 120, 350),
            "Gnomo": (20, 150, 350),
            "Meio Elfo": (25, 80, 180),
            "Halfling": (20, 50, 100)
        }
        if self.nome in limites:
            jovem, adulto, meia_idade = limites[self.nome]
            if idade < jovem: self.faixa_etaria = "Jovem"
            elif idade < adulto: self.faixa_etaria = "Adulto"
            elif idade < meia_idade: self.faixa_etaria = "Meia-Idade"
            else: self.faixa_etaria = "Idoso"
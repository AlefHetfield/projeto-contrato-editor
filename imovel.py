class Imovel:
    def __init__(self, tipo):
        self.tipo = tipo # Uma casa, Um apartamento, Um terreno
        self.matricula = ''
        self.endereco = ''
        self.cartorio = ''

    def __str__(self):
        return f'{self.tipo} localizado na {self.endereco}, objeto da matrícula nº {self.matricula}, do {self.cartorio}, assim descrito e caracterizado, denominado'
class Imovel:
    def __init__(self, tipo):
        self.tipo = tipo # Imóvel
        self.categoria = ''
        self.numero_da_matricula = ''
        self.endereco_do_imovel = '' 

    def coletar_dados(self):
        print(f'Cadastro do {self.tipo}')
        self.categoria = input(f'Digite se o {self.tipo} em questão é uma casa ou apartamento: ')
        self.numero_da_matricula = input(f'Digite o número da matrícula do {self.tipo}: ')
        self.endereco_do_imovel = input(f'Digite o endereço completo do {self.tipo}: ')

    def __str__(self):
        print(self.tipo.upper())
        return f'{self.categoria} | {self.numero_da_matricula} | {self.endereco_do_imovel}\n'
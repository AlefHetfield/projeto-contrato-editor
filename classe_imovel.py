class Imovel:
    def __init__(self, tipo):
        self.tipo = tipo # Imóvel
        self.categoria = ''
        self.numero_da_matricula = ''
        self.cartorio = ''
        self.endereco_do_imovel = '' 

    def coletar_dados(self):
        print(f'Cadastro do {self.tipo}')
        self.categoria = input(f'Digite se o {self.tipo} em questão é uma casa ou apartamento: ')
        self.numero_da_matricula = input(f'Digite o número da matrícula do {self.tipo}: ')
        self.cartorio = input(f'Digite o cartório responsável pelo {self.tipo}: ')
        self.endereco_do_imovel = input(f'Digite o endereço completo do {self.tipo}: ')

    def __str__(self):
        print(self.tipo.upper())
        print('Categoria'.ljust(20), '| Matrícula'.ljust(20), '| Cartório'.ljust(20), '| Endereço'.ljust(20))
        return f'{self.categoria.ljust(20)} | {self.numero_da_matricula.ljust(20)}| {self.cartorio.ljust(20)}| {self.endereco_do_imovel.ljust(20)}\n'
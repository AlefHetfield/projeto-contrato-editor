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
        header = f'{'Categoria':<40} | {'Matrícula':<15} | {'Cartório':<15} | {'Endereço':<25}'
        data = f'{self.categoria:<40} | {self.numero_da_matricula:<15} | {self.cartorio:<15} | {self.endereco_do_imovel:<25}'
        return f'{self.tipo.upper()}\n{header}\n{data}\n'
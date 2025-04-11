class Pessoa:
    def __init__(self, tipo):
        self.tipo = tipo # Vendedor ou Comprador
        self.nome = ''
        self.cpf = ''
        self.rg = ''
        self.endereco = ''

    def coletar_dados(self):
        print(f'Cadastro do {self.tipo}')
        self.nome = input(f'Digite o nome do {self.tipo}: ')
        self.cpf = input(f'Digite o CPF do {self.tipo}: ')
        self.rg = input(f'Digite o RG do {self.tipo}: ')
        self.endereco = input(f'Digite o Endereço Completo do {self.tipo}: ')

    def __str__(self):
        print(self.tipo.upper())
        return f'{self.nome} | {self.cpf} | {self.rg} | {self.endereco}\n'
    
    def editar_dado(self):
        while True:
            print(f'\nEditar dados do {self.tipo}')
            print('[1] Nome')
            print('[2] CPF')
            print('[3] RG')
            print('[4] Endereço')
            print('[5] Voltar')
            opcao = input('\nEscolha a opção que deseja alterar: ')
            if opcao == '1':
                self.nome = input('Digite o novo Nome: ')
            elif opcao == '2':
                self.cpf = input('Digite o novo CPF: ')
            elif opcao == '3':
                self.rg = input('Digite o novo RG: ')
            elif opcao == '4':
                self.endereco = input('Digite o novo Endereço: ')
            elif opcao == '5':
                break
            else:
                print('Opção inválida. Digite novamente.')

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
        return f'{self.tipo.categoria} | {self.tipo.numero_da_matricula} | {self.tipo.endereco_do_imovel}\n'

# vendedor = Pessoa("Vendedor")
# vendedor.coletar_dados()
# print(vendedor)

# vendedor.editar_dado()

# print(vendedor)
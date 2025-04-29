class Imovel:
    def __init__(self, tipo):
        self.tipo = tipo # Imóvel
        self.categoria = ''
        self.numero_da_matricula = ''
        self.cartorio = ''
        self.endereco_do_imovel = '' 

    def coletar_dados(self):
        print(f'CADASTRO DO {self.tipo}\n'.upper())
        self.categoria = input(f'Digite se o {self.tipo} em questão é uma casa ou apartamento: ')
        self.numero_da_matricula = input(f'Digite o número da matrícula do {self.tipo}: ')
        self.cartorio = input(f'Digite o cartório responsável pelo {self.tipo}: ')
        self.endereco_do_imovel = input(f'Digite o endereço completo do {self.tipo}: ')

    def __str__(self):
        return f'{self.tipo.upper()}\nCategoria: {self.categoria}\nNúmero da Matrícula: {self.numero_da_matricula}\nCartório: {self.cartorio}\nEndereço: {self.endereco_do_imovel}\n'
    
    def editar_dados(self):
        while True:
            print(f'\nEditar dados do {self.tipo}')
            print('[1] Categoria')
            print('[2] Matricula')
            print('[3] Cartório')
            print('[4] Endereço')
            print('[5] Voltar')
            opcao = input('\nEscolha a opção que deseja alterar: ')
            if opcao == '1':
                self.categoria = input('Digite o nova Categoria: ')
                print(f'Categoria alterado para: {self.categoria}')
                input('Digite [ENTER] para voltar.')
                break
            elif opcao == '2':
                self.numero_da_matricula = input('Digite a nova Matricula: ')
                print(f'Matricula alterada para: {self.numero_da_matricula}')
                input('Digite [ENTER] para voltar.')
                break
            elif opcao == '3':
                self.cartorio = input('Digite o novo Cartório: ')
                print(f'RG alterado para: {self.cartorio}')
                input('Digite [ENTER] para voltar.')
                break
            elif opcao == '4':
                self.endereco_do_imovel = input('Digite o novo Endereço: ')
                print(f'Endereço alterado para: {self.endereco_do_imovel}')
                input('Digite [ENTER] para voltar.')
                break
            elif opcao == '5':
                break
            else:
                print('Opção inválida. Digite novamente.')
    
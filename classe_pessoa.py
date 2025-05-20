class Pessoa:
    def __init__(self, tipo):
        self.tipo = tipo # Vendedor ou Comprador
        self.nome = ''
        self.cpf = ''
        self.rg = ''
        self.endereco = ''

    def coletar_dados(self):
        print(f'CADASTRO DO {self.tipo}\n'.upper())
        self.nome = input(f'Digite o nome do {self.tipo}: ')
        self.cpf = input(f'Digite o CPF do {self.tipo}: ')
        self.rg = input(f'Digite o RG do {self.tipo}: ')
        self.estado_civil = input(f'Digite o estado civil do {self.tipo}: ')
        self.endereco = input(f'Digite o Endereço Completo do {self.tipo}: ')

    def coletar_dados_segundo_participante(self):
        print(f'CADASTRO DO {self.tipo}\n'.upper())
        self.nome = input(f'Digite o nome do {self.tipo}: ')
        self.cpf = input(f'Digite o CPF do {self.tipo}: ')
        self.rg = input(f'Digite o RG do {self.tipo}: ')

        while True:
            endereco_segundo_participante = input('O endereço é o mesmo do primeiro participante? [S/N]: ').strip().upper()
            if endereco_segundo_participante == 'N':
                self.endereco = input(f'Digite o Endereço Completo do {self.tipo}: ')
                break

            elif endereco_segundo_participante == 'S':
                self.endereco == {self.endereco}
                break

            else:
                print('Digite uma opção válida!\n')


    def __str__(self):
        return f'{self.tipo.upper()}\nNome: {self.nome}\nCPF: {self.cpf}\nRG: {self.rg}\nEstado Civil: {self.estado_civil}\nEndereço: {self.endereco}\n'
    
    def editar_dados(self):
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
                print(f'Nome alterado para: {self.nome}')
                input('Digite [ENTER] para voltar.')
                break
            elif opcao == '2':
                self.cpf = input('Digite o novo CPF: ')
                print(f'CPF alterado para: {self.cpf}')
                input('Digite [ENTER] para voltar.')
                break
            elif opcao == '3':
                self.rg = input('Digite o novo RG: ')
                print(f'RG alterado para: {self.rg}')
                input('Digite [ENTER] para voltar.')
                break
            elif opcao == '4':
                self.endereco = input('Digite o novo Endereço: ')
                print(f'Endereço alterado para: {self.endereco}')
                input('Digite [ENTER] para voltar.')
                break
            elif opcao == '5':
                break
            else:
                print('Opção inválida. Digite novamente.')



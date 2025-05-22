class Valores:
    def __init__(self, tipo):
        self.tipo = tipo # Valores
        self.banco = ''
        self.valor_do_imovel = ''
        self.sinal = ''
        self.fgts = ''
        self.recursos_proprios = ''
        self.financiamento = '' 

    def coletar_dados(self):
        print('CADASTRO DOS DADOS DA NEGOCIAÇÃO\n')
        self.banco = input('Banco a financiar: ')
        self.valor_do_imovel = int(input('Valor do imóvel: R$ '))    
        self.sinal = int(input('Valor do sinal. Caso não se aplique, deixe em branco: R$ '))
        self.fgts = int(input('Valor do FGTS. Caso não se aplique, deixe em branco: R$ '))
        self.recursos_proprios = int(input('Valor de recursos próprios. Caso não se aplique, deixe em branco: R$ '))
        self.financiamento = int(input('Valor do financiamento: R$ '))

    def __str__(self):
        return f'{self.tipo.upper()}\nBanco: {self.banco}\nValor do Imóvel: R$ {self.valor_do_imovel}\nSinal: R$ {self.sinal}\nFGTS: R$ {self.fgts}\nRecursos Próprios: R$ {self.recursos_proprios}\nFinanciamento: R$ {self.financiamento}'
    
    def editar_dados(self):
        while True:
            print(f'\nEditar dados dos {self.tipo}')
            print('[1] Nome do Banco')
            print('[2] Valor do Imóvel')
            print('[3] Valor do Sinal')
            print('[4] Valor do FGTS')
            print('[5] Valor em Recursos Próprios')
            print('[6] Valor do Financiamento')
            print('[7] Voltar')
            opcao = input('\nEscolha a opção que deseja alterar: ')
            if opcao == '1':
                self.banco = input('Digite o novo nome do banco: ')
                print(f'Banco alterado para: {self.banco}')
                input('Digite [ENTER] para voltar.')
                break            
            elif opcao == '2':
                self.valor_do_imovel = input(int('Digite o novo valor: R$ '))
                print(f'Valor do Imóvel alterado para: R$ {self.valor_do_imovel}')
                input('Digite [ENTER] para voltar.')
                break
            elif opcao == '3':
                self.sinal = input(int('Digite o novo valor: R$ '))
                print(f'Valor do Sinal alterado para: R$ {self.sinal}')
                input('Digite [ENTER] para voltar.')
                break
            elif opcao == '4':
                self.fgts = input(int('Digite o novo valor: R$ '))
                print(f'Valor de FGTS alterado para: R$ {self.fgts}')
                input('Digite [ENTER] para voltar.')
                break
            elif opcao == '5':
                self.recursos_proprios = input(int('Digite o novo valor: R$ '))
                print(f'Valor de Recursos Próprios alterado para: R$ {self.recursos_proprios}')
                input('Digite [ENTER] para voltar.')
                break
            elif opcao == '6':
                self.financiamento = input(int('Digite o novo valor: R$ '))
                print(f'Valor de Financiamento alterado para: R$ {self.financiamento}')
                input('Digite [ENTER] para voltar.')
                break
            elif opcao == '7':
                break
            else:
                print('Opção inválida. Digite novamente.')
    
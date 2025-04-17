class Valores:
    def __init__(self, tipo):
        self.tipo = tipo # Valores
        self.valor_do_imovel = ''
        self.sinal = ''
        self.fgts = ''
        self.recursos_proprios = ''
        self.financiamento = '' 

    def coletar_dados(self):
        print('CADASTRO DOS VALORES DA NEGOCIAÇÃO\n')
        self.valor_do_imovel = input('Valor do imóvel: R$ ')    
        self.sinal = input('Valor do sinal. Caso não se aplique, deixe em branco: R$ ')
        self.fgts = input('Valor do FGTS. Caso não se aplique, deixe em branco: R$ ')
        self.recursos_proprios = input('Valor de recursos próprios: R$ ')
        self.financiamento = input('Valor do financiamento: R$ ')

    def __str__(self):
        return f'{self.tipo.upper()}\nValor do Imóvel: R$ {self.valor_do_imovel}\nSinal: R$ {self.sinal}\nFGTS: R$ {self.fgts}\nRecursos Próprios: R$ {self.recursos_proprios}\nFinanciamento: R$ {self.financiamento}'
    
    def editar_dados(self):
        while True:
            print(f'\nEditar dados dos {self.tipo}')
            print('[1] Valor do Imóvel')
            print('[2] Valor do Sinal')
            print('[3] Valor do FGTS')
            print('[4] Valor em Recursos Próprios')
            print('[5] Valor do Financiamento')
            print('[6] Voltar')
            opcao = input('\nEscolha a opção que deseja alterar: ')
            if opcao == '1':
                self.valor_do_imovel = input('Digite o novo valor: R$ ')
                print(f'Valor do Imóvel alterado para: R$ {self.valor_do_imovel}')
                input('Digite [ENTER] para voltar.')
                break
            elif opcao == '2':
                self.sinal = input('Digite o novo valor: R$ ')
                print(f'Valor do Sinal alterado para: R$ {self.sinal}')
                input('Digite [ENTER] para voltar.')
                break
            elif opcao == '3':
                self.fgts = input('Digite o novo valor: R$ ')
                print(f'Valor de FGTS alterado para: R$ {self.fgts}')
                input('Digite [ENTER] para voltar.')
                break
            elif opcao == '4':
                self.recursos_proprios = input('Digite o novo valor: R$ ')
                print(f'Valor de Recursos Próprios alterado para: R$ {self.recursos_proprios}')
                input('Digite [ENTER] para voltar.')
                break
            elif opcao == '5':
                self.financiamento = input('Digite o novo valor: R$ ')
                print(f'Valor de Financiamento alterado para: R$ {self.financiamento}')
                input('Digite [ENTER] para voltar.')
                break
            elif opcao == '6':
                break
            else:
                print('Opção inválida. Digite novamente.')
    
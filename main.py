from docx import Document
from docx2pdf import convert
from num2words import num2words as extenso
from datetime import datetime
from babel.dates import format_date
import os
from classe_pessoa import Pessoa
from classe_imovel import Imovel
from classe_valores import Valores

doc = Document("contrato_motive.docx")

def main(): # Função principal que inicia o programa
    comprador = ''
    comprador_2 = ''
    vendedor = ''
    vendedor_2 = ''
    imovel = ''
    valores = ''
    tela_limpa()
    while True:
        tela_limpa()
        print('MENU PRINCIPAL\n')
        print('[1] Cadastrar Informações')
        print('[2] Exibir Dados do Contrato')
        print('[3] Salvar Arquivo')
        print('[4] Converter para PDF')
        print('[5] Sair\n')
        
        opcao_escolhida = input('Digite a opção desejada: ')
        
        if opcao_escolhida == '1':
            while True:
                tela_limpa()
                print('CADASTRO DE INFORMAÇÕES\n')
                print('[1] Cadastrar Vendedores')
                print('[2] Cadastrar Compradores')
                print('[3] Cadastrar Imóvel')
                print('[4] Cadastrar Dados da Negociação')
                print('[5] Editar Dados Cadastrados')
                print('[6] Voltar ao Menu Principal\n')
                opcao_cadastro = input('Quem gostaria de cadastrar: ')
                
                if opcao_cadastro == '1':
                    tela_limpa()
                    vendedor = Pessoa("Vendedor")
                    vendedor.coletar_dados()
                    print('\nVENDEDOR CADASTRADO COM SUCESSO!\n')
                    
                    while True:
                        segundo_vendedor = input('Cadastrar mais um vendedor? [S/N]: ').strip().upper()
                        if segundo_vendedor == 'S':
                            tela_limpa()
                            vendedor_2 = Pessoa("Vendedor 2")
                            vendedor_2.coletar_dados()
                            print('\nSEGUNDO VENDEDOR CADASTRADO COM SUCESSO!\n')
                            input('Digite [ENTER] para voltar: ')
                            break                        
                        elif segundo_vendedor == 'N':
                            print('Voltando ao menu de cadastro... ')
                            break
                        else:
                            print('Digite uma opção válida!\n')

                
                elif opcao_cadastro == '2':
                    tela_limpa()
                    comprador = Pessoa("Comprador")
                    comprador.coletar_dados()
                    print('\nCOMPRADOR CADASTRADO COM SUCESSO!\n')
                    
                    while True:
                        segundo_comprador = input('Cadastrar mais um comprador? [S/N]: ').strip().upper()
                        if segundo_comprador == 'S':
                            tela_limpa()
                            comprador_2 = Pessoa("Comprador 2")
                            comprador_2.coletar_dados()
                            print('\nSEGUNDO COMPRADOR CADASTRADO COM SUCESSO!\n')
                            input('Digite [ENTER] para voltar: ')
                            break                        
                        elif segundo_comprador == 'N':
                            print('Voltando ao menu de cadastro... ')
                            break
                        else:
                            print('Digite uma opção válida!\n')

                elif opcao_cadastro == '3':
                    tela_limpa()
                    imovel = Imovel("Imóvel")
                    imovel.coletar_dados()
                    print('\nIMÓVEL CADASTRADO COM SUCESSO!\n')
                    input('Digite [ENTER] para voltar: ')

                elif opcao_cadastro == '4':
                    tela_limpa()
                    valores = Valores("Valores")
                    valores.coletar_dados()
                    print('\nVALORES CADASTRADOS COM SUCESSO!\n')
                    input('Digite [ENTER] para voltar: ')
                
                elif opcao_cadastro == '5':
                    tela_limpa()
                    print('EDITAR DADOS CADASTRADOS\n')
                    print('[1] Editar Vendedores')
                    print('[2] Editar Compradores')
                    print('[3] Editar Imóvel')
                    print('[4] Editar Valores')
                    print('[5] Voltar\n')
                    opcao_editar = input('Escolha uma opção: ')

                    if opcao_editar == '1':
                        if not vendedor:
                            print('\nNenhum vendedor cadastrado.\n')
                            input('Digite [ENTER] para voltar.')
                            break
                        else:
                            tela_limpa()
                            print(vendedor)
                            print(vendedor_2)
                            print('-' * 30)
                            
                        while True:
                            editar_vendedores = input('\nQual vendedor você deseja editar? [1/2]: ').strip().upper()
                            if editar_vendedores == '1':
                                vendedor.editar_dados()
                                break
                                                      
                            elif editar_vendedores == '2':
                                if not vendedor_2:
                                    print('\nVendedor 2 não cadastrado.\n')
                                    input('Digite [ENTER] para voltar.')
                                    break

                                else:
                                    vendedor_2.editar_dados()
                                    break

                            else:
                                print('Digite uma opção válida!\n')

                    elif opcao_editar == '2':
                        if not comprador:
                            print('\nNenhum comprador cadastrado.\n')
                            input('Digite [ENTER] para voltar.')
                            break
                        else:
                            tela_limpa()
                            print(comprador)
                            print(comprador_2)
                            print('-' * 30)
                            
                        while True:
                            editar_compradores = input('\nQual comprador você deseja editar? [1/2]: ').strip().upper()
                            if editar_compradores == '1':
                                comprador.editar_dados()
                                break
                                                      
                            elif editar_compradores == '2':
                                if not comprador_2:
                                    print('\nComprador 2 não cadastrado.\n')
                                    input('Digite [ENTER] para voltar.')
                                    break

                                else:   
                                    comprador_2.editar_dados()
                                    break

                            else:
                                print('Digite uma opção válida!\n')

                    elif opcao_editar == '3':
                        if not imovel:
                            print('\nNenhum imóvel cadastrado.\n')
                            input('Digite [ENTER] para voltar.')
                            break
                        else:
                            tela_limpa()
                            print(imovel)
                            print('-' * 30)
                            imovel.editar_dados()

                    elif opcao_editar == '4':
                        if not valores:
                            print('\nNenhum valor cadastrado.\n')
                            input('Digite [ENTER] para voltar.')
                            break
                        else:
                            tela_limpa()
                            print(valores)
                            print('-' * 30)
                            valores.editar_dados()

                    elif opcao_editar == '5':
                        break

                    else:
                        print('Opção inválida.')
                    
                elif opcao_cadastro == '6':
                    break    
            continue

        elif opcao_escolhida == '2':
            tela_limpa()
            print('-' * 30 + '\n')
            print(vendedor, '\n')
            print(vendedor_2, '\n')
            print('-' * 30 + '\n')
            print(comprador, '\n')
            print(comprador_2, '\n')
            print('-' * 30 + '\n')
            print(imovel, '\n')
            print('-' * 30 + '\n')
            print(valores, '\n')
            print('-' * 30 + '\n')
            input('\nDigite [ENTER] para voltar: ')

        elif opcao_escolhida == '3':
            if vendedor_2 != '' and comprador_2 != '':
                substituir_texto('PARAGRAFO_VENDEDOR', f'{vendedor.nome.upper()}, {vendedor.estado_civil.lower()}, inscrito(a) na cédula de identidade RG n° {vendedor.rg}, inscrito(a) no CPF sob n°{vendedor.cpf} e {vendedor_2.nome.upper()}, {vendedor_2.estado_civil.lower()}, inscrito(a) na cédula de identidade RG n° {vendedor_2.rg}, inscrito(a) no CPF sob n° {vendedor_2.cpf}, residente(s) e domiciliado(s) à {vendedor.endereco}.')
                substituir_texto('PARAGRAFO_COMPRADOR', f'{comprador.nome.upper()}, {comprador.estado_civil.lower()}, inscrito(a) na cédula de identidade RG n° {comprador.rg}, inscrito(a) no CPF sob n°{comprador.cpf} e {comprador_2.nome.upper()}, {comprador_2.estado_civil.lower()}, inscrito(a) na cédula de identidade RG n° {comprador_2.rg}, inscrito(a) no CPF sob n° {comprador_2.cpf}, residente(s) e domiciliado(s) à {comprador.endereco}.')
                substituir_texto('NOME_VENDEDOR', vendedor.nome)
                substituir_texto('NOME_SEGUNDO_VENDEDOR', vendedor_2.nome)
                substituir_texto('NOME_COMPRADOR', comprador.nome)                
                substituir_texto('NOME_SEGUNDO_COMPRADOR', comprador_2.nome)

            elif vendedor_2 == '' and comprador_2 == '':
                substituir_texto('PARAGRAFO_VENDEDOR', f'{vendedor.nome.upper()}, {vendedor.estado_civil.lower()}, inscrito(a) na cédula de identidade RG n° {vendedor.rg}, inscrito(a) no CPF sob n°{vendedor.cpf}, residente(s) e domiciliado(s) à {vendedor.endereco}.')
                substituir_texto('PARAGRAFO_COMPRADOR', f'{comprador.nome.upper()}, {comprador.estado_civil.lower()}, inscrito(a) na cédula de identidade RG n° {comprador.rg}, inscrito(a) no CPF sob n°{comprador.cpf}, residente(s) e domiciliado(s) à {comprador.endereco}.')
                substituir_texto('NOME_VENDEDOR', vendedor.nome)
                substituir_texto('NOME_COMPRADOR', comprador.nome) 

            elif vendedor_2 != '' and comprador_2 == '':
                substituir_texto('PARAGRAFO_VENDEDOR', f'{vendedor.nome.upper()}, {vendedor.estado_civil.lower()}, inscrito(a) na cédula de identidade RG n° {vendedor.rg}, inscrito(a) no CPF sob n°{vendedor.cpf} e {vendedor_2.nome.upper()}, {vendedor_2.estado_civil.lower()}, inscrito(a) na cédula de identidade RG n° {vendedor_2.rg}, inscrito(a) no CPF sob n° {vendedor_2.cpf}, residente(s) e domiciliado(s) à {vendedor.endereco}.')
                substituir_texto('PARAGRAFO_COMPRADOR', f'{comprador.nome.upper()}, {comprador.estado_civil.lower()}, inscrito(a) na cédula de identidade RG n° {comprador.rg}, inscrito(a) no CPF sob n°{comprador.cpf}, residente(s) e domiciliado(s) à {comprador.endereco}.')
                substituir_texto('NOME_VENDEDOR', vendedor.nome)
                substituir_texto('NOME_SEGUNDO_VENDEDOR', vendedor_2.nome)
                substituir_texto('NOME_COMPRADOR', comprador.nome)

            elif vendedor_2 == '' and comprador_2 != '':
                substituir_texto('PARAGRAFO_VENDEDOR', f'{vendedor.nome.upper()}, {vendedor.estado_civil.lower()}, inscrito(a) na cédula de identidade RG n° {vendedor.rg}, inscrito(a) no CPF sob n°{vendedor.cpf}, residente(s) e domiciliado(s) à {vendedor.endereco}.')
                substituir_texto('PARAGRAFO_COMPRADOR', f'{comprador.nome.upper()}, {comprador.estado_civil.lower()}, inscrito(a) na cédula de identidade RG n° {comprador.rg}, inscrito(a) no CPF sob n°{comprador.cpf} e {comprador_2.nome.upper()}, {comprador_2.estado_civil.lower()}, inscrito(a) na cédula de identidade RG n° {comprador_2.rg}, inscrito(a) no CPF sob n° {comprador_2.cpf}, residente(s) e domiciliado(s) à {comprador.endereco}.')    
                substituir_texto('NOME_VENDEDOR', vendedor.nome)
                substituir_texto('NOME_COMPRADOR', comprador.nome)                
                substituir_texto('NOME_SEGUNDO_COMPRADOR', comprador_2.nome)           

            else:
                print("Preencha os dados corretamente antes de salvar o arquivo.")

            substituir_texto('PARAGRAFO_IMOVEL', f'Um(a) {imovel.categoria.lower()} localizado(a) na {imovel.endereco_do_imovel}, objeto da matrícula nº {imovel.numero_da_matricula}, do Oficial de Registro de Imóveis de {imovel.cartorio}, assim descrito e caracterizado, denominado “imóvel”.')

            substituir_texto('VALOR_DO_IMOVEL', valores.valor_do_imovel)
            substituir_texto('VALOR_SINAL', valores.sinal)
            substituir_texto('VALOR_FGTS', valores.fgts)
            substituir_texto('VALOR_RECURSOS', valores.recursos_proprios)
            substituir_texto('VALOR_FINANCIAMENTO', valores.financiamento)
            substituir_texto('NOME_BANCO', valores.banco)
            
            # Obtém a data atual
            data_atual = datetime.now()
            # Formata a data com o mês por extenso em português
            data_formatada = format_date(data_atual, format='d \'de\' MMMM \'de\' y', locale='pt_BR')
            substituir_texto('DATA_ATUAL', data_formatada)
            
            nome_arquivo = input('Digite o nome do arquivo que deseja salvar: ')
            doc.save(f'{nome_arquivo}.docx')

        elif opcao_escolhida == '4':
            convert(f'{nome_arquivo}.docx', f'{nome_arquivo}.pdf')
        
        elif opcao_escolhida == '5':
            os.system('cls')
            print('TCHAU. ATÉ A PRÓXIMA!')
            print('\n© Motive Consultoria Imobiliária LTDA.\n')
            break




def substituir_texto(marcador, novo_valor):
    """
    Substitui o texto de um marcador no documento preservando a formatação.
    
    marcador: Texto do marcador a ser substituído
    novo_valor: Novo valor que substituirá o marcador
    """
    for paragrafo in doc.paragraphs:
        if marcador in paragrafo.text:
            for run in paragrafo.runs:
                if marcador in run.text:
                    run.text = run.text.replace(marcador, novo_valor)

def exibir_nome_programa(): # Exibe o nome do programa na tela
    print('''

    █▀▀ █▀▀█ █▀▀▄ ▀▀█▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀ 　 █▀▄▀█ █▀▀█ ▀▀█▀▀ ░▀░ ▀█░█▀ █▀▀ 
    █░░ █░░█ █░░█ ░░█░░ █▄▄▀ █▄▄█ ░░█░░ █░░█ ▀▀█ 　 █░▀░█ █░░█ ░░█░░ ▀█▀ ░█▄█░ █▀▀ 
    ▀▀▀ ▀▀▀▀ ▀░░▀ ░░▀░░ ▀░▀▀ ▀░░▀ ░░▀░░ ▀▀▀▀ ▀▀▀ 　 ▀░░░▀ ▀▀▀▀ ░░▀░░ ▀▀▀ ░░▀░░ ▀▀▀
    ''')

def tela_limpa(): #Limpa a tela e exibe o nome do programa
    os.system('cls')
    exibir_nome_programa()







if __name__ == '__main__':
    main()



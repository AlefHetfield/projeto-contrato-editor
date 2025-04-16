from docx import Document
from docx2pdf import convert
from num2words import num2words as extenso
import os
from classe_pessoa import Pessoa
from classe_imovel import Imovel

doc = Document("contrato_motive.docx")

def main(): # Função principal que inicia o programa
    comprador = ''
    vendedor = ''
    imovel = ''
    tela_limpa()
    while True:
        tela_limpa()
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
                print('[4] Cadastrar Valores da Negociação')
                print('[5] Editar Dados Cadastrados')
                print('[6] Voltar ao Menu Principal\n')
                opcao_cadastro = input('Quem gostaria de cadastrar: ')
                
                if opcao_cadastro == '1':
                    tela_limpa()
                    vendedor = Pessoa("Vendedor")
                    vendedor.coletar_dados()
                    print('\nVENDEDOR CADASTRADO COM SUCESSO!\n')
                    input('Digite [ENTER] para voltar: ')
                
                elif opcao_cadastro == '2':
                    tela_limpa()
                    comprador = Pessoa("Comprador")
                    comprador.coletar_dados()
                    print('\nCOMPRADOR CADASTRADO COM SUCESSO!\n')
                    input('Digite [ENTER] para voltar: ')

                elif opcao_cadastro == '3':
                    tela_limpa()
                    imovel = Imovel("Imóvel")
                    imovel.coletar_dados()
                    print('\nIMÓVEL CADASTRADO COM SUCESSO!\n')
                    input('Digite [ENTER] para voltar: ')
                
                elif opcao_cadastro == '5':
                    tela_limpa()
                    print('EDITAR DADOS CADASTRADOS\n')
                    print('[1] Editar Vendedor')
                    print('[2] Editar Comprador')
                    print('[3] Editar Imóvel')
                    print('[4] Voltar\n')
                    opcao_editar = input('Escolha uma opção: ')

                    if opcao_editar == '1':
                        if not vendedor:
                            print('\nNenhum vendedor cadastrado.\n')
                            input('Digite [ENTER] para voltar.')
                            break
                        else:
                            tela_limpa()
                            print(vendedor)
                            print('-' * 30)
                            vendedor.editar_dados()

                    elif opcao_editar == '2':
                        if not comprador:
                            print('\nNenhum comprador cadastrado.\n')
                            input('Digite [ENTER] para voltar.')
                            break
                        else:
                            tela_limpa()
                            print(comprador)
                            print('-' * 30)
                            comprador.editar_dados()

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
                        break

                    else:
                        print('Opção inválida.')
                    
                elif opcao_cadastro == '6':
                    break    
            continue

        if opcao_escolhida == '2':
            tela_limpa()
            print(vendedor)
            print('-' * 30)
            print(comprador)
            print('-' * 30)
            print(imovel)
            input('Digite [ENTER] para voltar: ')

        if opcao_escolhida == '3':
            substituir_texto('NOME_VENDEDOR', vendedor.nome.upper())
            substituir_texto('CPF_VENDEDOR', vendedor.cpf)
            substituir_texto('RG_VENDEDOR', vendedor.rg)
            substituir_texto('ENDERECO_VENDEDOR', vendedor.endereco)
        
            nome_arquivo = input('Digite o nome do arquivo que deseja salvar: ')
            doc.save(f'{nome_arquivo}.docx')


        
        if opcao_escolhida == '5':
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



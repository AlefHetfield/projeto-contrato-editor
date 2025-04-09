from docx import Document
from docx2pdf import convert
from num2words import num2words as extenso
import os
from classe_pessoa import Pessoa

compradores = {}
vendedores = {}

doc = Document("contrato_teste.docx")

def main(): # Função principal que inicia o programa
    os.system('cls')
    exibir_nome_programa()
    while True:
        menu_principal()
        escolher_opcao_menu_principal()


def exibir_nome_programa(): # Exibe o nome do programa na tela
    print('''

    █▀▀ █▀▀█ █▀▀▄ ▀▀█▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀ 　 █▀▄▀█ █▀▀█ ▀▀█▀▀ ░▀░ ▀█░█▀ █▀▀ 
    █░░ █░░█ █░░█ ░░█░░ █▄▄▀ █▄▄█ ░░█░░ █░░█ ▀▀█ 　 █░▀░█ █░░█ ░░█░░ ▀█▀ ░█▄█░ █▀▀ 
    ▀▀▀ ▀▀▀▀ ▀░░▀ ░░▀░░ ▀░▀▀ ▀░░▀ ░░▀░░ ▀▀▀▀ ▀▀▀ 　 ▀░░░▀ ▀▀▀▀ ░░▀░░ ▀▀▀ ░░▀░░ ▀▀▀
    ''')

def encerrar_programa(): # Função para encerrar o programa
    os.system('cls')
    print('ENCERRANDO PROGRAMA...')

def menu_principal(): # Exibe o menu principal
    print('[1] Cadastrar Participantes')
    print('[2] Exibir Dados do Contrato')
    print('[3] Salvar Arquivo')
    print('[4] Converter para PDF')
    print('[5] Sair\n')

def escolher_opcao_menu_principal(): # Função para escolher a opção do menu principal
    while True:
        os.system('cls')
        exibir_nome_programa()
        menu_principal()
        opcao_escolhida = int(input('Digite a opção desejada: '))

        if opcao_escolhida == 1:
            while True:  
                os.system('cls')
                exibir_nome_programa()
                menu_cadastrar_participantes()
                opcao_cadastro = int(input('Digite a opção desejada: '))
                
                if opcao_cadastro == 1:
                    os.system('cls')
                    exibir_nome_programa()
                    coletar_dados_vendedores()
                    print('\nVENDEDOR CADASTRADO COM SUCESSO!\n')
                    input('Digite [ENTER] para voltar: ')
                elif opcao_cadastro == 2:
                    os.system('cls')
                    exibir_nome_programa()
                    coletar_dados_compradores()
                    print('\nCOMPRADOR CADASTRADO COM SUCESSO!\n')
                    input('Digite [ENTER] para voltar: ')
                elif opcao_cadastro == 3:
                    break             
                else:
                    print('Opção inválida! Tente novamente.')
                    menu_cadastrar_participantes()
            continue

        elif opcao_escolhida == 2:
            exibir_dados_contrato()
        elif opcao_escolhida == 3:
            salvar_arquivo()
        elif opcao_escolhida == 4:
            converter_em_PDF()
        elif opcao_escolhida == 5:
            encerrar_programa()
            break
        else:
            opcao_invalida()

def menu_cadastrar_participantes(): # Exibe o menu de cadastro de participantes
    print('CADASTRO DE PARTICIPANTES\n')
    print('[1] Cadastrar Vendedores')
    print('[2] Cadastrar Compradores')
    print('[3] Voltar ao Menu Principal\n')

def coletar_dados_vendedores(): # Coleta os dados dos vendedores
    global vendedores
    vendedores = {
        'nome': input('Digite o nome completo do Vendedor: '),
        'CPF': input('Digite o CPF do Vendedor: '),
        'RG' : input('Digite o RG do Vendedor: '),
        'endereço': input('Digite o endereço do Vendedor: ')
    }
    return vendedores

def coletar_dados_compradores(): # Coleta os dados dos compradores
    global compradores
    compradores = {
        'nome': input('Digite o nome completo do Comprador: '),
        'CPF': input('Digite o CPF do Comprador: '),
        'RG' : input('Digite o RG do Comprador: '),
        'endereço': input('Digite o endereço do Comprador: ')
    }
    return compradores

def exibir_dados_contrato(): # Exibe os dados do contrato coletados até o momento
    os.system('cls')
    exibir_nome_programa()
    print('VENDEDORES')
    if vendedores:
        print(f"{vendedores['nome']} | {vendedores ['CPF']} | {vendedores['RG']} | {vendedores['endereço']}")
    else:
        print('Nenhum vendedor cadastrado.')
    print('-' * 30)
    print('\nCOMPRADORES')
    if compradores:
        print(f"{compradores['nome']} | {compradores ['CPF']} | {compradores['RG']} | {compradores['endereço']}")
    else:
        print('Nenhum vendedor cadastrado.')
    input('\nDigite uma tecla para voltar: ')

def salvar_arquivo(): # Salva o arquivo com os dados coletados 
    nome_arquivo = input('Digite o nome do arquivo que deseja salvar: ')
    doc.save(f'{nome_arquivo}.docx')

def converter_em_PDF(texto): # Converte o arquivo .docx para .pdf
    convert(f'{texto}.docx', f'{texto}.pdf')

def voltar_ao_menu(): # Volta ao menu principal
    input('\nDigite uma tecla para voltar ao menu ')
    menu_principal()




if __name__ == '__main__':
    main()


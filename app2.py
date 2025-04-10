from docx import Document
from docx2pdf import convert
from num2words import num2words as extenso
import os
from classe_pessoa import Pessoa

doc = Document("contrato_teste.docx")

# Testando se vai chegar as mudanças pro Adriano
# Chegou mesmo!

def main(): # Função principal que inicia o programa
    comprador = ''
    vendedor = ''
    tela_limpa()
    while True:
        tela_limpa()
        print('[1] Cadastrar Participantes')
        print('[2] Exibir Dados do Contrato')
        print('[3] Salvar Arquivo')
        print('[4] Converter para PDF')
        print('[5] Sair\n')
        
        opcao_escolhida = input('Digite a opção desejada: ')
        
        if opcao_escolhida == '1':
            while True:
                tela_limpa()
                print('CADASTRO DE PARTICIPANTES\n')
                print('[1] Cadastrar Vendedores')
                print('[2] Cadastrar Compradores')
                print('[3] Voltar ao Menu Principal\n')
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
                    break    
            continue

        if opcao_escolhida == '2':
            tela_limpa()
            print(comprador)
            print('-' * 30)
            print(vendedor)
            input('Digite [ENTER] para voltar: ')

        if opcao_escolhida == '3':
            nome_arquivo = input('Digite o nome do arquivo que deseja salvar: ')
            doc.save(f'{nome_arquivo}.docx')



        if opcao_escolhida == '5':
            os.system('cls')
            print('TCHAU. ATÉ A PRÓXIMA!')
            print('\n© Motive Consultoria Imobiliária LTDA.\n')
            break



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



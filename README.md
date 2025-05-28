# Projeto Contrato

Este é um projeto em Python para gerenciar contratos, permitindo o cadastro de participantes (vendedores e compradores), exibição de dados, salvamento de arquivos `.docx` e conversão para PDF.

## Funcionalidades

- Cadastro de vendedores e compradores (com possibilidade de múltiplos participantes).
- Cadastro e edição de informações do imóvel negociado.
- Cadastro e edição de valores do negócio (valor do imóvel, sinal, financiamento, FGTS, recursos próprios).
- Exibição detalhada dos dados cadastrados (participantes, imóvel e valores).
- Geração automática do contrato em formato `.docx` preenchido com os dados fornecidos.
- Conversão do contrato gerado para o formato PDF.
- Validação e edição dos dados antes do salvamento final.
- Interface de linha de comando interativa.

## Como funciona

O programa é executado via terminal, guiando o usuário por menus para cadastrar todos os dados necessários dos participantes (vendedores e compradores), do imóvel e dos valores envolvidos. Após o cadastro, é possível revisar e editar qualquer informação antes de gerar o contrato.

O contrato é montado a partir de um template `.docx` (contrato_motive.docx), onde o código substitui marcadores por dados fornecidos pelo usuário. Em seguida, o arquivo pode ser salvo e convertido automaticamente para PDF.

## Tecnologias e Bibliotecas Utilizadas

- **Python 3**: Linguagem principal do projeto.
- **python-docx** (`docx`): Manipulação de arquivos Word (`.docx`), preenchendo o template com os dados do contrato.
- **docx2pdf**: Conversão automática do arquivo `.docx` gerado para PDF.
- **num2words**: Conversão de valores numéricos para texto por extenso (ex: valores monetários).
- **Babel**: Formatação de datas e valores monetários no padrão brasileiro (pt_BR).
- **datetime**: Para trabalhar com datas e horários.
- **os**: Utilitário para comandos do sistema e limpeza de tela.
- **Estrutura orientada a objetos**: O projeto conta com classes para representar Pessoas, Imóveis e Valores, organizando melhor o fluxo de dados.

## Estrutura do Código

- `main.py`: Arquivo principal, responsável pela interação com o usuário e orquestração do fluxo do programa.
- `classe_pessoa.py`: Define a classe Pessoa, responsável pelo cadastro e edição dos participantes.
- `classe_imovel.py`: Define a classe Imovel, para cadastro e manipulação dos dados do imóvel.
- `classe_valores.py`: Define a classe Valores, que gerencia os valores do negócio.

## Requisitos

- Python 3.8+
- Instale as dependências utilizando:
  ```bash
  pip install python-docx docx2pdf num2words Babel
  ```

## Como usar

1. Execute o `main.py`:
   ```bash
   python main.py
   ```
2. Siga o menu interativo para cadastrar os dados.
3. Após preencher e revisar os dados, salve o contrato e converta para PDF se desejar.

## Observações

- É necessário ter o arquivo de template `contrato_motive.docx` na mesma pasta do script para que a geração do contrato funcione corretamente.
- O sistema foi pensado para uso em ambiente local e linha de comando. Não possui interface gráfica.

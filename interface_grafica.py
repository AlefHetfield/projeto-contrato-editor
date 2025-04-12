import customtkinter as ctk

ctk.set_appearance_mode('dark')


nome = '''

█▀▀ █▀█ █▄░█ ▀█▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀   █▀▄▀█ █▀█ ▀█▀ █ █░█ █▀▀
█▄▄ █▄█ █░▀█ ░█░ █▀▄ █▀█ ░█░ █▄█ ▄█   █░▀░█ █▄█ ░█░ █ ▀▄▀ ██▄
'''




app = ctk.CTk()

app.title('Editor de Contrato MOTIVE')
app.geometry('800x800')

botao = ctk.CTkButton(app, text='Cadastrar Participantes')
botao2 = ctk.CTkButton(app, text='Exibir Dados do Contrato')
botao3= ctk.CTkButton(app, text='Salvar Arquivo')
botao4 = ctk.CTkButton(app, text='Converter para PDF')
botao5 = ctk.CTkButton(app, text='Cadastrar imóvel')

                      
                      
                      
                      
nome_programa = ctk.CTkLabel(app, text=nome)

nome_programa.pack()
botao.pack(pady=10, padx=10)
botao2.pack(pady=10, padx=10)
botao3.pack(pady=10, padx=10)
botao4.pack(pady=10, padx=10)
botao5.pack(pady=10, padx=10)

app.mainloop()

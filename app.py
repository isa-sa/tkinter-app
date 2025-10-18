import customtkinter as ctk

def calcular():
    nota_1 = float(nota1.get())
    nota_2 = float(nota2.get())
    nota_3 = float(nota3.get())
    nomeAluno = nome.get()
    final = (nota_1+nota_2+nota_3)/3
    
    if final >= 7:
        situacao = 'aprovado'
    elif 5 <= final < 7:
        situacao = 'recuperação'
    else:
        situacao = 'reprovado'
    mensagem.configure(text=f'Sr(a) {nomeAluno}, sua média final foi de {final:.2f} e sua situação é {situacao}')

janela = ctk.CTk('#a772ba')
janela.geometry('600x550')
janela.title('Sistema Escolar - 2025')
janela.resizable(False, False)

ctk.CTkLabel(janela,
            text=('App Sistema Escolar'),
            text_color='black',
            font=('arial',40,'bold')).pack(pady=40)

nome = ctk.CTkEntry(janela,
            width=400,
            height=40,
            placeholder_text='Digite o nome do aluno',
            fg_color='white',
            text_color='black',
            border_color='black'
)
nome.pack(pady=10)

nota1 = ctk.CTkEntry(janela,
            width=400,
            height=40,
            placeholder_text='Digite a nota da 1ª unidade',
            fg_color='white',
            text_color='black',
            border_color='black'
)
nota1.pack(pady=10)

nota2 = ctk.CTkEntry(janela,
            width=400,
            height=40,
            placeholder_text='Digite a nota da 2ª unidade',
            fg_color='white',
            text_color='black',
            border_color='black'
)
nota2.pack(pady=10)

nota3 = ctk.CTkEntry(janela,
            width=400,
            height=40,
            placeholder_text='Digite a nota da 3ª unidade',
            fg_color='white',
            text_color='black',
            border_color='black'
)
nota3.pack(pady=10)

resultado = ctk.CTkButton(janela,
            width=150,
            height=40,
            text='Resultado final',
            text_color='black',
            border_color='black',
            fg_color='white',
            cursor='hand2',
            command=calcular
)
resultado.pack(pady=20)

mensagem = ctk.CTkLabel(janela,
                        text='',
                        text_color='black',
                        font=('arial', 15, 'bold'))
mensagem.pack(pady=10)


janela.mainloop()
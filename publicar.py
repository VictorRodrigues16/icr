import tkinter as tk
from tkinter import filedialog, scrolledtext
from PIL import Image, ImageTk


def carregar_imagem():
    filename = filedialog.askopenfilename(title="Selecione uma imagem")
    if filename:
        image_original = Image.open(filename)
        image_resized = image_original.resize((250, 180))
        photo = ImageTk.PhotoImage(image_resized)
        label_imagem.configure(image=photo)
        label_imagem.image = photo
        return filename

def configure_button(button):
    button.configure(
        background='#6495ED',
        foreground='white',
        font=('Helvetica', 12, 'bold'),
        relief=tk.GROOVE,
        borderwidth=0,
        padx=10,
        pady=5
    )

formato_botao2 = {
        'background': '#FA8072',
        'foreground': 'white',
        'font': ('Helvetica', 12, 'bold'),
        'relief': tk.GROOVE,
        'borderwidth': 0,
        'padx': 10,
        'pady': 5
    }

def sair_publi(janela):
    janela.destroy()
def criar_publicacao():
    def carregar_e_mostrar_imagem():
        global imagem_carregada
        imagem_carregada = carregar_imagem()
        if imagem_carregada:
            image_original = Image.open(imagem_carregada)
            image_resized = image_original.resize((250, 180))
            photo = ImageTk.PhotoImage(image_resized)
            label_imagem.configure(image=photo)
            label_imagem.image = photo

    def salvar_publicacao():
        nome = entry_nome.get()
        sobrenome = entry_sobrenome.get()
        descricao = entry_descricao.get("1.0", tk.END)
        if nome.strip() == "" or sobrenome.strip() == "" or descricao.strip() == "" or not imagem_carregada:
            tk.messagebox.showerror("Erro", "Por favor, preencha todos os campos e carregue uma imagem.")
        else:
            publicacoes.append({
                "nome": nome,
                "sobrenome": sobrenome,
                "descricao": descricao,
                "imagem": imagem_carregada
            })
            print("Publicação criada com sucesso!")
            janela_publicacao.destroy()

    janela_publicacao = tk.Toplevel()
    janela_publicacao.title("Criar Publicação")
    largura_janela = 600
    altura_janela = 500
    pos_x = (janela_publicacao.winfo_screenwidth() - largura_janela) // 2
    pos_y = (janela_publicacao.winfo_screenheight() - altura_janela) // 2
    janela_publicacao.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    nome = tk.Label(janela_publicacao, text="Nome", font=('Arial', 18, 'bold'))
    nome.place(relx=0.125, rely=0.15, anchor="center")
    entry_nome = tk.Entry(janela_publicacao, font=('Arial', 14), width=17)
    entry_nome.place(relx=0.22, rely=0.22, anchor="center")

    sobrenome = tk.Label(janela_publicacao, text="Sobrenome", font=('Arial', 18, 'bold'))
    sobrenome.place(relx=0.17, rely=0.30, anchor="center")
    entry_sobrenome = tk.Entry(janela_publicacao, font=('Arial', 14), width=17)
    entry_sobrenome.place(relx=0.22, rely=0.37, anchor="center")

    desc = tk.Label(janela_publicacao, text="Descrição", font=('Arial', 18, 'bold'))
    desc.place(relx=0.16, rely=0.48, anchor="center")
    entry_descricao = tk.Text(janela_publicacao, height=7, width=30)
    entry_descricao.place(relx=0.27, rely=0.64, anchor="center")

    btn_carregar_imagem = tk.Button(janela_publicacao, text="Carregar Imagem", command=carregar_e_mostrar_imagem)
    configure_button(btn_carregar_imagem)
    btn_carregar_imagem.place(relx=0.75, rely=0.1, anchor="center", width=190, height=50)

    global label_imagem
    label_imagem = tk.Label(janela_publicacao)
    label_imagem.place(relx=0.74, rely=0.4, anchor="center")

    btn_publicar = tk.Button(janela_publicacao, text="Publicar", command=salvar_publicacao)
    configure_button(btn_publicar)
    btn_publicar.place(relx=0.2, rely=0.89, anchor="center",  width=190, height=55)

    btn_sair_publi = tk.Button(janela_publicacao, text="Voltar", command=lambda: sair_publi(janela_publicacao), **formato_botao2)
    btn_sair_publi.place(relx=0.54, rely=0.89, anchor="center", width=190, height=55)

def ver_publicacoes():
    janela_visualizar = tk.Toplevel()
    janela_visualizar.title("Minhas Publicações")
    largura_janela = 1100
    altura_janela = 600
    pos_x = (janela_visualizar.winfo_screenwidth() - largura_janela) // 2
    pos_y = (janela_visualizar.winfo_screenheight() - altura_janela) // 2
    janela_visualizar.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    canvas = tk.Canvas(janela_visualizar)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(janela_visualizar, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    frame_publicacoes = tk.Frame(canvas)
    canvas.create_window(0, 0, window=frame_publicacoes, anchor='nw')

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_publicacoes.bind("<Configure>", on_frame_configure)

    row = 0
    col = 0
    for i, publicacao in enumerate(publicacoes):
        nome = publicacao["nome"]
        sobrenome = publicacao["sobrenome"]
        imagem = publicacao["imagem"]
        descricao = publicacao["descricao"]

        if i % 3 == 0 and i != 0:
            row += 1
            col = 0

        frame_publicacao = tk.Frame(frame_publicacoes, relief=tk.GROOVE, borderwidth=2)
        frame_publicacao.grid(row=row, column=col, padx=10, pady=10)

        tk.Label(frame_publicacao, text=f"{nome} {sobrenome}", font=('Arial', 14, 'bold')).pack()

        image_original = Image.open(imagem)
        image_resized = image_original.resize((310, 260))
        photo = ImageTk.PhotoImage(image_resized)
        label_imagem = tk.Label(frame_publicacao, image=photo)
        label_imagem.image = photo
        label_imagem.pack()

        tk.Label(frame_publicacao, text="Descrição", font=('Arial', 14, 'bold')).pack()
        tk.Label(frame_publicacao, text=descricao, font=('Arial', 12)).pack()

    col += 1

    janela_visualizar.mainloop()



publicacoes = []


def sair(janela):
    janela.destroy()


def criar_botoes_pub():
    root = tk.Toplevel()
    root.title("PROCEDIMENTOS")
    largura_janela = 650
    altura_janela = 500
    pos_x = (root.winfo_screenwidth() - largura_janela) // 2
    pos_y = (root.winfo_screenheight() - altura_janela) // 2
    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    canvas = tk.Canvas(root, width=largura_janela, height=altura_janela)
    canvas.pack()

    image_original = Image.open("image_3.png")
    image_resized = image_original.resize((340, 240))
    photo = ImageTk.PhotoImage(image_resized)

    canvas.create_image(330, 20, anchor='n', image=photo)
    canvas.image = photo

    procedimentos_esquerda = [
        ("Publicar", criar_publicacao),
    ]



    procedimentos_direita = [
        ("Minhas Publicações", lambda: ver_publicacoes()),
    ]

    pos_y = 0.55
    espacamento = 25

    for nome, funcao in procedimentos_esquerda:
        btn_procedimento = tk.Button(root, text=nome, command=funcao, background='#6495ED',
                                     foreground='white', font=('Helvetica', 12, 'bold'),
                                     relief=tk.GROOVE, borderwidth=0, padx=3, pady=5)
        btn_procedimento.place(relx=0.30, rely=pos_y, anchor="center", width=250, height=60)
        pos_y += 0.1 + espacamento / 800

    pos_y = 0.55

    for nome, funcao in procedimentos_direita:
        btn_procedimento = tk.Button(root, text=nome, command=funcao, background='#6495ED',
                                     foreground='white', font=('Helvetica', 12, 'bold'),
                                     relief=tk.GROOVE, borderwidth=0, padx=3, pady=5)
        btn_procedimento.place(relx=0.70, rely=pos_y, anchor="center", width=250, height=60)
        pos_y += 0.1 + espacamento / 800

    posi_y = 0.7

    btn_sair = tk.Button(root, text='Voltar', command=lambda: sair(root), **formato_botao2)
    btn_sair.place(relx=0.5, rely=posi_y, anchor="center", width=180, height=60)

    return root


if __name__ == "__main__":
    root = criar_botoes()

    # Loop principal que não será interrompido pelo teclado
    while root.winfo_exists():
        root.update_idletasks()
        root.update()
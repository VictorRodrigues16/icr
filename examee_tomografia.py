import tkinter as tk
from PIL import Image, ImageTk


def veja_video():
    print("Abrindo o vídeo.")


def sair(janela):
    janela.destroy()


def tomo():
    root = tk.Toplevel()
    root.title("Procedimento")
    largura_janela = 750
    altura_janela = 600
    pos_x = (root.winfo_screenwidth() - largura_janela) // 2
    pos_y = (root.winfo_screenheight() - altura_janela) // 2
    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    canvas = tk.Canvas(root, width=largura_janela, height=altura_janela)
    canvas.pack()

    # Abre a imagem original
    image_original = Image.open("tomografia.png")
    # Redimensiona a imagem para um tamanho menor (por exemplo, 400x400)
    image_resized = image_original.resize((250, 230))
    # Converte a imagem para um formato suportado pelo tkinter
    photo = ImageTk.PhotoImage(image_resized)

    # Coloca a imagem no canvas mais no canto superior esquerdo
    canvas.create_image(30, 5, anchor='nw', image=photo)
    canvas.image = photo

    formato_botao = {
        'background': '#6495ED',
        'foreground': 'white',
        'font': ('Helvetica', 12, 'bold'),
        'relief': tk.GROOVE,
        'borderwidth': 0,
        'padx': 10,
        'pady': 5
    }

    formato_botao2 = {
        'background': '#FA8072',
        'foreground': 'white',
        'font': ('Helvetica', 12, 'bold'),
        'relief': tk.GROOVE,
        'borderwidth': 0,
        'padx': 10,
        'pady': 5
    }
    opcao = [
        ("Veja o Vídeo", veja_video),
        ("Sair", lambda: sair(root))
    ]

    pos_y = 0.96

    btn_video = tk.Button(root, text='Veja o Vídeo', command=veja_video, **formato_botao)
    btn_video.place(relx=0.35, rely=pos_y, anchor="s", width=220, height=60)

    btn_sair = tk.Button(root, text='Sair', command=lambda: sair(root), **formato_botao2)
    btn_sair.place(relx=0.65, rely=pos_y, anchor="s", width=150, height=60)

    # Adiciona o rótulo (label) com o texto "Exame De Sangue" em três linhas distintas
    label_exame = tk.Label(root, text="Tomografia", font=("Helvetica", 45, "bold"), foreground="#4682B4")
    label_exame.place(relx=0.9, rely=0.10, anchor="ne")

    tittle_preparo = tk.Label(root, text="Preparo", font=("Helvetica", 30, "bold"), foreground="#696969")
    tittle_preparo.place(relx=0.60, rely=0.52, anchor="se")

    preparo_cont = tk.Label(root, text="1. Utilizar de preferência roupas de algodão\n e que não tenham itens metálicos\n (botões e zíper), incluindo roupas íntimas.\n \n 2. Realizar jejum de 8 horas antes do exame (Incluindo água).\n \n 3. Seguir instruções de preparo específicas\nfornecidas pela clínica ou hospital."
                                       , font=("Helvetica", 13, "bold"), foreground="#696969")
    preparo_cont.place(relx=0.83, rely=0.78, anchor="se")

    return root


if __name__ == "__main__":
    root = tomo()
    root.mainloop()

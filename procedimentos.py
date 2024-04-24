import tkinter as tk
from examee_sangue import sangue
from examee_radiografia import radio
from examee_ultrassom import ultra
from examee_endoscopia import endos
from examee_tomografia import tomo
from examee_ressonancia import ress


def exame_sangue():
    print("Executando exame de sangue.")
    sangue()


def radiografia():
    print("Realizando radiografia.")
    radio()


def ultrassom():
    print("Realizando ultrassom.")
    ultra()


def endoscopia():
    print("Realizando endoscopia.")
    endos()


def tomografia():
    print("Realizando tomografia.")
    tomo()


def ressonancia():
    print("Realizando ressonância magnética.")
    ress()


def sair(janela):
    janela.destroy()


def criar_botoes():
    root = tk.Toplevel()
    root.title("PROCEDIMENTOS")
    largura_janela = 650
    altura_janela = 700
    pos_x = (root.winfo_screenwidth() - largura_janela) // 2
    pos_y = (root.winfo_screenheight() - altura_janela) // 2
    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    canvas = tk.Canvas(root, width=largura_janela, height=altura_janela)
    canvas.pack()

    image = tk.PhotoImage(file="../icr2/galery/image_3.png")
    canvas.create_image(largura_janela / 2, 0, anchor='n', image=image)
    canvas.image = image

    procedimentos_esquerda = [
        ("Exame de Sangue", exame_sangue),
        ("Radiografia", radiografia),
        ("Ultrassom", ultrassom)
    ]

    formato_botao2 = {
        'background': '#FA8072',
        'foreground': 'white',
        'font': ('Helvetica', 12, 'bold'),
        'relief': tk.GROOVE,
        'borderwidth': 0,
        'padx': 10,
        'pady': 5
    }

    procedimentos_direita = [
        ("Endoscopia", endoscopia),
        ("Tomografia", tomografia),
        ("Ressonância", ressonancia)
    ]

    pos_y = 0.5
    espacamento = 25

    for nome, funcao in procedimentos_esquerda:
        btn_procedimento = tk.Button(root, text=nome, command=funcao, background='#6495ED',
                                     foreground='white', font=('Helvetica', 12, 'bold'),
                                     relief=tk.GROOVE, borderwidth=0, padx=3, pady=5)
        btn_procedimento.place(relx=0.30, rely=pos_y, anchor="center", width=250, height=60)
        pos_y += 0.1 + espacamento / 800

    pos_y = 0.5

    for nome, funcao in procedimentos_direita:
        btn_procedimento = tk.Button(root, text=nome, command=funcao, background='#6495ED',
                                     foreground='white', font=('Helvetica', 12, 'bold'),
                                     relief=tk.GROOVE, borderwidth=0, padx=3, pady=5)
        btn_procedimento.place(relx=0.70, rely=pos_y, anchor="center", width=250, height=60)
        pos_y += 0.1 + espacamento / 800

    posi_y = 0.9

    btn_sair = tk.Button(root, text='Voltar', command=lambda: sair(root), **formato_botao2)
    btn_sair.place(relx=0.5, rely=posi_y, anchor="center", width=180, height=60)

    return root


if __name__ == "__main__":
    root = criar_botoes()
    root.mainloop()

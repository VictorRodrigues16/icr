import tkinter as tk
from PIL import Image, ImageTk
import webbrowser


def mapa():
    print("Abrindo o vídeo.")
    url = "https://www.google.com.br/maps/place/Hospital+das+Cl%C3%ADnicas+da+Universidade+de+S%C3%A3o+Paulo+Emergency+Room/@-23.5567673,-46.6729039,17z/data=!3m1!4b1!4m6!3m5!1s0x94ce582a0a3b4c3f:0x878285f3f6b43c83!8m2!3d-23.5567722!4d-46.670329!16s%2Fg%2F11g6nj4ghl?entry=ttu"
    webbrowser.open(url)


def sair(janela):
    janela.destroy()


def mapa_int():
    root = tk.Toplevel()
    root.title("MAPAS")
    largura_janela = 750
    altura_janela = 600
    pos_x = (root.winfo_screenwidth() - largura_janela) // 2
    pos_y = (root.winfo_screenheight() - altura_janela) // 2
    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    canvas = tk.Canvas(root, width=largura_janela, height=altura_janela)
    canvas.pack()

    image_original = Image.open("mapa-interno.png")
    image_resized = image_original.resize((520, 410))
    photo = ImageTk.PhotoImage(image_resized)

    canvas.create_image(370, 80, anchor='n', image=photo)
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
        ("Como chegar?", mapa),
        ("Sair", lambda: sair(root))
    ]

    pos_y = 0.96

    btn_mapa = tk.Button(root, text='Como chegar?', command=mapa, **formato_botao)
    btn_mapa.place(relx=0.35, rely=pos_y, anchor="s", width=220, height=60)

    btn_sair = tk.Button(root, text='Voltar', command=lambda: sair(root), **formato_botao2)
    btn_sair.place(relx=0.65, rely=pos_y, anchor="s", width=150, height=60)


    tittle_preparo = tk.Label(root, text="Mapa Interno", font=("Helvetica", 30, "bold"), foreground="#696969")
    tittle_preparo.place(relx=0.5, rely=0, anchor="n")

    return root


if __name__ == "__main__":
    root = mapa_int()
    root.mainloop()

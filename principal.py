import tkinter as tk
from PIL import Image, ImageTk
import ctypes
from procedimentos import criar_botoes

def publicar():
    print("Botão Publicar pressionado")

def procedimento():
    print("Botão Procedimentos pressionado")
    criar_botoes()

def localizacao():
    print("Botão Localização pressionado")

def sair():
    root.destroy()

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

root = tk.Tk()
root.title("ICR CONECTA")
root.iconbitmap('image-3.ico')

user32 = ctypes.windll.user32
largura_tela = user32.GetSystemMetrics(0)
altura_tela = user32.GetSystemMetrics(1)

largura_janela = 500
altura_janela = 500
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2
root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

image = Image.open("image_3.png")
image = image.resize((300, 200))
photo = ImageTk.PhotoImage(image)
label_img = tk.Label(root, image=photo)
label_img.place(relx=0.5, rely=0, anchor="n")

espacamento = 20
pos_y = 0.5

btn_publicar = tk.Button(root, text="Publicar", command=publicar)
configure_button(btn_publicar)
btn_publicar.place(relx=0.5, rely=pos_y, anchor="center", width=200, height=50)

pos_y += 0.1 + espacamento / 500

btn_procedimentos = tk.Button(root, text="Procedimentos", command=procedimento)
configure_button(btn_procedimentos)
btn_procedimentos.place(relx=0.5, rely=pos_y, anchor="center", width=200, height=50)

pos_y += 0.1 + espacamento / 500

btn_localizacao = tk.Button(root, text="Localização", command=localizacao)
configure_button(btn_localizacao)
btn_localizacao.place(relx=0.5, rely=pos_y, anchor="center", width=200, height=50)

pos_y += 0.1 + espacamento / 500

btn_sair = tk.Button(root, text='Sair', command=sair, **formato_botao2)
btn_sair.place(relx=0.5, rely=pos_y, anchor="center", width=200, height=50)

root.mainloop()

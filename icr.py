import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import ctypes

def publicar():
    print("Botão Publicar pressionado")

def procedimentos():
    print("Botão Procedimentos pressionado")

def localizacao():
    print("Botão Localização pressionado")

def sair():
    root.destroy()



root = tk.Tk()
root.title("ICR CONECTA")

user32 = ctypes.windll.user32
largura_tela = user32.GetSystemMetrics(0)
altura_tela = user32.GetSystemMetrics(1)

largura_janela = 500
altura_janela = 500
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2
root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")



style = ttk.Style()
style.configure('Custom.TButton', background='#6495ED', foreground='black', focuscolor='#6495ED',
                font=('Helvetica', 12, 'bold'))

image = Image.open("image 3.png")

image = image.resize((300, 200))
photo = ImageTk.PhotoImage(image)


label_img = tk.Label(root, image=photo)

label_img.place(relx=0.5, rely=0, anchor="n")


espacamento = 20


pos_y = 0.5


btn_publicar = ttk.Button(root, text="Publicar", style='Custom.TButton', command=publicar)
btn_publicar.place(relx=0.5, rely=pos_y, anchor="center", width=200, height=50)

pos_y += 0.1 + espacamento / 500

btn_procedimentos = ttk.Button(root, text="Procedimentos", style='Custom.TButton', command=procedimentos)
btn_procedimentos.place(relx=0.5, rely=pos_y, anchor="center", width=200, height=50)

pos_y += 0.1 + espacamento / 500

btn_localizacao = ttk.Button(root, text="Localização", style='Custom.TButton', command=localizacao)
btn_localizacao.place(relx=0.5, rely=pos_y, anchor="center", width=200, height=50)

pos_y += 0.1 + espacamento / 500

btn_sair = ttk.Button(root, text="Sair", style='Custom.TButton', command=sair)
btn_sair.place(relx=0.5, rely=pos_y, anchor="center", width=200, height=50)

root.mainloop()

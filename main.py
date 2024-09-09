import ctypes
import tkinter as tk
from PIL import ImageTk, Image
import time

def move_image(image_path, speed=10):
    root = tk.Tk()
    root.overrideredirect(True)
    img = Image.open(image_path)
    photo = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=photo)
    label.pack()

    # Obtém as dimensões da tela e da imagem
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    img_width, img_height = img.size

    # Variáveis para controlar a posição
    x, y = 0, 0
    direction = 1  # 1: direita, -1: esquerda

    def move():
        nonlocal x, y, direction
        # Calcula a nova posição
        x += speed * direction
        # Verifica se a imagem saiu da tela
        if x + img_width >= screen_width or x <= 0:
            direction *= -1
        # Atualiza a posição da janela
        root.geometry(f"{img_width}x{img_height}+{x}+{y}")
        # Chama a função novamente após 1 segundo
        root.after(1000, move)

    move()
    root.mainloop()

# Substitua 'caminho_da_sua_imagem.jpg' pelo caminho completo da sua imagem
image_path = "imagem.png"
move_image(image_path, speed=5)  # Ajuste a velocidade aqui
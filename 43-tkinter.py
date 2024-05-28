import tkinter as tk

# 1 - Crinado a janela
window = tk.Tk()
window.geometry('300x150')
window.title('Gerenciador de frases')

# 2 - Adicionando o frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# 3 - Adicionando o label
label = tk.Label(frame, text='Hello, word')
label.pack(padx=10, pady=10, fill='x', expand=True)

# 4 - Adicionando o input text
fraseLab = tk.Label(frame, text='Frase')
fraseLab.pack(padx=10, pady=10, fill='x', expand=True)

fraseInp = tk.Entry(frame)
fraseInp.pack(fill='x', expand=True)

# 5 -Função para alterar o tetxo do label
def click():
    label.config(text=fraseInp.get())

# 6 - Adicionando botão
button = tk.Button(frame, text='Enviar', command=click)
button.pack()
window.mainloop()

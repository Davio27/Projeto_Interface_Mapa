import tkinter as tk
from tkinter import ttk

class OutraClasse(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Nova Janela")
        self.geometry("300x200")
        label = ttk.Label(self, text="Esta é outra classe!")
        label.pack(pady=20)
        closeButton = ttk.Button(self, text="Fechar", command=self.fechar_janela)
        closeButton.pack(pady=10)

    def fechar_janela(self):
        self.destroy()

class MinhaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Minha Aplicação")
        self.geometry("400x300")
        label = ttk.Label(self, text="Bem-vindo à minha aplicação!")
        label.pack(pady=20)
        button = ttk.Button(self, text="Abrir Outra Janela", command=self.abrir_outra_janela)
        button.pack(pady=10)

    def abrir_outra_janela(self):
        outra_janela = OutraClasse(self)
        outra_janela.grab_set()

if __name__ == "__main__":
    app = MinhaApp()
    app.mainloop()

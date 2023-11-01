# import folium
# import hashlib
# import json
# import webbrowser
import customtkinter
import customtkinter as ctk


class registrar(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Aplicação Map")
        self.geometry("900x500")
        
        self.titulo = customtkinter.CTkLabel(self, text='Cadastro de Clientes', font=customtkinter.CTkFont(size=20, weight="bold"), bg_color="transparent")
        self.titulo.grid(row=0, column=0, padx=10, pady=(10))


        # Criar Rótulos e campos de entrada
        self.label_nome = ctk.CTkLabel(self, text="Nome Completo:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_nome.grid(row=2, column=2, padx=10, pady=10)
        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Obrigatório", width=380)
        self.entry_nome.grid(row=2, column=3, padx=10, pady=10)

        self.label_email = ctk.CTkLabel(self, text="Email:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_email.grid(row=3, column=2, padx=10, pady=10)
        self.entry_email = ctk.CTkEntry(self, placeholder_text="Obrigatório", width=380)
        self.entry_email.grid(row=3, column=3, padx=10, pady=10)
    
        self.label_N_Telefone = ctk.CTkLabel(self, text="Numero com DDD:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_N_Telefone.grid(row=4, column=2, padx=10, pady=10)
        self.entry_N_Telefone = ctk.CTkEntry(self, placeholder_text="Obrigatório", width=380)
        self.entry_N_Telefone.grid(row=4, column=3, padx=10, pady=10)
        
        self.label_Senha = ctk.CTkLabel(self, text="Senha:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_Senha.grid(row=5, column=2, padx=10, pady=10)
        self.entry_Senha = ctk.CTkEntry(self, placeholder_text="Obrigatório", width=380)
        self.entry_Senha.grid(row=5, column=3, padx=10, pady=10)
        
        self.label_D_Nascimento = ctk.CTkLabel(self, text="Data de Nascimento:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_D_Nascimento.grid(row=6, column=2, padx=10, pady=10)
        self.entry_D_Nascimento = ctk.CTkEntry(self, placeholder_text="Obrigatório", width=380)
        self.entry_D_Nascimento.grid(row=6, column=3, padx=10, pady=10)
        

        # Criar Botão para cadastrar cliente
        btn_cadastrar = ctk.CTkButton(self, text="Registrar", command=self.cadastrar)
        btn_cadastrar.grid(row=850, column=3, padx=0, pady=30)
        
    def cadastrar(self):
        self.register


class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Aplicação Map")
        self.geometry("900x500")

        # Criar widgets
        self.titulo = customtkinter.CTkLabel(self, text='Bem Vindo a nossa Plataforma!', font=customtkinter.CTkFont(size=20, weight="bold"), bg_color="transparent")
        self.titulo.grid(row=0, column=0, padx=10, pady=(20))
        
        self.label_login = ctk.CTkLabel(self, text="Tela de Login", font=customtkinter.CTkFont(size=20, weight="bold"), text_color="white", bg_color="transparent")
        self.label_login.grid(row=1, column=2, padx=10, pady=20)
        
        self.label_email = ctk.CTkLabel(self, text="Email:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_email.grid(row=2, column=1, padx=10, pady=10)
        self.entry_email = ctk.CTkEntry(self, placeholder_text="Obrigatório", width=380)
        self.entry_email.grid(row=2, column=2, padx=10, pady=10)
        
        self.label_senha = ctk.CTkLabel(self, text="Senha:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_senha.grid(row=3, column=1, padx=10, pady=10)
        self.entry_senha = ctk.CTkEntry(self, placeholder_text="Obrigatório", width=380)
        self.entry_senha.grid(row=3, column=2, padx=10, pady=10)

        
        self.bt_registro = ctk.CTkButton(self, text="Register", bg_color="transparent", command=self.Registro)
        self.bt_registro.grid( row=497, column=0, pady=(10, 20))
        
        self.bt_sair = ctk.CTkButton(self, text="Sair", bg_color="transparent")
        self.bt_sair.grid(row=499, column=0, pady=(10, 20))

    def login(self):
        pass
            
    def Registro(self):
        if __name__ == "__main__":
            app = registrar()
            app.mainloop()
            
if __name__ == "__main__":
    app = Login()
    app.mainloop()
    


    

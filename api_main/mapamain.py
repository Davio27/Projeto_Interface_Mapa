import customtkinter
import customtkinter as ctk
from customtkinter import *
import tkinter 
from tkinter import messagebox
from tkinter import END
import folium
import hashlib
import os
import json
import webbrowser
import re
import sqlite3

class Interface(ctk.CTk):
    # # Variaveis Globais
    # confirmar_modo = False
    # porrasenha=False

    # encriptar senha
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    # Salvar dados do usuário
    def salva_dados_usuario(self, email, senha_hash, nome_full, telefone, dataN):
        with open("usuarios.json", "a") as file:
            data = {"email": email, "Senha": senha_hash, "Nome Completo": nome_full, "Telefone": telefone, "Data de Nascimento": dataN}
            json.dump(data, file)
            file.write('\n')
    
    # Verificar se o usuário já esta cadastrado para altenticar
    def load_user_data(self):
        try:
            with open("usuarios.json", "r") as file:
                return [json.loads(line) for line in file]
        except FileNotFoundError:
            return []
    
    # função abrir mapa no navegador
    def mostrar_html(self, file_path):
        # Abre o arquivo mapa.html no navegador padrão
        webbrowser.open(file_path, new=2)  
    
    # Gerar mapa no Folium
    def carregar_folium_map(self, file_path):
        map_folium = folium.Map(
            location=[-22.9064, -47.0616],
            zoom_start=18,)
        # Adicione um ouvinte de eventos de clique ao mapa
        folium.ClickForMarker(popup='Local Marcado').add_to(map_folium)
        
        # Adicione o código do formulário ao final do HTML
        formulario_html = """
        <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <style>
        #formulario-button {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 1000;
            background-color: #4caf50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    
        #formulario-container {
            display: none;
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 1000;
        }
    
        #formulario {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
            width: 200px;
            margin: 0 auto;
            position: relative;
        }
    
        #minimizar-btn {
            position: absolute;
            top: 5px;
            right: 5px;
            width: 30px;
            height: 30px;
            background-color: #e7e7e7;
            color: red;
            padding: 5px;
            border: none;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        #minimizar-btn i{
            font-size: 30px;
        }

        #upload-btn {
        background-color: #3498db;
        color: white;
        padding: 10px 15px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 10px;
        }

        input[type="file"] {
            display: none;
        }

        input[type="file"] + label {
            background-color: #3498db;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
            display: inline-block;
        }

        input[type="file"]:focus + label {
            outline: 1px dotted #000;
        }

        input[type="file"]:active + label {
            outline: 1px solid #000;
        }
    
        input {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
        }
    
        button {
            background-color: #4caf50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    
        button:hover {
            background-color: #45a049;
        }
    </style>
    
    <button id="formulario-button" onclick="toggleFormulario()">Formulário</button>
    
    <div id="formulario-container">
        <form id="formulario">
            <button id="minimizar-btn" onclick="minimizarFormulario()"><i class='bx bxs-x-circle' style='color:#ec0d0d'></i></button>
            Telefone: <input type="text" id="telefone"><br>
            CEP: <input type="text" id="cep"><br>
            Nome: <input type="text" id="nome"><br>
            Assunto: <input type="text" id="assunto"><br>

            <!-- Botão para upload de fotos -->
            <input type="file" id="file" />
            <label for="file" id="upload-btn">Carregar Fotos</label>
        
            <button type="button" onclick="submitForm()">Salvar</button>
        </form>
    </div>
    
<script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
<script>
    function toggleFormulario() {
        var formularioContainer = document.getElementById('formulario-container');
        formularioContainer.style.display = (formularioContainer.style.display === 'none' || formularioContainer.style.display === '') ? 'block' : 'none';
    }

    function minimizarFormulario() {
        document.getElementById('formulario-container').style.display = 'none';
    }

    function submitForm() {
        // Obter dados do formulário
        var dados = {
            telefone: $('#telefone').val(),
            cep: $('#cep').val(),
            nome: $('#nome').val(),
            assunto: $('#assunto').val()
        };

        var url = window.location.href;

        // Fazer uma requisição assíncrona para o servidor Python
        $.ajax({
            type: 'POST',
            url: url + '/salvar_dados_formulario',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify(dados),
            success: function () {
                console.log('Dados enviados:', dados);
                alert('Formulário enviado!');
            },
            error: function () {
                alert('Erro ao enviar formulário. Por favor, tente novamente.');
            }
        });
    }
 </script>
        """
        map_folium.get_root().html.add_child(folium.Element(formulario_html))
        
        map_folium.save(file_path)
        self.mostrar_html(file_path)
    
    # Salvar dados do Usuário
    def salvar_dados_formulario(self, dados_json):
        # Converter o JSON de volta para um dicionário
        dados = json.loads(dados_json)

        # Adicionar lógica para salvar os dados no arquivo desejado
        with open("dados_formulario.json", "a") as file:
            json.dump(dados, file)
            file.write('\n')

        # Adicionar código de depuração
        print(dados)

        # Verificar se o arquivo foi criado
        if os.path.isfile("dados_formulario.json"):
            print("O arquivo foi criado")
        else:
            print("O arquivo não foi criado")

    # Interface Login
    def Login(self):
        self.title("Aplicação Map")
        self.geometry("900x600")
    

        # Criar widgets
        self.titulo = customtkinter.CTkLabel(self, text='Bem Vindo a nossa Plataforma!', font=customtkinter.CTkFont(size=20, weight="bold"), bg_color="transparent")
        self.titulo.grid(row=0, column=0, padx=10, pady=(20))
        
        self.label_login = ctk.CTkLabel(self, text="Tela de Login", font=customtkinter.CTkFont(size=20, weight="bold"), text_color="white", bg_color="transparent")
        self.label_login.grid(row=1, column=2, padx=10, pady=20)
        
        self.label_emailL = ctk.CTkLabel(self, text="Email:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_emailL.grid(row=2, column=1, padx=10, pady=10)
        self.entry_emailL = ctk.CTkEntry(self, width=380)
        self.entry_emailL.grid(row=2, column=2, padx=10, pady=10)
        
        self.label_senhaL = ctk.CTkLabel(self, text="Senha:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_senhaL.grid(row=3, column=1, padx=10, pady=10)
        
        self.senha_var = ctk.StringVar()
        self.senha_var.set("")
        self.entry_senhaL = ctk.CTkEntry(self, placeholder_text="Obrigatório", width=380, show="*", textvariable=self.senha_var)
        self.entry_senhaL.grid(row=3, column=2, padx=10, pady=10)
        
        self.ver_senha_var = ctk.BooleanVar()
        self.ver_senha_check = ctk.CTkCheckBox(self, text="Ver Senha", corner_radius=50,fg_color="green",text_color="light blue", command=self.ver_senha)
        self.ver_senha_check.grid(row=4, column=2, padx=10, pady=10)

        
        self.bt_registro = ctk.CTkButton(self, text="Register", bg_color="transparent", command=self.Registrar)
        self.bt_registro.grid( row=497, column=0, pady=(10, 20))
        
        self.bt_sair = ctk.CTkButton(self, text="Sair", bg_color="transparent", command=self.Sair)
        self.bt_sair.grid(row=499, column=0, pady=(10, 20))
        
        self.btn_cadastrarL = ctk.CTkButton(self, text="Login", command=self.entrar)
        self.btn_cadastrarL.grid(row=550, column=2, padx=0, pady=30)

        self.appearance_mode_label = customtkinter.CTkLabel(self, text="""⬇ Aparência ⬇️""", anchor="w", text_color="white", font=("Helvetica", 14))
        self.appearance_mode_label.grid(row=500, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self, values=["Dark", "Light"],
                                                                       command=self.aparencia_mode)
        self.appearance_mode_optionemenu.grid(row=502, column=0, padx=20, pady=(10, 10))
        
        if Interface.confirmar_modo == True:
            customtkinter.set_default_color_theme("green")
            # Alterar a cor do texto para preto no modo "Write"
            self.titulo.configure(text_color="black")
            self.label_login.configure(text_color="black")
            self.label_emailL.configure(text_color="black")
            self.label_senhaL.configure(text_color="black")
            self.ver_senha_check.configure(text_color="black")
            self.appearance_mode_label.configure(text_color="black")
            # Alterar a cor dos botões para verde no modo "Write"
            self.bt_registro.configure(fg_color="green", hover_color="light green", text_color="black")
            self.bt_sair.configure(fg_color="green", hover_color="light green", text_color="black")
            self.btn_cadastrarL.configure(fg_color="green", hover_color="light green", text_color="black")
            self.appearance_mode_optionemenu.configure(fg_color="green",button_color="green",button_hover_color="light green", text_color="black")
            Interface.confirmar_modo = True
        else:
            self.titulo.configure(text_color="white")
            self.label_login.configure(text_color="white")
            self.label_emailL.configure(text_color="white")
            self.label_senhaL.configure(text_color="white")
            self.ver_senha_check.configure(text_color="white")
            self.appearance_mode_label.configure(text_color="white")
            # Alterar a cor dos botões para verde no modo "white"
            self.bt_registro.configure(fg_color="#1d6ca4", hover_color="#144c74", text_color="white")
            self.bt_sair.configure(fg_color="#1d6ca4", hover_color="#144c74", text_color="white")
            self.btn_cadastrarL.configure(fg_color="#1d6ca4", hover_color="#144c74", text_color="white")
            self.appearance_mode_optionemenu.configure(fg_color="#1d6ca4",button_color="#1d6ca4",button_hover_color="#144c74", text_color="white")
            Interface.confirmar_modo = False

    # Modo de Aparencia de Dark e White
    def aparencia_mode(self, new_appearance_mode: str):
        if not new_appearance_mode or new_appearance_mode == "Sistema":
            customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        else:
            customtkinter.set_appearance_mode(new_appearance_mode)
        if new_appearance_mode == "Dark":
            self.titulo.configure(text_color="white")
            self.label_login.configure(text_color="white")
            self.label_emailL.configure(text_color="white")
            self.label_senhaL.configure(text_color="white")
            self.ver_senha_check.configure(text_color="white")
            self.appearance_mode_label.configure(text_color="white")
            # Alterar a cor dos botões para verde no modo "white"
            self.bt_registro.configure(fg_color="#1d6ca4", hover_color="#144c74", text_color="white")
            self.bt_sair.configure(fg_color="#1d6ca4", hover_color="#144c74", text_color="white")
            self.btn_cadastrarL.configure(fg_color="#1d6ca4", hover_color="#144c74", text_color="white")
            self.appearance_mode_optionemenu.configure(fg_color="#1d6ca4",button_color="#1d6ca4",button_hover_color="#144c74", text_color="white")
            Interface.confirmar_modo = False

        else:
            self.titulo.configure(text_color="black")
            self.label_login.configure(text_color="black")
            self.label_emailL.configure(text_color="black")
            self.label_senhaL.configure(text_color="black")
            self.ver_senha_check.configure(text_color="black")
            self.appearance_mode_label.configure(text_color="black")
            # Alterar a cor dos botões para verde no modo "Write"
            self.bt_registro.configure(fg_color="green", hover_color="light green", text_color="black")
            self.bt_sair.configure(fg_color="green", hover_color="light green", text_color="black")
            self.btn_cadastrarL.configure(fg_color="green", hover_color="light green", text_color="black")
            self.appearance_mode_optionemenu.configure(fg_color="green",button_color="green",button_hover_color="light green", text_color="black")
            Interface.confirmar_modo = True

    # Função ver Senha
    def ver_senha(self):
        if Interface.porrasenha == False:
            self.entry_senhaL.configure(show="")
            Interface.porrasenha = True
        
        elif Interface.porrasenha == True:
            self.entry_senhaL.configure(show="*")
            Interface.porrasenha = False


        
    # Altenticação de Login
    def entrar(self):
        email = self.entry_emailL.get()
        password = self.entry_senhaL.get()

        users = self.load_user_data()
        user = next((user for user in users if user["email"] == email), None)

        if user and self.hash_password(password) == user["Senha"]:
            self.carregar_folium_map("mapa.html")
        else:
            messagebox.showerror("Erro no Login", "Credenciais incorretas. Por favor, verifique seu e-mail e senha.")

    #  Interface de Registro
    def Registro(self):

        self.title("Aplicação Map")
        self.geometry("900x600")
        
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
        self.entry_N_Telefone.bind('<KeyRelease>', self.formato_numero)
        
        self.label_Senha = ctk.CTkLabel(self, text="Senha:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_Senha.grid(row=5, column=2, padx=10, pady=10)
        self.entry_Senha = ctk.CTkEntry(self, placeholder_text="Obrigatório", width=380)
        self.entry_Senha.grid(row=5, column=3, padx=10, pady=10)
        
        self.label_D_Nascimento = ctk.CTkLabel(self, text="Data de Nascimento:", font=("Helvetica", 16), text_color="white", bg_color="transparent")
        self.label_D_Nascimento.grid(row=6, column=2, padx=10, pady=10)
        self.entry_D_Nascimento = ctk.CTkEntry(self, placeholder_text="Obrigatório", width=380)
        self.entry_D_Nascimento.grid(row=6, column=3, padx=10, pady=10)
        self.entry_D_Nascimento.bind('<KeyRelease>', self.formato_data)

        # Criar Botão para cadastrar cliente
        self.btn_cadastrar = ctk.CTkButton(self, text="Registrar", command=self.cadastrar)
        self.btn_cadastrar.grid(row=850, column=3, padx=0, pady=30)
        
        self.bt_login = ctk.CTkButton(self, text="Login", command=self.Logout)
        self.bt_login.grid(row=499, column=0, pady=(10, 20))  

        if Interface.confirmar_modo == True:
            self.label_nome.configure(text_color="black")
            self.entry_nome.configure(text_color="black")
            self.label_email.configure(text_color="black")
            self.entry_email.configure(text_color="black")
            self.label_N_Telefone.configure(text_color="black")
            self.entry_N_Telefone.configure(text_color="black")
            self.label_Senha.configure(text_color="black")
            self.entry_Senha.configure(text_color="black")
            self.label_D_Nascimento.configure(text_color="black")
            self.entry_D_Nascimento.configure(text_color="black")
            # Alterar a cor dos botões para verde no modo "Write"
            self.btn_cadastrar.configure(fg_color="green", hover_color="light green", text_color="black")
            self.bt_login.configure(fg_color="green", hover_color="light green", text_color="black")
            Interface.confirmar_modo = True
        else:
            self.label_nome.configure(text_color="white")
            self.entry_nome.configure(text_color="white")
            self.label_email.configure(text_color="white")
            self.entry_email.configure(text_color="white")
            self.label_N_Telefone.configure(text_color="white")
            self.entry_N_Telefone.configure(text_color="white")
            self.label_Senha.configure(text_color="white")
            self.entry_Senha.configure(text_color="white")
            self.label_D_Nascimento.configure(text_color="white")
            self.entry_D_Nascimento.configure(text_color="white")
            # Alterar a cor dos botões para verde no modo "Write"
            self.btn_cadastrar.configure(fg_color="#1d6ca4", hover_color="#144c74", text_color="white")
            self.bt_login.configure(fg_color="#1d6ca4", hover_color="#144c74", text_color="white")
            Interface.confirmar_modo = False
    
    # Formatação de Numero do telefone na caixa de entrada
    def formato_numero(self, event):
        current_text = self.entry_N_Telefone.get()
        cleaned_text = re.sub(r'[()-]', '', current_text)

        if len(cleaned_text) == 0 and event.char != '\b':
            self.entry_N_Telefone.insert(tkinter.END, '(')
        elif len(cleaned_text) == 2 and event.char != '\b':
            self.entry_N_Telefone.insert(tkinter.END, ') ')
        elif len(cleaned_text) == 8 and event.char != '\b':
            self.entry_N_Telefone.insert(tkinter.END, '-')
        
 
    # Formatação de Data na caixa de entrada
    def formato_data(self, event):
        
    # Adicione a barra automaticamente após cada dois caracteres
        current_text = self.entry_D_Nascimento.get()
        if len(current_text) == 2 or len(current_text) == 5:
            self.entry_D_Nascimento.insert(tkinter.END, '/')
             
    def cadastrar(self):
        email = self.entry_email.get()
        senha = self.entry_Senha.get()
        nome_full = self.entry_nome.get()
        telefone = self.entry_N_Telefone.get()
        dataN = self.entry_D_Nascimento.get()
        
        if not email or not senha or not nome_full or not telefone or not dataN:
            # Exibir messagebox de erro
            messagebox.showerror("ATENÇÃO", "Todos os campos são obrigatórios.")
        else:
            # Verificar formato do e-mail usando expressão regular
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                # Exibir messagebox de erro
                messagebox.showerror("Erro no E-mail", "Por favor, insira um endereço de e-mail válido.")
            else:
                senha_crip = self.hash_password(senha)
                self.salva_dados_usuario(email, senha_crip, nome_full, telefone, dataN)
        
                # Exibir messagebox de confirmação
                messagebox.showinfo("Cadastro Concluído", "Volte para tela de Login e efetue seu login e senha para proseguir")
        
    def criar_tabela(self):
        conn = sqlite3.connect("dados_formulario.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS formulario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telefone TEXT,
                cep TEXT,
                nome TEXT,
                assunto TEXT
            )
        ''')
        conn.commit()
        conn.close()
    # Adicione esta função para salvar os dados no banco de dados
    def salvar_dados_no_banco(self, dados):
        conn = sqlite3.connect("dados_formulario.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO formulario (telefone, cep, nome, assunto)
            VALUES (?, ?, ?, ?)
            ''', (dados['telefone'], dados['cep'], dados['nome'], dados['assunto']))
        conn.commit()
        conn.close()

    def Registrar(self):
        self .destroy()
        app = Interface()
        app.Registro()
        app.mainloop()
        
        
    def Logout(self):
        self.destroy()
        app = Interface()
        app.Login()
        app.mainloop()
    
    def Sair(self):
        # Fechar todas as janelas abertas
        self.destroy()
            
if __name__ == "__main__":
    app = Interface()
    app.Login()
    app.mainloop()
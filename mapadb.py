import json
import folium
import webbrowser
import os
class User:
    def __init__(self, email, password, full_name, phone_number):
        self.email = email
        self.password = password
        self.full_name = full_name
        self.phone_number = phone_number

    def __repr__(self):
        return f"User(email={self.email}, full_name={self.full_name})"

def validate_user_data(user):
    if not user.email or not user.password or not user.full_name or not user.phone_number:
        raise ValueError("Todos os campos são obrigatórios.")

    if not re.match(r"[^@]+@[^@]+\.[^@]+", user.email):
        raise ValueError("Email inválido.")

def save_user_data(user):
    with open("usuarios.json", "a") as file:
        json.dump(user, file)
        file.write('\n')

def load_user_data():
    users = []
    try:
        with open("usuarios.json", "r") as file:
            for line in file:
                user = json.loads(line)
                users.append(user)
    except FileNotFoundError:
        pass

    return users

def login(user):
    users = load_user_data()

    for user_in_users in users:
        if user_in_users.email == user.email and user_in_users.password == user.password:
            return True

    return False

# Lista para rastrear os marcadores adicionados
marcadores = []


def display_map():
    # Criar mapa
    map = folium.Map(location=[-22.9064, -47.0616], zoom_start=15)
    map.save("map.html")
    
def on_map_click(event):
    # Obtenha as coordenadas do local onde o clique ocorreu
    lat, lon = event.latlng
    
    # Crie um marcador com pop-up no local do clique
    marker = folium.Marker([lat, lon], tooltip='Novo Marcador').add_to(map)
     # Adicione o marcador à lista de marcadores
    marcadores.append(marker)

# Adicione um ouvinte de eventos de clique ao mapa
folium.ClickForMarker(popup='Clique para adicionar marcador').add_to(map)
# Adicione um objeto ClickForMarker ao mapa
folium.ClickForMarker(popup='Clique para adicionar marcador').add_to(map)

def register_user(user):
    try:
        save_user_data(user)
        print("Cadastro realizado com sucesso.")
    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")

# Função para validar os dados do usuário
def validate_user_data(user):
    # Verifica se todos os campos são obrigatórios
    if not user.email or not user.password or not user.full_name or not user.phone_number:
        raise ValueError("Todos os campos são obrigatórios.")

    # Verifica se o email é válido
    if not re.match(r"[^@]+@[^@]+\.[^@]+", user.email):
        raise ValueError("Email inválido.")


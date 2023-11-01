import folium
import hashlib
import json
import webbrowser

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_user_data(email, hashed_password, full_name, phone_number):
    with open("usuarios.json", "a") as file:
        data = {"email": email, "password": hashed_password, "full_name": full_name, "phone_number": phone_number}
        json.dump(data, file)
        file.write('\n')

def load_user_data():
    try:
        with open("usuarios.json", "r") as file:
            return [json.loads(line) for line in file]
    except FileNotFoundError:
        return []

def login():
    email = input("Email: ")
    password = input("Senha: ")

    users = load_user_data()
    user = next((user for user in users if user["email"] == email), None)

    if user and hash_password(password) == user["password"]:
        return True
    else:
        return False

def register():
    emailr = input("Seu Email: ")
    passwordr = input("Crie uma senha: ")
    full_namer = input("Nome Completo: ")
    phone_numberr = input("Numero de celular: ")

    hashed_password = hash_password(passwordr)
    save_user_data(emailr, hashed_password, full_namer, phone_numberr)
    print("Registro concluído.")

def display_map():
    map = folium.Map(location=[-22.9064, -47.0616], zoom_start=15)
    map.save("map.html")
    webbrowser.open("map.html", new=2)  # Abre o arquivo map.html no navegador padrão
    print("Map displayed successfully.")

def main():
    while True:
        print("\n\n\n Bem Vindo a nossa Plataforma. Seleciona uma das opcoes abaixo para continuar\n\n\n")
        choice = input("    1. Login\n\n    2. Registrar\n\n    3. Sair\n\n    Selecione uma opcao: \n\n")

        if choice == "1":
            if login():
                print("Login bem sucedido.")
                display_map()
                break
            else:
                print("Credenciais inválidas. Try again.")
        elif choice == "2":
            register()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

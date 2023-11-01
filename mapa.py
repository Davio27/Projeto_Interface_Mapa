import folium
import os

mapa = folium.Map(location=[-22.9064,-47.0616], zoom_star=12)

# Lista para rastrear os marcadores adicionados
marcadores = []

def on_map_click(event):
    # Obtenha as coordenadas do local onde o clique ocorreu
    lat, lon = event.latlng
    
    # Crie um marcador com pop-up no local do clique
    marker = folium.Marker([lat, lon], tooltip='Novo Marcador').add_to(mapa)
     # Adicione o marcador à lista de marcadores
    marcadores.append(marker)

# Adicione um ouvinte de eventos de clique ao mapa
folium.ClickForMarker(popup='Clique para adicionar marcador').add_to(mapa)
# Adicione um objeto ClickForMarker ao mapa
folium.ClickForMarker(popup='Clique para adicionar marcador').add_to(mapa)

# Função para desmarcar um marcador específico
def desmarcar_marcador(event):
    # Remova o marcador do mapa
    if isinstance(event.target, folium.ClickForMarker):
        # Remove o marcador do mapa
        # mapa.    (event.target)
        pass



# Adicione um objeto ClickForMarker para desmarcar marcadores
folium.ClickForMarker(popup='Clique para desmarcar marcador').add_to(mapa)

# Salve o mapa em um arquivo HTML
pasta_dest = "C:\\Users\\davic\\OneDrive\\Documentos\\main project\\projeto_mapa"
nome_arquivo = "mapa.html"
caminho_arquivo = os.path.join("projeto_mapa", "mapa.html")
mapa.save(caminho_arquivo)


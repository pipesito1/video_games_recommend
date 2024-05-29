from fastapi import FastAPI, Query
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



app = FastAPI(title='Proyecto Integrador Numero 1 Jesus Felipe Sepulveda')
@app.get('/',tags=['Home'])

async def Home():
    return 'Bienvenidos a la API del Proyecto Individual de Steam'

@app.get('/about', tags=['About this Proyect'])
async def about():
    return 'Proyecto Individual Numero 1, Machine Learning Operations (MLOps) Jesus Felipe Sepulveda'

@app.get('/Developer', tags=['GET'])

def developer(desarrollador: str):
    developer = pd.read_parquet('dataSet/developer_endpoint.parquet')
    developer= developer[developer['developer'] == desarrollador]
    if developer.empty:
        return "No hay datos para el desarrollador especificado."
    
    # Agrupar por año
    grouped = developer.groupby('Year').agg(
        total_items=('price', 'count'),
        free_items=('price', lambda x: (x == 0).sum())
    ).reset_index()
    
    # Calcular el porcentaje de contenido gratuito
    grouped['free_percentage'] = (grouped['free_items'] / grouped['total_items']) * 100

    # Crear un diccionario con los resultados
    result = {}
    for _, row in grouped.iterrows():
        year = row['Year']
        total_items = row['total_items']
        free_percentage = row['free_percentage']
        
        result[year] = {
            'Cantidad de items': total_items,
            'Porcentaje de contenido Free': free_percentage
        }
    
    return result

@app.get('/recomendacion_juego/{id_de_producto}', tags=['GET'])

def recomendacion_juego(id_de_producto:str):
    modelo = pd.read_parquet('dataSet/steam_game_clean.parquet')
    
    game = modelo[modelo['id'] == id_de_producto]
    # Extraer el género del juego
    if game.empty:
        print("Producto no encontrado")
        return
    
    genres = game['genres'].iloc[0]  # Obtener el primer elemento, ya que 'genres' es una serie
    
    # Para hacer recomendaciones, puedes buscar los productos más similares a un producto dado
    
    producto = modelo[modelo['genres'] == genres]

    if not producto.empty:
        product_index = producto.index[0]
        genres_p = producto['genres']
        #instanceo el vectoridador para utilizarlo
        vector = TfidfVectorizer()
        #tranforma en numeros las palabras para que el modelo entienda 
        matriz = vector.fit_transform(genres_p)
        product_similarities = cosine_similarity(matriz)
        product_similarities = list(enumerate(product_similarities))
        similar_games = [producto.iloc[i[0]] for i in product_similarities]
        print("Los productos más similares al producto son:")
        print (similar_games[1:6])
    else:         
        print("Producto no encontrado")


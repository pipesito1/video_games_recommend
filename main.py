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

# JESUS FELIPE SEPULVEDA ALVAREZ

## Descripción del Proyecto

Este proyecto cubre todas las fases del ciclo de vida de un proyecto de Machine Learning. El resultado final es una API desplegada en Render, la cual permite realizar consultas a los registros de una base de datos de la plataforma Steam. Además, se desarrolló un modelo de recomendación de videojuegos basado en la similitud del coseno, accesible también a través de la API.

## División del Proyecto

### Parte I: Data Engineering
Comenzamos desde cero, abordando tareas propias de un ingeniero de datos, incluyendo la recolección, extracción, tratamiento, transformación y modelado de datos.

### Parte II: Machine Learning
Construimos el modelo de machine learning, utilizando los datos ya procesados. Entrenamos un sistema de recomendación de videojuegos para usuarios de Steam, empleando técnicas de MLOps para garantizar la escalabilidad, reproducibilidad y mantenibilidad del modelo y la API.

## Objetivos

- **Transformaciones de Datos**: Limpiar y procesar el dataset, eliminando columnas innecesarias y optimizando el rendimiento, considerando la baja madurez de los datos (datos anidados, formato raw, sin procesos automatizados de actualización).
  - [Link de descarga de Datasets (ETL aplicado)](#) 
  - [Diccionario de datos](#)

- **Feature Engineering**: Realizar análisis de sentimiento en las reseñas de usuarios y crear una nueva columna 'sentiment_analysis'.

- **Desarrollo de API**: Implementar una API con FastAPI para consultas de datos y recomendaciones.

- **Despliegue**: Hacer la API accesible públicamente a través de un servicio web.

- **Análisis Exploratorio de Datos (EDA)**: Explorar y visualizar los datos para obtener insights valiosos.
  - [Artículo de interés](#)

- **Modelo de Aprendizaje Automático**: Desarrollar un sistema de recomendación basado en la similitud del coseno.

## Estructura del Proyecto

- **Data**: Archivos `.parquet` (5 archivos) generados del proceso ETL, base para consultas y modelado.
- **Notebooks**: Jupyter notebooks para ETL y EDA.
- **main.py**: Archivo principal de la API (consultas y modelo de recomendación).
- **requirements.txt**: Lista de dependencias del proyecto.
- **README.md**: Descripción y guía del proyecto.

## Pasos Realizados

### Transformaciones de Datos

- Lectura y preprocesamiento de datasets en el formato correcto.
- Limpieza y manejo de datos nulos y anidados.
- Las transformaciones están documentadas en los notebooks `etl_steam`, `etl_user_items` y `etl_user_reviews`.

### Feature Engineering

- Análisis de sentimiento en las reseñas de usuarios.
- Creación de la columna 'sentiment_analysis' con valores 0 (negativo), 1 (neutral) y 2 (positivo) usando la librería NLTK.

### Desarrollo de API

Se implementaron los siguientes endpoints utilizando FastAPI:

- `developer(desarrollador: str)`: Cantidad de items y porcentaje de contenido gratuito por año según la empresa desarrolladora.
- `userdata(User_id: str)`: Cantidad de dinero gastado por el usuario, porcentaje de recomendación y cantidad de items.
- `UserForGenre(genero: str)`: Usuario con más horas jugadas para el género dado y acumulación de horas jugadas por año de lanzamiento.
- `best_developer_year(año: int)`: Top 3 desarrolladores con juegos más recomendados por usuarios en el año dado.
- `developer_reviews_analysis(desarrolladora: str)`: Análisis de reseñas de usuarios categorizadas por análisis de sentimiento (positivo o negativo).
- `recomendacion_juego(id_de_producto: str)`: Lista de 5 juegos recomendados similares al ingresado.

### Despliegue

La API se desplegó en Render, haciendo que sea accesible públicamente desde cualquier dispositivo conectado a Internet.

### Análisis Exploratorio de Datos (EDA)

Análisis exploratorio para entender las relaciones entre variables, detectar outliers y descubrir patrones interesantes.

### Modelo de Aprendizaje Automático

Sistema de recomendación basado en la similitud del coseno:

- **Input**: ID de un producto.
- **Output**: Lista de 5 juegos recomendados similares al ingresado.

### Video de Demostración

[Video de demostración](#) mostrando el funcionamiento de las consultas de la API y el modelo de ML entrenado, explicando brevemente el despliegue del proyecto.

## Tecnología Utilizada

- **Python**: Lenguaje de programación principal.
- **FastAPI**: Framework para el desarrollo de la API.
- **Pandas**: Manipulación y análisis de datos.
- **Scikit-learn**: Desarrollo del modelo de recomendación.
- **NLTK**: Análisis de sentimiento.
- **Render**: Despliegue de la API.
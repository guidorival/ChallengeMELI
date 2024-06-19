from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

# Definir los parámetros de conexión
host = '127.0.0.1'
database = 'netflix'
user = 'root'
password = 'guido'

try:
    connection = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    engine = create_engine(connection)
    print("Base de datos leida correctamente!")
except Exception as e:
    print(f"Error al cargar la base de datos: {e}")
    
# Consulta SQL para seleccionar datos
query = "SELECT * FROM films;"

# Ejecutar la consulta y cargar los resultados en un DataFrame de pandas
try:
    with engine.connect() as connection:
        df = pd.read_sql(query, engine)
        print("Datos cargados correctamente!")
except Exception as e:
    print(f"Error al ejecutar la consulta SQL: {e}")

# Filtro por Peliculas
peliculas_df = df[df['type'] == 'Movie']
# Crear el histograma
peliculas_df['duration'].plot(kind='hist', bins=30, edgecolor='black')

# Configurar el título y los ejes del histograma
plt.title('Histograma de la duracion de las Peliculas')
plt.xlabel('Valores de duracion')
plt.ylabel('Frecuencia')

# Mostrar el histograma
plt.show()

# Crear el boxplot
plt.boxplot(peliculas_df['duration'], vert=False, patch_artist=True)
    
# Configurar el título y los ejes del box plot
plt.title('Box Plot de la duracion de las Peliculas')
plt.xlabel('Valores de duracion')

# Mostrar el box plot
plt.show()

## Filtro por Series
series_df = df[df['type'] == 'TV Show']
# Crear el histograma
series_df['duration'].plot(kind='hist', bins=15, edgecolor='black')

# Configurar el título y los ejes del histograma
plt.title('Histograma de la duracion de las Series')
plt.xlabel('Valores de duracion')
plt.ylabel('Frecuencia')

# Mostrar el histograma
plt.show()
plt.boxplot(series_df['duration'], vert=False, patch_artist=True)
    
# Configurar el título y los ejes del box plot
plt.title('Box Plot de la duracion de las Series')
plt.xlabel('Valores de duracion')

# Mostrar el box plot
plt.show()


# Agrupar por año y contar el número de títulos por año
titles_per_year = df.groupby('year_added').size()

# Convertir el resultado a un DataFrame para facilitar la visualización
titles_per_year = titles_per_year.reset_index(name='count')

plt.plot(titles_per_year['year_added'], titles_per_year['count'], marker='o')

# Configurar el título y los ejes del gráfico
plt.title('Número de títulos lanzados por año')
plt.xlabel('Año')
plt.ylabel('Número de títulos')
plt.grid(True)

# Mostrar el gráfico
plt.show()

engine.dispose()
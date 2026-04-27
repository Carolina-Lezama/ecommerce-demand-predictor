import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import glob

# Cargar variables del .env
load_dotenv()

USER = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')
HOST = os.getenv('POSTGRES_HOST')
PORT = os.getenv('POSTGRES_PORT')
DB = os.getenv('POSTGRES_DB')

# Crear la conexión a la base de datos
engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}')

def load_csv_to_postgres():
    # Buscar todos los archivos CSV en la carpeta data
    csv_files = glob.glob('data/*.csv')
    
    for file in csv_files:
        # Extraer el nombre de la tabla desde el nombre del archivo
        # Ejemplo: data/olist_customers_dataset.csv -> olist_customers_dataset
        table_name = os.path.basename(file).replace('.csv', '')
        
        print(f"Cargando {table_name}...")
        
        # Leer el CSV con Pandas
        df = pd.read_csv(file)
        
        # Enviar el DataFrame a PostgreSQL
        # if_exists='replace' sobrescribe la tabla si ya existe
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"{table_name} cargada exitosamente.\n")

if __name__ == "__main__":
    load_csv_to_postgres()
    print("¡Todos los datos han sido cargados a la base de datos!")

# crear una tabla por cada archivo CSV
# Ejecutar py load_data.py
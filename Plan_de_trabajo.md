# Stack Tecnológico para este Proyecto
- Almacenamiento y Extracción: PostgreSQL
- Limpieza, EDA y Modelado: Python
- Despliegue y API: FastAPI
- Contenedorización: Docker
- Nube: Google Cloud Platform
- Monitoreo/Tracking: MLflow

Plan de Trabajo: End-to-End MLOps Project
1. Configuración de Entorno y Repositorio
    1.1. Inicialización de repositorio en GitHub con estructura profesional.

    1.2. Configuración de entorno virtual (venv o conda) y gestión de dependencias (requirements.txt).

    1.3. Setup de Docker Desktop para contenerizar la base de datos local (PostgreSQL).

2. Ingesta de Datos y Arquitectura SQL
2.1. Descarga del dataset de Olist y carga en una base de datos PostgreSQL mediante scripts de Python.

    2.2. Diseño de consultas SQL avanzadas para consolidar tablas (pedidos, productos, vendedores, geolocalización).

    2.3. Creación de una "Gold Table" optimizada para el modelo mediante procesos ETL (Extract, Transform, Load).

3. Análisis Exploratorio de Datos (EDA) y Limpieza
3.1. Identificación y tratamiento de outliers y valores faltantes.

    3.2. Análisis de estacionalidad, tendencias de ventas y correlación de precios.

    3.3. Análisis geoespacial de las entregas y su impacto en la satisfacción del cliente.

4. Feature Engineering y Preprocesamiento
4.1. Creación de variables temporales (mes, día de la semana, festivos).

    4.2. Ingeniería de características de usuario (RFM: Recencia, Frecuencia, Valor Monetario).

    4.3. Codificación de variables categóricas y escalamiento de datos numéricos.

5. Modelado y ML Ops (Tracking)
5.1. Selección de algoritmos (XGBoost, LightGBM o modelos de Series Temporales).

    5.2. Implementación de MLflow para el registro de experimentos, hiperparámetros y versiones del modelo.

    5.3. Evaluación mediante métricas de negocio (MAE, RMSE, Error Porcentual).

6. Desarrollo de API con FastAPI
6.1. Creación de un servidor con FastAPI para exponer el modelo.

    6.2. Implementación de endpoints de predicción (POST) que reciban datos del producto y devuelvan la demanda estimada.

    6.3. Validación de datos de entrada utilizando Pydantic.

7. Contenedorización y Despliegue en la Nube
    7.1. Creación de un Dockerfile para empaquetar la aplicación FastAPI.

    7.2. Configuración de Google Cloud Platform (GCP) o AWS.

    7.3. Despliegue continuo mediante Google Cloud Run o AWS App Runner.

8. Monitoreo y Visualización Final
8.1. Implementación de logs básicos para monitorear las predicciones de la API.

    8.2. Creación de un Dashboard interactivo (Streamlit o Looker Studio) con los resultados del modelo.

    8.3. Documentación final y redacción del "Case Study" en el README.

# Otros:
- .ipynb para: El EDA (Análisis Exploratorio de Datos), probar hipótesis, hacer gráficos rápidos y entender tus datos.
- .py para: El proyecto final. Traducir el código del notebook a módulos estructurados.
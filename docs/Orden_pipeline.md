# Orden canónico de un Pipeline de Machine Learning

## 1. Exploración y Limpieza Básica:

Aquí revisas los tipos de datos (convertir textos a fechas, números a floats) y eliminas filas o columnas que son completamente inútiles o tienen 100% de valores nulos. También se eliminan las filas donde tu variable objetivo (target_demanda) es nula, porque no puedes entrenar si no sabes la respuesta.


## 2.Ingeniería de Características (Feature Engineering):

Creación de patrones.Extraes información útil de lo que tienes. De una fecha sacas el día de la semana; creas promedios móviles (rolling means), cuentas de transacciones pasadas y rezagos (lags).

## 3.Separación de Datos (Data Splitting):

Divides tu dataset en Entrenamiento (Train) y Prueba (Test). A partir de este momento, el conjunto de Test se guarda en una caja fuerte. Cualquier cálculo estadístico (medias, desviaciones) que necesites para los siguientes pasos, se extrae exclusivamente del conjunto Train.

## 4.Imputación de Nulos:

Rellenando los huecos. Para los valores faltantes en tus variables predictoras (X), decides si rellenarlos con la media, la mediana o un valor constante (como ceros). 

Se calcula las medidas usando solo X_train y se aplica tanto a X_train como a X_test.

## 5.Codificación de Categóricas (One-Hot Encoding):

Aquí conviertes categorías en números o en columnas binarias (1 y 0) usando técnicas como One-Hot Encoding o Label Encoding.

## 6.Escalado y Estandarización:

Si tienes una columna de "precio" que va de 10 a 5,000 reales y otra de "cantidad de fotos" que va de 1 a 5, el modelo podría darle más importancia al precio solo porque el número es más grande. Aquí usas un StandardScaler o MinMaxScaler para comprimir todas las variables al mismo rango (usualmente entre 0 y 1, o con media 0 y varianza 1).

## 7.Entrenamiento del Modelo:Fit.

Le pasas tu X_train ya procesada y tu y_train al algoritmo (como Random Forest, XGBoost o Regresión Lineal) para que aprenda las reglas matemáticas que conectan los datos con la demanda.

## 8.Predicción y Evaluación:
Pasas tu X_test por los mismos pasos de transformación (imputación, codificación, escalado) y le pides al modelo que prediga. Finalmente, comparas esas predicciones contra tu y_test real usando métricas de error (como RMSE o MAE).

En la práctica moderna, los pasos del 4 al 6 se empaquetan en un objeto de scikit-learn llamado Pipeline y ColumnTransformer, lo que automatiza las transformaciones y evita que cometamos errores al pasar de Train a Test
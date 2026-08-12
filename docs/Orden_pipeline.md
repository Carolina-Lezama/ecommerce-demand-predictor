# Orden canónico de un Pipeline de Machine Learning

## 1. Exploración y Limpieza Básica:

Aquí revisas los tipos de datos (convertir textos a fechas, números a floats) y eliminas filas o columnas que son completamente inútiles o tienen 100% de valores nulos. También se eliminan las filas donde tu variable objetivo (target_demanda) es nula, porque no puedes entrenar si no sabes la respuesta.

## 2.Ingeniería de Características (Feature Engineering):

Creación de patrones.Extraes información útil de lo que tienes. De una fecha sacas el día de la semana; creas promedios móviles (rolling means), cuentas de transacciones pasadas y rezagos (lags).

## 3.Separación de Datos (Data Splitting):

Divides tu dataset en Entrenamiento (Train) y Prueba (Test). A partir de este momento, el conjunto de Test se guarda en una caja fuerte. Cualquier cálculo estadístico (medias, desviaciones) que necesites para los siguientes pasos, se extrae exclusivamente del conjunto Train.

## 3.1 Manejo de Outliers (Valores atípicos)

Antes de escalar, a veces tienes que "recortar" o eliminar valores ridículamente altos que sabes que son errores (ej. un usuario con edad de 999 años).

Se calculan en Train, se aplican a Train (y las reglas de X se replican en Test).

## 4.Imputación de Nulos:

Rellenando los huecos. Para los valores faltantes en tus variables predictoras (X), decides si rellenarlos con la media, la mediana o un valor constante (como ceros).

Se calcula las medidas usando solo X_train y se aplica tanto a X_train como a X_test.

## 5.Codificación de Categóricas (One-Hot Encoding):

Aquí conviertes categorías en números o en columnas binarias (1 y 0) usando técnicas como One-Hot Encoding o Label Encoding.

## 6.Escalado y Estandarización:

Si tienes una columna de "precio" que va de 10 a 5,000 reales y otra de "cantidad de fotos" que va de 1 a 5, el modelo podría darle más importancia al precio solo porque el número es más grande. Aquí usas un StandardScaler o MinMaxScaler para comprimir todas las variables al mismo rango (usualmente entre 0 y 1, o con media 0 y varianza 1).

## 6.1 Selección de Características:
Analizas correlaciones o usas algoritmos (como Lasso) solo en Train para elegir las mejores columnas. Test simplemente se adapta y tira las columnas que Train decidió no usar.

## 6.2 Balanceo de Clases: (Ej. SMOTE). 

¡Se aplica ÚNICAMENTE a Train! Si balanceas antes del split o balanceas el Test, arruinas la evaluación, porque estarías evaluando tu modelo en datos inventados o en una proporción que no existe en el mundo real.

## 7.Entrenamiento del Modelo:Fit.

Le pasas tu X_train ya procesada y tu y_train al algoritmo (como Random Forest, XGBoost o Regresión Lineal) para que aprenda las reglas matemáticas que conectan los datos con la demanda.

## 8.Predicción y Evaluación:

Pasas tu X_test por los mismos pasos de transformación (imputación, codificación, escalado) y le pides al modelo que prediga. Finalmente, comparas esas predicciones contra tu y_test real usando métricas de error (como RMSE o MAE).

En la práctica moderna, los pasos del 4 al 6 se empaquetan en un objeto de scikit-learn llamado Pipeline y ColumnTransformer, lo que automatiza las transformaciones y evita que cometamos errores al pasar de Train a Test

# ¿Siempre se eliminan las filas donde Y es nulo?

En el 99% de los casos de aprendizaje supervisado, sí.

¿Y si pierdo demasiados datos? Si notas que el 40% de tu objetivo es nulo, no debes simplemente borrarlo. Tienes que investigar por qué es nulo. ¿un nulo significa que hubo cero ventas ese día? Si es así, no lo borras, lo rellenas con un 0. Si es un fallo del sistema y realmente no sabes qué pasó, es mejor descartar esa fila que enseñarle basura al modelo.

# ¿La variable Target (Y) nunca se modifica?

Sí se puede (y a veces se debe) modificar.

En Clasificación: Si tu "Y" es texto ("Compró", "No compró"), tienes que hacerle un Encoding

En Regresión: Es cierto que rara vez se estandariza o se escala de 0 a 1, pero es súper común aplicarle una transformación logarítmica. Si tienes una demanda donde la mayoría de los días vendes 10 productos, pero en el "Buen Fin" vendes 5,000, la gráfica está muy sesgada. Aplicarle un logaritmo a "Y" comprime esos picos extremos, ayuda al modelo a aprender mejor

# ¿No todos los modelos necesitan escalado?

Modelos sensibles (Requieren escalado): Regresión Lineal/Logística, Redes Neuronales, K-Nearest Neighbors (KNN) y Máquinas de Soporte Vectorial (SVM). Estos algoritmos usan geometría, distancias o gradientes. Si una variable está en miles y otra en decimales, el modelo se vuelve loco.

Modelos inmunes (NO requieren escalado): Los basados en árboles de decisión (Decision Tree, Random Forest, XGBoost, LightGBM). Estos algoritmos simplemente buscan un punto de corte

# ¿Imputar valores de Y no es erróneo?

Sí, estadísticamente es un pecado capital. Nunca debes usar la media o mediana para "inventar" la respuesta que el modelo debe aprender. Si no tienes la respuesta real, esa fila no sirve para entrenar

En proyectos de predicción de demanda, si tienes un registro de un producto un martes y la cantidad de ventas es nula, muchas veces en las bases de datos transaccionales eso no es un "dato perdido", sino que simplemente se vendieron cero unidades. En ese caso, cambiar el nulo por un 0 no es imputar, es reconstruir la realidad comercial. Si el nulo viene por un fallo del servidor y realmente no sabes si se vendió algo, entonces sí, la fila se elimina sin piedad.

# ¿Qué pasa con los Outliers (especialmente en el Target)?

Errores de captura (Tratamiento ANTES del split): Si tienes un producto con un peso de "-5 kg" o un usuario que compró en el año "2050", eso es basura. Eso se elimina en la Exploración y Limpieza Básica, antes del split.

Outliers estadísticos reales (Tratamiento DESPUÉS del split): Por ejemplo, un usuario que gastó 50,000 reales en un día. Es un dato real, pero extremo.

- En X (Variables predictoras): Calculas los límites (como los cuartiles) usando solo el conjunto de Train y "recortas" o transformas esos valores atípicos. Luego aplicas esos mismos límites de Train al Test.
- En Y (Target): Si tienes un pico anormal de demanda en Train, puedes recortarlo (capping) para evitar que el modelo se desvíe tratando de aprender un evento que fue casualidad. Pero el Y de Test NO se toca. El mundo real tiene anomalías y tu Test debe ser un reflejo cruel y exacto del mundo real.

# ¿y es siempre una sola columna (Series)?
En la gran mayoría de los casos tradicionales (y en nuestro proyecto actual para predecir la demanda), sí, es una sola columna (una pd.Series).

Sin embargo, los algoritmos modernos permiten tener un y de múltiples columnas. A esto se le llama Multi-output Regression o Multi-label Classification. Por ejemplo, si con las mismas variables de entrada (X) quisieras que un solo modelo te prediga simultáneamente la demanda en unidades (columna 1) y el ingreso en reales (columna 2).

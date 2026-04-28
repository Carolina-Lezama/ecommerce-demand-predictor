import pandas as pd
from sqlalchemy import create_engine

# Los datos vienen de tu archivo .env
engine = create_engine('postgresql://usuario:password@localhost:5433/ecommerce_db')

# En lugar de leer un CSV, lanzas una consulta SQL
query = """
SELECT 
    c.customer_city, 
    COUNT(o.order_id) as total_pedidos
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_city
ORDER BY total_pedidos DESC
LIMIT 10;
"""

df_top_ciudades = pd.read_sql(query, engine)
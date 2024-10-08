import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("vgsales.csv")



# Seleccionar columnas
juegos = df['Name'][:10]  # Selecciona los primeros 10 juegos
ventas_globales = df['Global_Sales'][:10]

# Gráfico de barras
plt.bar(juegos, ventas_globales, color='skyblue')
plt.title("Ventas Globales de Videojuegos")
plt.xlabel("Juegos")
plt.ylabel("Ventas Globales (millones)")
plt.xticks(rotation=45)
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("grafico.csv")

cantidad = df['Review_type'].value_counts()
colores = ["blue", "green", "yellow", "orange", "red", "gray", "purple", "black"]
cantidad.plot(kind="bar", color=colores)
plt.title("Reviews")
plt.xlabel("Tipo de review")
plt.ylabel("Cantidad")
#plt.axis('equal')
plt.show()



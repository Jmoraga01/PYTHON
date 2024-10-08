import matplotlib.pyplot as plt

comida = ["Hamburgguesa", "Pizza", "Pupusas", "Tacos"]
frecuencia = [6,10,4,3]
colores = ["red", "yellow", "gray", "green"]
plt.bar(comida,frecuencia,color=colores)

plt.title("Opciones para el almuerzo por el dia del niño")
plt.xlabel("Opciones de comida")
plt.ylabel("Votos")
plt.show()
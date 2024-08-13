# Este ejercicio lo realise de tal forma porque tenia en la mente crear un registro de estudiantes 
# y afuturo poder mejorar para asi poder crear una plataforma de registro de estudiante.

class Estudiantes:
    def __init__(self, nombre, edad, materia, promedio, id_estudiante):
        self.nombre = nombre
        self.edad = edad
        self.materia = materia 
        self.promedio = promedio
        self.id_estudiante = id_estudiante

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Materia: {self.materia}")
        print(f"Promedio de Calificaciones: {self.promedio}")
        print(f"ID de Estudiante: {self.id_estudiante}")
        print()

# Lista para almacenar los estudiantes
lista_estudiantes = []

# Agregar estudiantes a la lista
while True:
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    materia = input("Ingrese la materia: ")
    promedio = float(input("Ingrese el promedio del estudiante: "))
    id_estudiante = input("Ingrese el ID del estudiante: ")

    nuevo_estudiante = Estudiantes(nombre, edad, materia, promedio, id_estudiante)
    lista_estudiantes.append(nuevo_estudiante)

    # Preguntar si se desea agregar otro estudiante
    agregar_otro = input("¿Desea agregar otro estudiante? (s/n): ")
    if agregar_otro.lower() != 's':
        break

# Mostrar la información de todos los estudiantes
print("\nInformación de los estudiantes registrados:")
for estudiante in lista_estudiantes:
    estudiante.mostrar_informacion()


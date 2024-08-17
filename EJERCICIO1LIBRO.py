#EJ1 Una veterinaria atiende solamente perros y los registra en una base de datos. 
# Se requiere un programa que lea la información básica del perro (no más de 8 características)
#  y se muestre en pantalla. En esta veterinaria todos los animales que llegan,
#  entran con el estado inicial de NO ATEN- DIDO y cuando se registran se cambia automáticamente a ATENDIDO.
#  Por ahora como la veterinaria solo atiende perros, basado en el peso (menos de 10kg o más de 10kg) 
# los registra como “Perro Grande” o “Pe- rro Pequeño”.

class chucho:
    def __init__(self, nombre, raza, edad, peso, color, nombre_dueño, direccion_dueño, telefono_dueño):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.nombre_dueño = nombre_dueño
        self.direccion_dueño = direccion_dueño
        self.telefono_dueño = telefono_dueño
        self.estado = "NO ATENDIDO"
        self.tamano = "Perro Grande" if peso >= 10 else "Perro Pequeño"
    
    def registrar(self):
        self.estado = "ATENDIDO"
        self.mostrar_informacion()
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Color: {self.color}")
        print(f"Nombre del Dueño: {self.nombre_dueño}")
        print(f"Dirección del Dueño: {self.direccion_dueño}")
        print(f"Teléfono del Dueño: {self.telefono_dueño}")
        print(f"Estado: {self.estado}")
        print(f"Tamaño: {self.tamano}")

nombre = input("Nombre del perro: ")
raza = input("Raza: ")
edad = int(input("Edad: "))
peso = float(input("Peso (en kg): "))
color = input("Color: ")
nombre_dueño = input("Nombre del dueño: ")
direccion_dueño = input("Dirección del dueño: ")
telefono_dueño = input("Teléfono del dueño: ")

perro = chucho(nombre, raza, edad, peso, color, nombre_dueño, direccion_dueño, telefono_dueño)
perro.registrar()

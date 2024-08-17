
#EJE3 Un concesionario de autos vende vehículos nacionales e importados.
#  Todos tienen 4 ruedas y capacidad para 5 pasajeros. 
# Esta información debe registrarse siempre por razones de ley. 
# Requiere un programa que le permita almacenar las 10 principales características de los autos. 
# El precio de venta de cada auto es igual al precio de compra
#  multiplicado por 1.4 que corresponde a su margen de ganancia.

class Auto:
    def __init__(self, marca, modelo, año, color, tipo_motor, tipo_combustible, kilometraje, precio_compra, origen, transmision):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo_motor = tipo_motor
        self.tipo_combustible = tipo_combustible
        self.kilometraje = kilometraje
        self.precio_compra = precio_compra
        self.origen = origen  
        self.transmision = transmision  
        self.precio_venta = self.calcular_precio_venta()
        self.ruedas = 4
        self.capacidad_pasajeros = 5

    def calcular_precio_venta(self):
        return self.precio_compra * 1.4

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Tipo de Motor: {self.tipo_motor}")
        print(f"Tipo de Combustible: {self.tipo_combustible}")
        print(f"Kilometraje: {self.kilometraje} km")
        print(f"Transmisión: {self.transmision}")
        print(f"Origen: {self.origen}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad de Pasajeros: {self.capacidad_pasajeros}")
        print()

# informacion de vehiculo
auto1 = Auto(
    marca="Toyota",
    modelo="Corolla",
    año=2023,
    color="Blanco",
    tipo_motor="1.8L",
    tipo_combustible="Gasolina",
    kilometraje=0,
    precio_compra=20000.0,
    origen="Nacional",
    transmision="Automática"
)

auto2 = Auto(
    marca="BMW",
    modelo="X5",
    año=2022,
    color="Negro",
    tipo_motor="3.0L",
    tipo_combustible="Diesel",
    kilometraje=5000,
    precio_compra=45000.0,
    origen="Importado",
    transmision="Automática"
)

#información
auto1.mostrar_informacion()
auto2.mostrar_informacion()

#EJE4 Un almacén vende dispositivos electrónicos (celulares, tablets y portá- tiles). 
# Todos PHR que es una nueva marca que está entrando en el mer- cado. 
# Se requiere almacenar sus 6 principales características. 
# Todos son productos importados y su precio de venta es igual al precio de compra multiplicado por 1.7 
# que corresponde a su margen de ganancia.

class DispositivoElectronico:
    def __init__(self, tipo, modelo, pantalla, almacenamiento, procesador, ram, precio_compra):
        self.tipo = tipo
        self.marca = "PHR"
        self.modelo = modelo
        self.pantalla = pantalla
        self.almacenamiento = almacenamiento
        self.procesador = procesador
        self.ram = ram
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.7
        self.origen = "Importado"

    def mostrar_informacion(self):
        print(f"{self.tipo} {self.marca} {self.modelo}")
        print(f"Pantalla: {self.pantalla} pulgadas, Almacenamiento: {self.almacenamiento} GB")
        print(f"Procesador: {self.procesador}, RAM: {self.ram} GB")
        print(f"Precio de Compra: ${self.precio_compra:.2f}, Precio de Venta: ${self.precio_venta:.2f}")
        print(f"Origen: {self.origen}\n")

dispositivos = [
    DispositivoElectronico("Celular", "X1", 6.5, 128, "Snapdragon 888", 8, 300.0),
    DispositivoElectronico("Tablet", "Tab Pro", 10.1, 256, "Apple A12Z", 6, 500.0),
    DispositivoElectronico("Portátil", "Laptop Ultra", 15.6, 512, "Intel Core i7", 16, 1000.0)
]

for dispositivo in dispositivos:
    dispositivo.mostrar_informacion()

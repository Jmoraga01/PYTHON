PI=3.14

def hacer_PIZZA(ingr,tam,tipom, nomb,cant):
    print(f"Haz pedido {cant} pizza de ingrediente {ingr}"
          +f" de tamaño {tam} de masa {tipom}"  
          +f" es el banquete {nomb}")
    
def datosu(nombre,direc,telef): 
        print(f"Datos personales: \n"
          +f" 1-Nombre del cliente: {nombre} \n"
          +f" 2-Direccion:{direc} \n"
          +f" 3-Numero de telefono:{telef} \n")
        
def calculo(cilindro,cono,esfera):
    volumen_cilindro = PI * cilindro['radio']**2 * cilindro['altura']
    volumen_cono = (1/3) * PI * cono['radio']**2 * cono['altura']
    volumen_esfera = (4/3) * PI * esfera['radio']**3
    print("Calculo de volumen:\n"
          f"1-Calculo de volumen cilindro es: {volumen_cilindro}\n"
          f"2-Calculo de volumen cono es: {volumen_cono}\n"
          f"3-Calculo de volumen de esfera es: {volumen_esfera}")
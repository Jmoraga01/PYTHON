#wile
"""
i=0
while i<10:
    print("valor de i {i}")
    i+=1
    #i=i+1
"""
"""
valor = int(input("escribe un  numero:"))
i=1
while(i<valor):
    print(i)
    i+=1
"""
"""
numero = int(input("Digite el número que desea para la tabla de multiplicar: "))
i = 1
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1
"""
"""
while True:
    numero = int(input("Digite el número que desea para la tabla de multiplicar: "))
    i = 1
    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")
        i+=1
    op=input("Seleccione una opcion:\n"+
          "1-pedir numero:\n"+
          "2-salir\n")
    if(op=="1"):
        continue
    elif(op=="2"):
        break
    else:
        print("opcion incorrecta")
"""
contraseña_correcta = "Progra124"
while True:
    contraseña_ingresada = input("Introduce la contraseña: ")
    if contraseña_ingresada == contraseña_correcta:
        print("Contraseña correcta. Acceso concedido.")
        break  
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
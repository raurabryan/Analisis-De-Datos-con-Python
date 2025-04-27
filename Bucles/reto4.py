
datos = []

numero_datos = int(input("Ingrese la cantidad de datos a ingresar: "))

for i in range(numero_datos):
    valor_ingresado = input("Ingrese un dato: ")
    if valor_ingresado.isdigit():
        datos.append(int(valor_ingresado))
    elif valor_ingresado.replace('.', '', 1).isdigit() and valor_ingresado.count('.') < 2:
        datos.append(float(valor_ingresado))
    else:
        datos.append(valor_ingresado)


print(f"La lista es: {datos}")
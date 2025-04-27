from informacion import agregar_nombre, agregar_edad, nombre_paciente, edad

cantidad = int(input("¿Cuántos pacientes deseas ingresar?: "))

for i in range(cantidad):
    nombre = input(f"Ingrese el nombre completo del paciente : ")
    año = input(f"Ingrese el año de nacimiento de {nombre}: ")
    agregar_nombre(nombre)
    agregar_edad(año)

print("\nNombres de los pacientes:")
print(nombre_paciente)

print("\nEdades de los pacientes:")
print(edad)

mayor_edad = max(edad)
menor_edad = min(edad)

indice_mayor = edad.index(mayor_edad)
indice_menor = edad.index(menor_edad)

print("\nPaciente mayor:")
print(f"{nombre_paciente[indice_mayor]} con la edad de {mayor_edad} años.")

print("\nPaciente menor:")
print(f"{nombre_paciente[indice_menor]} con la edad de {menor_edad} años.")
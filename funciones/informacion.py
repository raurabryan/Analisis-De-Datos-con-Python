
nombre_paciente = []
edad = []

def agregar_nombre(nombre_completo):
    nombre_paciente.append(nombre_completo)

def agregar_edad(año_nacimiento):
    año_actual = 2025
    edad_actual = año_actual - int(año_nacimiento)
    edad.append(edad_actual)
from auto import Auto  

marca = input("Ingrese la marca del auto: ")
modelo = input("Ingrese el modelo del auto: ")
año = int(input("Ingrese el año del auto: "))

mi_auto = Auto(marca, modelo, año)

while True:
    print("\n¿Qué deseas hacer?")
    print("1. Mostrar información del auto")
    print("2. Actualizar kilometraje")
    print("3. Realizar un viaje")
    print("4. Mostrar estado del auto")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        mi_auto.mostrar_informacion()
    elif opcion == "2":
        nuevo_kilometraje = int(input("Ingrese el nuevo kilometraje: "))
        mi_auto.actualizar_kilometraje(nuevo_kilometraje)
        print(f"Kilometraje actualizado: {mi_auto.kilometraje} km")
    elif opcion == "3":
        kilometros_viaje = int(input("Ingrese los kilómetros recorridos en el viaje: "))
        mi_auto.realizar_viaje(kilometros_viaje)
        print(f"Kilometraje actualizado: {mi_auto.kilometraje} km")
    elif opcion == "4":
        mi_auto.estado_auto()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
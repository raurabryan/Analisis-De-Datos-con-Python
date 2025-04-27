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
    print("5. Crear auto nuevo Toyota")
    print("6. Crear auto genérico")
    print("7. Comparar kilometraje con otro auto")
    print("8. Verificar si el auto es clásico")
    print("9. Salir")

    opcion = input("Seleccione una opción (1-9): ")

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
        modelo_nuevo = input("Ingrese el modelo del Toyota nuevo: ")
        mi_auto = Auto.auto_nuevo(modelo_nuevo)
        print("Auto nuevo Toyota creado.")
    elif opcion == "6":
        modelo_generico = input("Ingrese el modelo del auto genérico: ")
        año_generico = int(input("Ingrese el año del auto genérico: "))
        mi_auto = Auto.auto_generico(modelo_generico, año_generico)
        print("Auto genérico creado.")
    elif opcion == "7":
        marca2 = input("Ingrese la marca del segundo auto: ")
        modelo2 = input("Ingrese el modelo del segundo auto: ")
        año2 = int(input("Ingrese el año del segundo auto: "))
        segundo_auto = Auto(marca2, modelo2, año2)
        kilometraje2 = int(input("Ingrese el kilometraje del segundo auto: "))
        segundo_auto.actualizar_kilometraje(kilometraje2)
        if Auto.mismo_kilometraje(mi_auto, segundo_auto):
            print("Ambos autos tienen el mismo kilometraje.")
        else:
            print("Los autos tienen diferente kilometraje.")
    elif opcion == "8":
        if Auto.es_clasico(mi_auto.año):
            print("El auto es clásico.")
        else:
            print("El auto NO es clásico.")
    elif opcion == "9":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
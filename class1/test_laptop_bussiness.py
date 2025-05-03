from laptop_Business import Laptop_Business

mi_laptop = Laptop_Business("Dell", "i7", 16, "1TB SSD", "10 horas")

print("\n--- Diagnóstico del Sistema ---")
diagnostico = mi_laptop.realizar_diagnostico_sistema()
for clave, valor in diagnostico.items():
    print(f"{clave}: {valor}")

print("\n--- Verificando conectividad de red ---")
conectividad = mi_laptop.verificar_conectividad_red()
for clave, valor in conectividad.items():
    print(f"{clave}: {'OK' if valor else 'FALLÓ'}")
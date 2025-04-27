valor_alto = float(input("Ingrese el valor del alto: "))
valor_hancho = float(input("Ingrese el valor del ancho: "))

area= valor_alto*valor_hancho
perimetro = 2*(valor_alto+valor_hancho)
superficie = valor_hancho*valor_alto

print(f"El area del rectangulo es: {area}")
print(f"El perimetro del rectangulo es: {perimetro}")
print(f"La superficie del rectangulo es: {superficie}")
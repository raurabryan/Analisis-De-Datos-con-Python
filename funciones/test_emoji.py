import emoji

cantidad_frase = int(input("Cuantas frases desea ingresar: "))
for i in range (cantidad_frase):
    frase = input("Ingresa la frase")
    emoji.encontrar_palabra(frase)
    emoji.agregar_frase(frase)

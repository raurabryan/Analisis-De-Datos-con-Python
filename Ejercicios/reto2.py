import random

velocidad = random.randint(5,130)

print(f"Su velocidad es : {velocidad}")
print("Escoga un Destino:")
print("Para Ecuador digite 1 ")
print("Para Colombia digite 2 ")
print("Para Peru digite 3 ")
pais_destino = int (input("Digite la opcion: "))


if pais_destino == 1 :
    print("En Ecuador en que zona te encuentas: ")
    print("Para Urbana digite 1 ")
    print("Para rural digite 2 ")
    print("Para Perimetral digite 3 ")
    zona = int (input("Digite la opcion: "))
    
    if zona == 1 :
        print("Zona Urbana")
        if velocidad <= 50 and velocidad >= 10 :
            print("Esta dentro de los limites de velocidad")
        else:
            print("Esta fuera de los limites de velocidad ")
    elif zona== 2 :
        print("Zona rural")
        if velocidad <= 70 and velocidad >= 51 :
            print("Esta dentro de los limites de velocidad")
        else:
            print("Esta fuera de los limites de velocidad ")
    elif zona == 3:
        print("Zona perimetral")
        if velocidad <=90 and velocidad >= 91:
            print("Esta dentro de los limites de velocidad")
        else:
            print("Esta fuera de los limites de velocidad ")
    else:
        print("Zona Incorrecta!")
elif pais_destino== 2 :
    print("En Colombia en que zona te encuentas: ")
    print("Para Urbana digite 1 ")
    print("Para rural digite 2 ")
    print("Para Perimetral digite 3 ")
    zona = int (input("Digite la opcion: "))
    
    if zona == 1 :
        print("Zona Urbana")
        if velocidad <= 30 and velocidad >= 10 :
            print("Esta dentro de los limites de velocidad")
        else:
            print("Esta fuera de los limites de velocidad ")
    elif zona== 2 :
        print("Zona rural")
        if velocidad <= 80 and velocidad >= 31 :
            print("Esta dentro de los limites de velocidad")
        else:
            print("Esta fuera de los limites de velocidad ")
    elif zona == 3:
        print("Zona perimetral")
        if velocidad <=100 and velocidad >= 81:
            print("Esta dentro de los limites de velocidad")
        else:
            print("Esta fuera de los limites de velocidad ")
    else:
        print("Zona Incorrecta!")
elif pais_destino == 3:
    print("En Peru en que zona te encuentas: ")
    print("Para Urbana digite 1 ")
    print("Para rural digite 2 ")
    print("Para Perimetral digite 3 ")
    zona = int (input("Digite la opcion: "))
    
    if zona == 1 :
        print("Zona Urbana")
        if velocidad <= 40 and velocidad >= 10 :
            print("Esta dentro de los limites de velocidad")
        else:
            print("Esta fuera de los limites de velocidad ")
    elif zona== 2 :
        print("Zona rural")
        if velocidad <= 60 and velocidad >= 41 :
            print("Esta dentro de los limites de velocidad")
        else:
            print("Esta fuera de los limites de velocidad ")
    elif zona == 3:
        print("Zona perimetral")
        if velocidad <=120 and velocidad >= 61:
            print("Esta dentro de los limites de velocidad")
        else:
            print("Esta fuera de los limites de velocidad ")
    else:
        print("Zona Incorrecta!")
else:
    print("Digito Incorrecto!!!!")
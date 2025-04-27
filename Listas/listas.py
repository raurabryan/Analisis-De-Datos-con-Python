

planetas = ["Mercirio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano","Neptuno"]
# print(planetas[-1])

# print(planetas[1: ])

# print(len(planetas))

# TRABAJAR CON UNA LISTA DE NUMEROS
 
gravedad_en_planetas = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12] 
peso_bus = 124054 #Newtons, en la Tierra

print("En la Tierra, un autobús de dos pisos pesa {peso_bus} N") 
print (f"En Mercurio, un autobús de dos pisos pesa {peso_bus*gravedad_en_planetas[0]} N")

print(f"Lo mas liviano que seria un bus en el suistema solar es:{peso_bus*min(gravedad_en_planetas)}")

print(f"Lo mas pesado que seria un bus en el suistema solar es:{peso_bus*max(gravedad_en_planetas)}")

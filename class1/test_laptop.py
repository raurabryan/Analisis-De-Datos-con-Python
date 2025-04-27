from laptop import Laptop


laptop_pepito= Laptop("lenovo","i7",32)

laptop_maria= Laptop("lenovo","i7",32, 600)


for numero in range (1, 1000):
    
    asus_laptop = Laptop.asus_laptop(numero)
    
    print(asus_laptop.__dict__)
print(Laptop.comparar_costo(laptop_pepito, laptop_maria))


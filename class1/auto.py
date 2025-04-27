class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = 0  

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")

    def actualizar_kilometraje(self, kilometraje):
        if kilometraje >= self.kilometraje:
            self.kilometraje = kilometraje
        else:
            print("No se puede reducir el kilometraje.")

    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
        else:
            print("La cantidad de kilómetros debe ser positiva.")

    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo.")
        elif 20000 <= self.kilometraje <= 100000:
            print("Ya estoy usado.")
        else:
            print("¡Ya déjame descansar por favor!")


    @classmethod
    def auto_nuevo(cls, modelo):
        año_actual = 2025
        return cls("Toyota", modelo, año_actual)

    @staticmethod
    def mismo_kilometraje(auto1, auto2):
        return auto1.kilometraje == auto2.kilometraje

    @classmethod
    def auto_generico(cls, modelo, año):
        return cls("Sin Marca", modelo, año)

    @staticmethod
    def es_clasico(año):
        año_actual = 2025
        return (año_actual - año) > 30
    
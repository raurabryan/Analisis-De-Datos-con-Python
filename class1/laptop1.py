import random

class Laptop:
    def __init__(self, marca, procesador, memoria, costo=500, impuesto=10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuesto

    def valor_final(self):
        return self.costo + self.impuesto

    def valor_descuento(self, descuento):
        return (self.costo * descuento) / 100

    def realizar_diagnostico_sistema(self):
        return {
            "CPU": "OK",
            "RAM": "OK",
            "Disco": "OK"
        }
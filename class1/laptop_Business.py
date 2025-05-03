from laptop1 import Laptop
import random

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria

    def realizar_diagnostico_sistema(self):
        diagnostico_base = super().realizar_diagnostico_sistema()
        diagnostico_base.update({
            "Conectividad Wi-Fi": "Verificado",
            "VPN Empresarial": "Disponible",
            "Seguridad TPM": "Activa"
        })
        return diagnostico_base

    def verificar_conectividad_red(self):
        return {
            "wifi_disponible": random.choice([True, False]),
            "acceso_servidores": random.choice([True, False]),
            "latencia_aceptable": random.choice([True, False])
        }
    

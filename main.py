from abc import ABC, abstractmethod

# 1. Creamos una abstracción para los métodos de pago
class MetodoPago(ABC):
    @abstractmethod
    def procesar(self, monto):
        """Procesa un pago por el monto indicado"""
        pass

# 2. Implementamos los métodos de pago concretos
class PagoTarjeta(MetodoPago):
    def procesar(self, monto):
        # Lógica específica para procesar pago con tarjeta
        print(f"Validando tarjeta...")
        print(f"Procesando cargo de ${monto} a la tarjeta de crédito")
        return True  # En un caso real, retornaría true solo si la transacción fue exitosa

class PagoPayPal(MetodoPago):
    def procesar(self, monto):
        # Lógica específica para procesar pago con PayPal
        print(f"Redirigiendo a PayPal...")
        print(f"Procesando ${monto} a través de PayPal")
        return True  # En un caso real, retornaría true solo si la transacción fue exitosa

# 3. Procesador de pagos que depende de la abstracción, no de implementaciones concretas
class ProcesadorPago:
    def __init__(self, metodo_pago: MetodoPago):
        # Inyección de dependencia: recibimos el método como parámetro
        self.metodo_pago = metodo_pago
    
    def realizar_pago(self, monto):
        # Delegamos la implementación al método inyectado
        resultado = self.metodo_pago.procesar(monto)
        
        if resultado:
            print(f"Pago de ${monto} completado exitosamente")
            return True
        else:
            print(f"Error al procesar el pago de ${monto}")
            return False

# Crear instancias de los métodos de pago
pago_tarjeta = PagoTarjeta()
pago_paypal = PagoPayPal()

# Crear un procesador con pago por tarjeta
procesador = ProcesadorPago(pago_tarjeta)

# Procesar un pago
procesador.realizar_pago(100.50)  # Utilizará tarjeta

# Cambiar el método de pago a PayPal
procesador = ProcesadorPago(pago_paypal)

# Procesar otro pago
procesador.realizar_pago(75.25)  # Utilizará PayPal
# ==========================================
# Programa que demuestra POO en Python
# Clases, Herencia, Encapsulación y Polimorfismo
# ==========================================

# Clase base
class DispositivoElectronico:
    def __init__(self, marca, modelo):
        # Encapsulación: atributo privado
        self.__marca = marca
        self.modelo = modelo

    # Método getter para acceder al atributo privado
    def get_marca(self):
        return self.__marca

    # Método común que será sobrescrito (polimorfismo)
    def encender(self):
        print("El dispositivo electrónico se está encendiendo.")


# Clase derivada (Herencia)
class Telefono(DispositivoElectronico):
    def __init__(self, marca, modelo, numero):
        super().__init__(marca, modelo)
        self.numero = numero

    # Polimorfismo: sobrescritura del método
    def encender(self):
        print(f"El teléfono {self.get_marca()} modelo {self.modelo} se está encendiendo.")


# Otra clase derivada
class Computadora(DispositivoElectronico):
    def __init__(self, marca, modelo, sistema_operativo):
        super().__init__(marca, modelo)
        self.sistema_operativo = sistema_operativo

    # Polimorfismo: sobrescritura del método
    def encender(self):
        print(f"La computadora {self.get_marca()} con {self.sistema_operativo} se está iniciando.")


# ==========================
# Creación de objetos
# ==========================
telefono1 = Telefono("Samsung", "Galaxy S23", "0987654321")
computadora1 = Computadora("HP", "Pavilion", "Windows 11")

# Uso de métodos
telefono1.encender()
computadora1.encender()

class Fabrica:
    def __init__(self, llantas, color, precio, descuento_minimo=100000, descuento_porcentaje=0.1):
        self.llantas = llantas
        self.color = color
        self.precio = precio
        self.descuento_minimo = descuento_minimo
        self.descuento_porcentaje = descuento_porcentaje

    def mostrar_datos(self):
        print(f"Este vehículo tiene {self.llantas} llantas, es de color {self.color} y cuesta ${self.precio}.")

    def aplicar_descuento(self):
        if self.precio > self.descuento_minimo:
            self.precio *= (1 - self.descuento_porcentaje)
            print("Se ha aplicado un descuento.")

class Auto(Fabrica):
    def __init__(self, llantas, color, precio, marca, puertas):
        super().__init__(llantas, color, precio)
        self.marca = marca
        self.puertas = puertas

class Moto(Fabrica):
    def __init__(self, llantas, color, precio, cilindrada):
        super().__init__(llantas, color, precio)
        self.cilindrada = cilindrada

class Camion(Fabrica):
    def __init__(self, llantas, color, precio, capacidad_carga, tipo_motor):
        super().__init__(llantas, color, precio)
        self.capacidad_carga = capacidad_carga
        self.tipo_motor = tipo_motor

    def cargar(self, peso):
        if peso <= self.capacidad_carga:
            print("Carga exitosa.")
        else:
            print("Carga excedida.")

# Creación de objetos
mi_auto = Auto(4, "rojo", 20000, "BMW", 4)
mi_moto = Moto(2, "negro", 120000, 600)
mi_camion = Camion(6, "blanco", 150000, 5000, "diesel")

# Mostrar datos iniciales
mi_auto.mostrar_datos()
mi_moto.mostrar_datos()
mi_camion.mostrar_datos()

# Aplicar descuento a la moto y mostrar los datos actualizados
mi_moto.aplicar_descuento()
mi_moto.mostrar_datos()

# Cargar el camión
mi_camion.cargar(4000)
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad 

class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        self.titular = titular
        self.__cantidad = cantidad

    # Getter para la cantidad
    def get_cantidad(self):
        return self.__cantidad

    # Setter para la cantidad
    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            print("La cantidad no puede ser negativa.")

    def mostrar(self):
        if self.titular is not None:
            print(f"Titular: {self.titular.nombre} {self.titular.apellido}")
        print(f"Saldo: ${self.__cantidad:.2f}") 

    def ingresar(self, cantidad):
        if cantidad >= 0:
            self.__cantidad += cantidad
        else:
            print("No puedes ingresar una cantidad negativa.")

    def retirar(self, cantidad):
        self.__cantidad -= cantidad


titular_nombre = input("Ingrese su nombre:")
titular_apellido = input("Ingrese su apellido:")
titular_edad = input("Ingresar su edad:")

# Crear un objeto de la clase Persona para el titular
titular = Persona(titular_nombre, titular_apellido, titular_edad)

# Crear una cuenta con el titular
c1 = Cuenta(titular)

# Mostrar información de la cuenta
c1.mostrar()

# Ingresar dinero en la cuenta
ingresar_cantidad = float(input("Ingrese la cantidad que desea ingresar:"))
c1.ingresar(ingresar_cantidad)

# Retirar dinero de la cuenta
retirar_cantidad = float(input("Ingrese la cantidad que desea retirar:"))
c1.retirar(retirar_cantidad)


c1.mostrar()



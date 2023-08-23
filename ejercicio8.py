class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.__cantidad = cantidad

    def mostrar(self):
        mensaje = "Cuenta\n"
        print(mensaje)

    def ingreso(self, cantidad):
        if cantidad >= 0:
            self.__cantidad += cantidad
        else:
            print("No puedes ingresar una cantidad negativa.")

    def retiro(self, cantidad):
        if self.titular is not None and self.titular.edad >= 18 and self.titular.edad < 25:
            if cantidad <= self.__cantidad:
                self.__cantidad -= cantidad
            else:
                print("No tienes suficiente saldo.")
        else:
            print("No puedes retirar dinero, el titular no es válido.")


class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def es_titular_valido(self):
        if self.edad >= 18 and self.edad < 25:
            return True
        return False


class CuentaJoven(Cuenta):
    def __init__(self, titular, bonificacion, cantidad=0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    def mostrar(self):
        mensaje = "Cuenta Joven\n"
        print(f"Bonificación: {self.__bonificacion}%")
        print(mensaje)


titular_nombre = input("Ingrese su nombre:")
titular_apellido = input("Ingrese su apellido:")
titular_edad = int(input("Ingresar su edad:"))
bonificacion = float(input("Ingresar la bonificación: "))

titular = Persona(titular_nombre, titular_apellido, titular_edad)
cuenta_joven = CuentaJoven(titular, bonificacion)
cuenta_joven.mostrar()

ingresar_cantidad = float(input("Ingresar la cantidad que desea ingresar: "))
cuenta_joven.ingreso(ingresar_cantidad)

if cuenta_joven.titular.es_titular_valido():
    retirar_cantidad = float(input("Ingresar la cantidad que desee retirar: "))
    cuenta_joven.retiro(retirar_cantidad)
else:
    print("Operación de retiro no permitida")

cuenta_joven.mostrar()
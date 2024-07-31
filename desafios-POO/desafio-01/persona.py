class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    # Getters
    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    def get_dni(self):
        return self._dni

    # Setters con validación
    def set_nombre(self, nombre):
        if isinstance(nombre, str) and nombre:
            self._nombre = nombre
        else:
            print("Nombre no válido")

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self._edad = edad
        else:
            print("Edad no válida")

    def set_dni(self, dni):
        if isinstance(dni, str) and dni:
            self._dni = dni
        else:
            print("DNI no válido")

    # Método para mostrar los datos de la persona
    def mostrar(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}, DNI: {self._dni}")

    # Método para verificar si es mayor de edad
    def es_mayor_de_edad(self):
        return self._edad >= 18


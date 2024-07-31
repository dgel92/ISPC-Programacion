from persona import Persona


def main():
    # Crear una instancia de Persona
    persona = Persona()

    # Obtener datos del usuario
    nombre = input("Introduce el nombre: ")
    edad = input("Introduce la edad: ")
    dni = input("Introduce el DNI: ")

    # Validar y establecer los datos
    persona.set_nombre(nombre)
    try:
        persona.set_edad(int(edad))
    except ValueError:
        print("Edad no válida. Debe ser un número entero.")
        return
    persona.set_dni(dni)

    # Mostrar los datos de la persona
    persona.mostrar()

    # Evaluar si es mayor de edad
    if persona.es_mayor_de_edad():
        print(f"{persona.get_nombre()} es mayor de edad.")
    else:
        print(f"{persona.get_nombre()} es menor de edad.")


if __name__ == "__main__":
    main()

# practica nro 1

# Realice un programa que solicite dos letras ingresadas por el usuario y verifique si son iguales o no, mostrando un mensaje
def comprobar_letras():
    letra_1 = input("Por favor ingresa una letra: ")
    if len(letra_1) == 1:
        letra_2 = input("Por favor ingresa la segunda letra: ")
        if len(letra_2) == 1:
            if len(letra_2) == len(letra_1):
                if letra_1 != letra_2:
                    print("¡Bienvenido!")
                else:
                    print("Las letras no pueden ser iguales")
            else:
                print("En la letra 02 puede ser un solo caracter")
        else:
            print("Por favor ingresa una sola letra para la segunda letra.")
    else:
        print("Por favor ingresa una sola letra para la primera letra.")
    # llamar a la funcion
    comprobar_letras()


#Hacer un programa que permita decidir si dos palabras son iguales o diferentes. Mostrar mensaje por pantalla.
def comprobar_palabras():
    palabra_1= input("porfavor ingresa una palabra")
    palabra_2= input("porfavor ingresa una segunda palabra")
    if palabra_1 == palabra_2:
        print("las palabras son iguales")
    else:
        print("las palabras son distintas")
    # llamar a la funcion
    comprobar_palabras()


#Realizar un programa que permita ingresar “f” o “m” y determinar si vota en mesa femenina o masculina.
def comprobar_genero():
    nombre: input("porfavor ingresa tu nombre")
    apellido: input("porfavor ingresa tu apellido")
    while True:
        genero = input("Por favor selecciona tu género (femenino/masculino/prefiero no elegir): ")
        if genero.lower() == "femenino":
            print("Por favor usa la mesa número 1.")
            break
        elif genero.lower() == "masculino":
            print("Por favor usa la mesa número 2.")
            break
        elif genero.lower() == "prefiero no elegir":
            print("Puedes elegir la mesa de votación que te resulte acorde a tu género.")
            break
        else:
            print("Por favor selecciona una opción válida.")

# llamar a la funcion
#comprobar_genero()


#Realice un programa que lea dos números y diga cuál es el mayor.
def mayor_o_menor():
    nro_1 = int(input("Por favor selecciona un número: "))
    nro_2 = int(input("Por favor selecciona otro número: "))

    if nro_1 > nro_2:
        print("El primer número es mayor.")
    elif nro_1 < nro_2:
        print("El segundo número es mayor.")
    else:
        print("Los números son iguales.")
    # Llamar a la función
    mayor_o_menor()


#Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y que sea el usuario quién decida qué tipo de cambio quiere, si de dólares a pesos o viceversa.

def cambio():
    dolar = 990  # Definir el valor del dólar
    cantidad_dolar = 0
    while True:
        opcion = input("Por favor elige qué tipo de cambio quieres hacer:\nPeso a dólar (A)\nDólar a peso (B)\n Terminar (C)\n").lower()
        if opcion == "a":
            cantidad = int(input("Indica cuántos pesos quieres cambiar a dólar: "))
            cantidad_dolar = cantidad / dolar
            print(f"Obtendrás {cantidad_dolar} dólares.")
        elif opcion == "b":
            cantidad = int(input("Indica cuántos dólares quieres cambiar a pesos: "))
            cantidad_pesos = cantidad * dolar
            print(f"Obtendrás {cantidad_pesos} pesos argentinos.")
        elif opcion == "c":
            print("Finalizar.")
            break

# Llamar a la función
#cambio()


#Realice un programa donde el usuario ingrese su edad. Si es mayor de 16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.
def votacion():
    age= int(input("porfavor coloca tu edad: "))
    if age > 16:
        print("podes votar")
    else: print("no tenes la edad necesaria")

    # Llamar a la función

#votacion()


#1. Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es equilátero, isósceles o escaleno.

def triangulo():
    a = float(input("Ingresa la longitud del primer lado del triángulo: "))
    b = float(input("Ingresa la longitud del segundo lado del triángulo: "))
    c = float(input("Ingresa la longitud del tercer lado del triángulo: "))
    if a == b == c:
        print("Es un triangulo equilatero")
    elif a == b or b == c or a == c:
        print("es un triangulo isoceles")
    else:
        print ("es un triangulo escaleno")
 # Llamar a la función

#triangulo()


#2. Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago:

def modulo_de_pago():
    contado_o_tarjeta = 10 / 100  # 10% de descuento
    debito = 5 / 100  # 5% de descuento
    monto_a_pagar = int(input("Por favor selecciona el monto a pagar: "))
    forma_de_pago = input(
        "Por favor elige la forma de pago que deseas:\nContado (A)\nTarjeta (B)\nDebito (C)\n").lower()

    if forma_de_pago == "a":
        total_descuento = monto_a_pagar * contado_o_tarjeta
        total_a_pagar = monto_a_pagar - total_descuento
        print(f"El importe del producto es {monto_a_pagar}")
        print(f"Vas a pagar de contado, tu descuento es {total_descuento}, que equivale al 10%")
        print(f"Total a pagar final {total_a_pagar}")
    elif forma_de_pago == "b":
        total_descuento = monto_a_pagar * contado_o_tarjeta
        total_a_pagar = monto_a_pagar - total_descuento
        print(f"El importe del producto es {monto_a_pagar}")
        print(f"Vas a pagar con tarjeta, tu descuento es {total_descuento}, que equivale al 10%")
        print(f"Total a pagar final {total_a_pagar}")
    elif forma_de_pago == "c":
        total_descuento = monto_a_pagar * debito
        total_a_pagar = monto_a_pagar - total_descuento
        print(f"El importe del producto es {monto_a_pagar}")
        print(f"Vas a pagar con débito, tu descuento es {total_descuento}, que equivale al 5%")
        print(f"Total a pagar final {total_a_pagar}")
    else:
        print("Por favor selecciona una opción válida.")
        modulo_de_pago()

#Llamar a la función

#modulo_de_pago()


#3. Realice un programa que lea tres números, muestre cuál es el mayor y determine si es par o impar.
def numero_mayor():
    variables= []
    for _ in range(3):
        variable = int(input("agrega los numeros a comparar"))
        variables.append(variable)
    if variables:
        mayor = max(variables)
        print(f"el numero mas grande es: {mayor}")
        if maximo % 2 == 0:
            print("el numero es par")
        else:
            print ("el numero es impar")
#llamar a la funcion
#numero_mayor()


#4. Confeccione un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente.

#5. Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente.

def dias_de_la_semana():
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    while True:
        numero = int(input("Selecciona un número del 1 al 7: "))
        if numero > 7:
            print("Por favor selecciona un número correcto.")
        else:
            break
    dia_seleccionado = dias[numero - 1]
    print("El día seleccionado es:", dia_seleccionado)

# Llamar a la función
# dias_de_la_semana()


def meses_del_año():
    dias = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    while True:
        numero = int(input("Selecciona un número del 1 al 12: "))
        if numero > 12:
            print("Por favor selecciona un número permitido.")
        else:
            break
    mes_seleccionado = dias[numero - 1]
    print("El mes seleccionado es:", mes_seleccionado)

# Llamar a la función
#meses_del_año()


#1. Realice un programa que lea 4 números y diga cuántos son pares y cuantos impares y devuelva la sumatoria de los pares.

def pares():
    pares = []
    suma_pares = 0
    print("Por favor selecciona cuatro números:")
    for _ in range(4):
        numero = int(input())
        pares.append(numero)
        if numero % 2 == 0:
            print(numero, "es par")
            suma_pares += numero
    return suma_pares

#suma_de_pares = pares()
#print("La suma de los números pares es:", suma_de_pares)

#Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo.

def numeros():
    variables = []
    for _ in range(10):
        numero = int(input("Selecciona 10 números: "))
        variables.append(numero)
        if numero < 100:
            print("Este número es menor a 100:", numero)
    maximo = max(variables)
    minimo = min(variables)
    print("El número máximo es:", maximo)
    print("El número mínimo es:", minimo)

#numeros()




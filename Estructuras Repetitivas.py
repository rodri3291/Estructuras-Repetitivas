# Ejercicio 1
for i in range(0, 100):
    print(i, "Debo aprender ciclos")
print("Terminé de aprender ciclos")


# Ejercicio 2
print("////////////////")
for i in range(5):
    print(i, "Debo aprender ciclos")
print("Terminé de aprender ciclos")
print("////////////////")


# Ejercicio 3
num1_str = input("Ingrese el primer número: ")
num2_str = input("Ingrese el segundo número: ")
num1 = int(num1_str)
num2 = int(num2_str)
if num1 > num2:
    num1, num2 = num2, num1
suma_total = sum(range(num1 + 1, num2))
print(f"La suma de los números entre {num1} y {num2} es: {suma_total}")


# Ejercicio 4
total_suma = 0
print("Ingrese números enteros. Ingresa '0' para terminar y ver el total.")
while True:
    try:
        numero_ingresado = int(input("Ingrese un número: "))
        if numero_ingresado == 0:
            break
        total_suma += numero_ingresado
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        print("Error: Por favor, ingresa solo números enteros.")
print(f"El total acumulado de los números ingresados es: {total_suma}")


# Ejercicio 5
import random
def juego_adivina_el_numero():
    numero_secreto = random.randint(0, 9)
    intentos = 5
    adivinado = False
    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 0 y 9.")
    while not adivinado:
        if intentos == 0:
            print(f"Lo siento, has agotado tus intentos. El número era {numero_secreto}.")
            break
        try:
            intento = int(input(f"Tienes {intentos} intentos restantes. ¿Cuál es tu suposición? "))
            if intento < 0 or intento > 9:
                print("Por favor, ingresa un número entre 0 y 9.")
                continue
            if intento == numero_secreto:
                print("¡Felicidades! ¡Has adivinado el número!")
                adivinado = True
            else:
                intentos -=  1
                if intento < numero_secreto:
                    print("El número es mayor.")
                else:
                    print("El número es menor.")
        except: ValueError
        print("Por favor, ingresa un número entero válido.")
juego_adivina_el_numero()


# Ejercicio 6
for i in range(100, 0, -1):
    print(i,"Lista de números del 100 al 1")
print("¡Terminé!")


# Ejercicio 7
numero = int(input("Ingrese un número: "))
if numero < 0:
    numero = numero * (-1)
c = 0    
for i in range(0, numero + 1):
    if i % 3 == 0:
        print(f"El numero {i} es múltiplo de 3")
        c += 1
    else:
        print(i)
print(f"Numero multiplos de 3: {c}")

    
# Ejercicio 8
def contar_numeros():
    cantidad_numeros = 100
    numeros_positivos = 0
    numeros_negativos = 0
    numeros_pares = 0
    numeros_impares = 0 
    print(f"Ingrese {cantidad_numeros} números:")
    for i in range(cantidad_numeros):
        while True:
            try:
                num_str = input(f"Número {i + 1}: ")
                numero = int(num_str)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
                if numero % 2 == 0:
                    numeros_pares += 1
                else:
                    numeros_impares += 1
                if numero > 0:
                        numeros_positivos += 1
                elif numero <0:
                        numeros_negativos += 1
    print(f"Números positivos: {numeros_positivos}")
    print(f"Números negativos: {numeros_negativos}")
    print(f"Números pares: {numeros_pares}")
    print(f"Números impares: {numeros_impares}")
contar_numeros()


# Ejercicio 9
def calcular_media_numeros():
    cantidad_numeros = 10
    suma_total = 0
    print(f"Ingrese {cantidad_numeros} números:")
    for i in range(cantidad_numeros):
        while True:
            try:
                num1_str = input(f"Número {i + 1}: ")
                numero = float(num1_str)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número válido.")
                suma_total += numero
                media = suma_total / cantidad_numeros
                print(f"La suma total de los números ingresados es: {suma_total}")
                print(f"La media de los números ingresados es: {media}")
                

# Ejercicio 10
numero = input("Ingrese un número: ")
if numero.isdigit():
    numero = int(numero)
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
        print(f"El factorial de {numero} es: {factorial}")
    else:
        print("Por favor, ingrese un número entero válido.")                      
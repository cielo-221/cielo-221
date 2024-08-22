# Definir un diccionario con los precios de las frutas
precios_frutas = {
    "manzana": 3.0,  # Precio por kilo
    "banana": 2.5,
    "naranja": 4.0,
    "fresa": 5.0
}

# Solicitar al usuario que ingrese el nombre de la fruta
fruta = input("Ingrese el nombre de la fruta: ").lower()

# Solicitar al usuario que ingrese la cantidad en kilos
try:
    kilos = float(input("Ingrese el número de kilos: "))
    if kilos < 0:
        raise ValueError("El número de kilos debe ser positivo.")
except ValueError as e:
    print(f"Error: {e}")
else:
    # Verificar si la fruta está en el diccionario
    if fruta in precios_frutas:
        # Calcular el precio total
        precio_total = precios_frutas[fruta] * kilos
        print(f"El precio de {kilos} kilos de {fruta} es ${precio_total:.2f}")
    else:
        # Mostrar mensaje si la fruta no está en el diccionario
        print("La fruta no está en el diccionario.")

def contar_digitos(texto):
    """Cuenta cuántos dígitos numéricos (del 0 al 9) hay en el texto dado."""
    return sum(c.isdigit() for c in texto)

def main():
    lineas_completas = 0
    while True:
        lineas_texto = ""
        while True:
            entrada = input("Ingrese un título de libro o '/' para terminar la línea ( '*' para finalizar): ")
            
            if entrada == '*':
                # Terminamos el ingreso de datos
                break
            
            if entrada == '/':
                # Contamos los dígitos en la línea completa
                digitos = contar_digitos(lineas_texto)
                print(f"Dígitos en la línea: {digitos}")
                lineas_completas += 1
                lineas_texto = ""  # Reiniciamos el texto para la próxima línea
            else:
                # Agregamos el título al texto de la línea actual
                lineas_texto += entrada

        # Informamos el número total de líneas completas ingresadas
        print(f"\nNúmero total de líneas completas: {lineas_completas}")

if __name__ == "__main__":
    main()

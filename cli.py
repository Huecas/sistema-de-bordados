from prendas_google import agregar_registro, leer_datos

SHEET_ID = "TU_ID_AQUI"
NOMBRE_HOJA = "Hoja 1"

def menu():
    print("=== SISTEMA DE BORDADOS CLI ===")
    print("1. Ver prendas")
    print("2. Agregar prenda")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        df = leer_datos(SHEET_ID, NOMBRE_HOJA)
        print(df)
    elif opcion == "2":
        nombre = input("Nombre del cliente: ")
        tipo = input("Tipo de prenda: ")
        color = input("Color: ")
        fecha = input("Fecha (AAAA-MM-DD): ")
        agregar_registro(SHEET_ID, NOMBRE_HOJA, [nombre, tipo, color, fecha])

if __name__ == "__main__":
    menu()

# cli.py
from prendas_google import guardar_registro
from datetime import datetime

def input_nonempty(prompt):
    v = input(prompt).strip()
    return v

def run():
    print("== Nuevo registro de Bata ==")
    datos = {}
    datos["VENDEDOR"] = input_nonempty("VENDEDOR: ")
    datos["CLIENTE"] = input_nonempty("NOMBRE DE CLIENTE: ")
    datos["TELÉFONO"] = input_nonempty("NUMERO TELEFONICO: ")
    datos["PRENDA"] = input_nonempty("PRENDA: ")
    datos["COLOR"] = input_nonempty("COLOR (ej. Blanca, Guinda): ")
    datos["TALLA"] = input_nonempty("TALLA (28-30-...-46): ")
    datos["BORDADOS"] = input_nonempty("BORDADOS (ej. ESIME + ESCOM): ")
    datos["A_CUENTA"] = input_nonempty("A CUENTA (monto): ")
    datos["RESTAN"] = input_nonempty("RESTAN (monto): ")
    datos["TOTAL"] = input_nonempty("TOTAL (monto): ")
    datos["FECHA_ENTREGA"] = input_nonempty("FECHA DE ENTREGA (dd/mm/yyyy): ")
    datos["PUNTO_ENTREGA"] = input_nonempty("PUNTO DE ENTREGA: ")
    datos["TIPO"] = input_nonempty("TIPO (Venta / Pedido): ")

    guardar_registro(datos)

if __name__ == "__main__":
    run()

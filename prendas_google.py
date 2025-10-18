import gspread
from google.oauth2.service_account import Credentials
import streamlit as st

# Alcances (permisos) de Google Sheets y Drive
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Cargar credenciales desde archivo JSON local
try:
    credentials = Credentials.from_service_account_file("credenciales.json", scopes=SCOPES)
    client = gspread.authorize(credentials)
    st.write("✅ Conectado correctamente a Google Sheets")
except Exception as e:
    st.error(f"❌ Error al conectar con Google Sheets: {e}")

# Abre el archivo de Google Sheets
try:
    spreadsheet = client.open("Sistema_Bordados")
except Exception as e:
    st.error(f"❌ Error al abrir el archivo de Google Sheets: {e}")

def guardar_registro(data: dict):
    try:
        # Determinar hoja según vendedor y tipo
        vendedor = data.get("vendedor", "").strip()
        tipo = data.get("tipo", "").strip().capitalize()  # "Venta" o "Pedidos"

        if not vendedor or not tipo:
            raise ValueError("Falta el nombre del vendedor o el tipo (Venta/Pedidos).")

        hoja = f"{vendedor}_{tipo}"  # Ejemplo: Jabe_Pedidos, Danilo_Ventas, etc.

        st.write(f"Guardando en hoja: {hoja}")

        # Abre la hoja correspondiente
        sheet = spreadsheet.worksheet(hoja)

        # Datos a guardar
        valores = [
            vendedor,
            data.get("nombre_cliente", ""),
            data.get("telefono", ""),
            data.get("prenda", ""),
            data.get("color", ""),
            data.get("talla", ""),
            data.get("corte", ""),
            data.get("bordado", ""),
            data.get("a_cuenta", ""),
            data.get("restan", ""),
            data.get("total", ""),
            data.get("fecha_entrega", ""),
            data.get("punto_entrega", ""),
            tipo
        ]

        # ✅ Corrección: se inserta siempre desde la columna A
        next_row = len(sheet.get_all_values()) + 1
        sheet.update(f"A{next_row}:N{next_row}", [valores])

        st.success(f"✅ Registro guardado correctamente en {hoja}.")
        return True

    except gspread.exceptions.WorksheetNotFound:
        st.error(f"❌ La hoja '{hoja}' no existe en el archivo de Google Sheets.")
        return False

    except Exception as e:
        st.error(f"❌ Error al guardar: {e}")
        return False


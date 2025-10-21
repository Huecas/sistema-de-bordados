import gspread
import streamlit as st
import json
from google.oauth2.service_account import Credentials

# Alcances (permisos) de Google Sheets y Drive
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Inicializamos las variables globales
client = None
spreadsheet = None

# --- CONEXIÓN SEGURA A GOOGLE SHEETS ---
try:
    credenciales_dict = json.loads(st.secrets["general"]["google_service_account"])
    credentials = Credentials.from_service_account_info(credenciales_dict, scopes=SCOPES)
    client = gspread.authorize(credentials)
    spreadsheet = client.open("Sistema_Bordados")
    st.write("✅ Conectado correctamente a Google Sheets (modo seguro)")
except Exception as e:
    st.error(f"❌ Error al conectar o abrir Google Sheets: {e}")

# --- FUNCIÓN PARA GUARDAR REGISTRO ---
def guardar_registro(data: dict):
    if spreadsheet is None:
        st.error("❌ No se ha podido conectar con Google Sheets. Revisa las credenciales o los secrets.")
        return False

    try:
        vendedor = data.get("vendedor", "").strip()
        tipo = data.get("tipo", "").strip().capitalize()  # "Venta" o "Pedidos"

        if not vendedor or not tipo:
            raise ValueError("Falta el nombre del vendedor o el tipo (Venta/Pedidos).")

        hoja = f"{vendedor}_{tipo}"  # Ejemplo: Jabe_Pedidos
        st.write(f"Guardando en hoja: {hoja}")

        sheet = spreadsheet.worksheet(hoja)

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

        # Buscar la siguiente fila vacía
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




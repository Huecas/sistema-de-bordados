# prendas_google.py
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Cargar credenciales desde los Secrets de Streamlit
creds = Credentials.from_service_account_info(
    st.secrets["google_credentials"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
)

# Conectar con Google Sheets
gc = gspread.authorize(creds)
sh = gc.open("pedidos_y_ventas")

# Obtener las hojas por nombre
pedidos_ws = sh.worksheet("Hoja 1")   # hoja para PEDIDOS
ventas_ws  = sh.worksheet("Hoja 2")   # hoja para VENTAS

# Función para guardar registro
def guardar_registro(datos):
    fila = [
        datos.get("VENDEDOR",""),
        datos.get("CLIENTE",""),
        datos.get("TELÉFONO",""),
        datos.get("PRENDA",""),
        datos.get("MARCA",""),
        datos.get("CORTE",""),
        datos.get("COLOR",""),
        datos.get("TALLA",""),
        datos.get("BORDADOS",""),
        datos.get("A_CUENTA",""),
        datos.get("RESTAN",""),
        datos.get("TOTAL",""),
        datos.get("FECHA_ENTREGA",""),
        datos.get("PUNTO_ENTREGA",""),
        datos.get("TIPO","")
    ]

    tipo = (datos.get("TIPO","")).strip().lower()
    if tipo == "venta":
        ventas_ws.append_row(fila, value_input_option="USER_ENTERED")
    else:
        pedidos_ws.append_row(fila, value_input_option="USER_ENTERED")



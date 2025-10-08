# prendas_google.py
import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
SERVICE_ACCOUNT_FILE = "credenciales.json"   # asegúrate que esté en la misma carpeta
DOC_NAME = "pedidos_y_ventas"                # nombre exacto del documento en Drive

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
gc = gspread.authorize(creds)
sh = gc.open(DOC_NAME)

# Obtener las hojas por nombre (asegúrate de tenerlas creadas)
pedidos_ws = sh.worksheet("Hoja 1")   # hoja para PEDIDOS
ventas_ws  = sh.worksheet("Hoja 2")    # hoja para VENTAS

def guardar_registro(datos):
    # fila con el orden exacto de las columnas del sheet
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


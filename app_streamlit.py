# app_streamlit.py
import streamlit as st
from prendas_google import guardar_registro

st.set_page_config(page_title="Sistema Bordados", layout="wide")
st.title("🧵 Registro de Batas / Prendas - Pedidos y Ventas")

# Datos básicos
vendedor = st.text_input("Vendedor")
cliente = st.text_input("Nombre del cliente")
telefono = st.text_input("Teléfono (sin espacios)")

# Tipo (decide hoja destino)
tipo = st.selectbox("Tipo (separador hoja):", ["Pedido", "Venta"])

# Prenda y opciones dinámicas
prenda = st.selectbox("Prenda:", ["Bata", "Playera", "Sudadera", "Gorra", "Otra"])

if prenda == "Bata":
    talla = st.selectbox("Talla:", ["28","30","32","34","36","38","40","42","44","46"])
    color = st.selectbox("Color:", ["Guinda", "Blanca", "Marino"])
    # Para batas dejamos marca por si la quieres (default Yasbek)
    marca = st.selectbox("Marca:", ["Yasbek", "Otra"], index=0)
    corte = st.selectbox("Corte:", ["Unisex", "Dama", "Caballero", "N/A"], index=0)
else:
    talla = st.selectbox("Talla:", ["Extra Chica","Chica","Mediana","Grande","XL","XXL"])
    color = st.selectbox("Color:", ["Blanca","Guinda","Marino","Negra","Gris","Otra"])
    marca = st.selectbox("Marca:", ["Yasbek","Otra"], index=0)
    corte = st.selectbox("Corte de prenda:", ["Dama","Caballero","Unisex","N/A"])

bordados = st.text_area("Bordados (ej. ESIME + ESCOM, o Diseños personalizados)")
a_cuenta = st.text_input("A cuenta (monto)")
restan = st.text_input("Restan (monto)")
total = st.text_input("Total (monto)")
fecha_entrega = st.date_input("Fecha de entrega")
punto_entrega = st.text_input("Punto de entrega (lugar)")

# Botón guardar
if st.button("Guardar registro"):
    # validaciones básicas
    if not cliente or not telefono:
        st.warning("Completa al menos Cliente y Teléfono.")
    else:
        datos = {
            "VENDEDOR": vendedor.strip(),
            "CLIENTE": cliente.strip(),
            "TELÉFONO": telefono.strip(),
            "PRENDA": prenda,
            "MARCA": marca,
            "CORTE": corte,
            "COLOR": color,
            "TALLA": talla,
            "BORDADOS": bordados.strip(),
            "A_CUENTA": a_cuenta.strip(),
            "RESTAN": restan.strip(),
            "TOTAL": total.strip(),
            "FECHA_ENTREGA": fecha_entrega.strftime("%d/%m/%Y"),
            "PUNTO_ENTREGA": punto_entrega.strip(),
            "TIPO": tipo
        }

        try:
            guardar_registro(datos)
            st.success(f" {tipo} guardado: {cliente} — {prenda} talla {talla}")
            # mostramos un resumen
            st.markdown("**Resumen guardado:**")
            st.write({
                "Cliente": datos["CLIENTE"],
                "Prenda": datos["PRENDA"],
                "Marca": datos["MARCA"],
                "Corte": datos["CORTE"],
                "Talla": datos["TALLA"],
                "Color": datos["COLOR"],
                "Total": datos["TOTAL"]
            })
        except Exception as e:
            st.error(f"Error al guardar: {e}")


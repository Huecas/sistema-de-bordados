import streamlit as st
from prendas_google import guardar_registro

st.set_page_config(page_title="Sistema de Bordados YASVEK", page_icon="🧵", layout="centered")

st.title("🧵 Sistema de Bordados YASVEK")
st.markdown("Rellena los datos del pedido o venta según corresponda.")

# --- SECCIÓN DE VENDEDOR ---
vendedor = st.selectbox("👤 Vendedor:", ["Jabe", "Danilo", "Trabajador"])

# --- FORMULARIO DE DATOS ---
nombre_cliente = st.text_input("🪪 Nombre del Cliente:")
telefono = st.text_input("📞 Número Telefónico:")

# --- PRENDA ---
prenda = st.selectbox(
    "👕 Tipo de prenda:",
    [
        "Bata",
        "Chaleco",
        "Sudadera con gorro",
        "Sudadera sin gorro",
        "Sudadera con cierre y gorro",
        "Camisa de vestir 100% algodón con mangas",
        "Camisa de vestir 100% algodón sin mangas",
        "Camisola de mezclilla con mangas",
        "Camisola de mezclilla sin mangas",
        "Polo pique",
        "Playera 100% algodón con mangas",
        "Playera 100% algodón sin mangas",
        "Playera licra con mangas",
        "Playera licra sin mangas",
        "Gorra",
        "Chamarra",
        "Sudadera deportiva",
    ],
)

# --- COLOR Y TALLA ---
if prenda == "Bata":
    color = st.selectbox("🎨 Color:", ["Blanco", "Guinda", "Azul Marino"])
    talla = st.selectbox("📏 Talla (solo bata):", ["28", "30", "32", "34", "36", "38", "40", "42", "44", "46"])
else:
    color = st.text_input("🎨 Color:")
    talla = st.selectbox("📏 Talla:", ["CH", "M", "G", "XG", "XXG"])

# --- CORTE ---
corte = st.selectbox("✂️ Corte:", ["Dama", "Caballero"])

# --- BORDADOS ---
bordado = st.text_input("🧶 Bordado (Ejemplo: POLITÉCNICO + ESIME, ESIME, ESIA, UPIBI, etc.):")

# --- PAGOS ---
a_cuenta = st.number_input("💰 A cuenta ($):", min_value=0, step=1)
restan = st.number_input("💸 Restan ($):", min_value=0, step=1)
total = st.number_input("💵 Total ($):", min_value=0, step=1)

# --- ENTREGA ---
fecha_entrega = st.date_input("📅 Fecha de entrega:")
punto_entrega = st.text_input("📍 Punto de entrega:")
tipo = st.selectbox("🧾 Tipo:", ["Ventas", "Pedidos"])

# --- BOTÓN GUARDAR ---
# --- BOTÓN GUARDAR ---
if st.button("💾 Guardar registro"):
    # Convertir tipo a plural correctamente
    tipo_plural = "Ventas" if tipo.lower() == "Ventas" else "Pedidos"
    hoja_destino = f"{vendedor.capitalize()}_{tipo_plural}"

    data = {
        "vendedor": vendedor,
        "nombre_cliente": nombre_cliente,
        "telefono": telefono,
        "prenda": prenda,
        "color": color,
        "talla": talla,
        "corte": corte,
        "bordado": bordado,
        "a_cuenta": a_cuenta,
        "restan": restan,
        "total": total,
        "fecha_entrega": str(fecha_entrega),
        "punto_entrega": punto_entrega,
        "tipo": tipo,
        "hoja": hoja_destino,
    }

    if guardar_registro(data):
        st.success(f"✅ Registro guardado correctamente en la hoja **{hoja_destino}**.")
    else:
        st.error("❌ Error al guardar el registro.")


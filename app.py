"""
Script: app.py
Descripción: Dashboard interactivo de ciberseguridad, Habeas Data y RBAC para Carsystem.
"""
import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la interfaz del Dashboard
st.set_page_config(page_title="Ciberseguridad & Gobernanza - Carsystem", page_icon="🛡️", layout="wide")
st.title("🛡️ Centro de Control de Ciberseguridad y Cumplimiento - Carsystem")
st.markdown("Plataforma operativa para la validación de Habeas Data (Ley 1581), control de accesos RBAC y auditoría de inventario.")
st.markdown("---")

# Pestañas de navegación para la auditoría
tab1, tab2, tab3 = st.tabs(["📊 Dashboard de Riesgos", "⚖️ Gatekeeper Habeas Data", "🔒 Matriz RBAC & Inventario"])

with tab1:
    st.subheader("📈 Indicadores Clave de Exposición y Cumplimiento")
    col1, col2, col3 = st.columns(3)
    col1.metric("Exposición Legal (Habeas Data)", "$16,781,000 COP", delta="-33.3% Clientes sin autorizar", delta_color="inverse")
    col2.metric("Descuadre de Inventario (RBAC)", "-$8,380,000 COP", delta="-157 Unidades fantasma", delta_color="inverse")
    col3.metric("Estado del Firewall Cloud", "100% Activo", delta="Cifrado AES-256 + WORM")
    
    st.markdown("---")
    st.info("💡 **Resumen Ejecutivo:** La activación del Gatekeeper interactivo en WhatsApp y la restricción de escritura en la nube blindan la operación frente a sanciones legales y mermas fantasma.")

with tab2:
    st.subheader("⚖️ Protocolo Gatekeeper - Ley 1581 de 2012")
    st.warning("⚠️ Clientes identificados en riesgo legal por falta de consentimiento expreso en interacciones previas (C002, C006, C009, C012).")
    
    df_hab = pd.DataFrame({
        'Cliente_ID': ['C001', 'C002', 'C006', 'C009', 'C012'],
        'Segmento': ['Taller', 'Taller', 'Particular', 'Particular', 'Particular'],
        'Estado Habeas Data': ['Autorizado ✅', 'Pendiente / Bloqueado ❌', 'Pendiente / Bloqueado ❌', 'Pendiente / Bloqueado ❌', 'Pendiente / Bloqueado ❌'],
        'Valor Cotizado en Riesgo': ['$0 COP', '$2,816,000 COP', '$2,342,000 COP', '$4,195,000 COP', '$2,195,000 COP']
    })
    st.dataframe(df_hab, use_container_width=True)
    st.success("🔒 **Acción automática:** Al escribir por WhatsApp, el bot despliega los botones '[ ✅ Sí, autorizo ]' / '[ ❌ No autorizo ]', impidiendo procesar cotizaciones si el usuario no acepta.")

with tab3:
    st.subheader("🔒 Control de Acceso Basado en Roles (RBAC) & Auditoría")
    st.markdown("Matriz de privilegios aplicada para corregir el desfase histórico en la base de datos:")
    
    df_rbac = pd.DataFrame({
        'Rol de Usuario': ['Bodega (Logística)', 'Asesores Comerciales (E02-E08)', 'Administrador / Ciberseguridad'],
        'Permiso sobre Inventario': ['Escritura única en stock físico (con log de auditoría)', 'Solo Lectura (Previene sobreventas)', 'Control Total (CRUD)'],
        'Permiso sobre Precios / Cotizaciones': ['Sin Acceso', 'Escritura en Cotizaciones (Prohibido alterar precios)', 'Control Total']
    })
    st.dataframe(df_rbac, use_container_width=True)
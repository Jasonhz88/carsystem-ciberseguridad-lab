import pandas as pd
import numpy as np

def ejecutar_auditoria_ciberseguridad():
    # 1. Datos de clientes y estado de autorización de Habeas Data (Ley 1581)
    clientes_data = {
        'cliente_id': ['C001', 'C002', 'C006', 'C009', 'C012'],
        'nombre': ['Taller La 80', 'Mecánica Rápida Norte', 'Laura Gómez', 'Julián Álvarez', 'Santiago Ruiz'],
        'autoriza_tratamiento_datos': ['Sí', 'No registrado', 'No registrado', 'No registrado', 'No registrado'],
        'valor_cotizado_riesgo_cop': [0, 2816000, 2342000, 4195000, 2195000]
    }
    df_clientes = pd.DataFrame(clientes_data)
    
    # 2. Datos de inventario auditado (Descuadre histórico de Carsystem)
    inventario_data = {
        'sku': ['FR-101', 'MO-201', 'SU-301', 'EL-401'],
        'producto': ['Pastillas de freno', 'Filtro de aceite', 'Amortiguador', 'Batería 12V'],
        'stock_registrado': [28, 65, 19, 9],
        'stock_fisico': [12, 18, 11, 7],
        'costo_promedio': [82000, 28000, 180000, 277000]
    }
    df_inv = pd.DataFrame(inventario_data)
    
    # --- LÓGICA DE AUDITORÍA Y CIBERSEGURIDAD ---
    
    # Regla A: Auditoría de cumplimiento legal Habeas Data
    df_clientes['Estado_Legal'] = df_clientes['autoriza_tratamiento_datos'].apply(
        lambda x: 'COMPLIANT ✅' if x == 'Sí' else 'EN RIESGO LEGAL ⚠️ (Bloqueado por Gatekeeper)'
    )
    
    # Regla B: Calcular exposición financiera por clientes sin consentimiento
    riesgo_legal_total = df_clientes[df_clientes['autoriza_tratamiento_datos'] != 'Sí']['valor_cotizado_riesgo_cop'].sum()
    
    # Regla C: Calcular desfase físico y financiero en inventario (Control RBAC)
    df_inv['diferencia_uds'] = df_inv['stock_fisico'] - df_inv['stock_registrado']
    df_inv['perdida_neta_cop'] = df_inv['diferencia_uds'].abs() * df_inv['costo_promedio']
    descuadre_total_cop = df_inv['perdida_neta_cop'].sum()
    
    # 3. Diseñar el reporte ejecutivo de ciberseguridad
    reporte = f"=== REPORTE DE CIBERSEGURIDAD Y GOBERNANZA - CARSYSTEM ===\n\n"
    reporte += f"1. CONTROL DE HABEAS DATA (LEY 1581):\n"
    reporte += f"{df_clientes[['cliente_id', 'nombre', 'Estado_Legal']].to_string(index=False)}\n\n"
    reporte += f"🚨 EXPOSICIÓN LEGAL TOTAL: ${int(riesgo_legal_total):,} COP\n"
    reporte += f"----------------------------------------------------\n"
    reporte += f"2. AUDITORÍA DE INVENTARIO Y CONTROL RBAC:\n"
    reporte += f"{df_inv[['sku', 'producto', 'stock_registrado', 'stock_fisico', 'diferencia_uds']].to_string(index=False)}\n\n"
    reporte += f"🔒 DESCUADRE NETO AUDITADO: ${int(descuadre_total_cop):,} COP\n"
    
    return reporte

resultado_auditoria = ejecutar_auditoria_ciberseguridad()
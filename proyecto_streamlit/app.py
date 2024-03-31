import streamlit as st
from modules.innundaciones import show_map as innundacion
from modules.visualizations import show_map
from modules.temperaturas_historicas import show_map as temp_historicas
from modules.lluvias_historicas import show_map as lluvias_historicas
from modules.temperaturas_mortales import show_map as riesgo_mortal
from modules.temperaturas_futuras import show_map as temp_futuras
from modules.temperaturas_actualista import show_map as temp_actualista

import os
os.environ["AWS_ACCESS_KEY_ID"] = "CHANGEME"
os.environ["AWS_SECRET_ACCESS_KEY"] = "CHANGEME"

tab1, tab2, tab3 = st.tabs(["Histor-ista", "Futur-ista", "Actual-ista"])

with tab1:
    col1, col2 = st.columns([1, 3], gap="small")
    with col1:
        opciones = ["Selecciona", "Temperaturas", "Lluvias", "Riesgo de salud"]
        risk = st.selectbox("¿Qué riesgo quieres ver?", opciones, index=0)  

    with col2:
        if risk == "Selecciona":
            show_map()
        elif risk == "Temperaturas":
            temp_historicas()
        elif risk == "Lluvias":
            lluvias_historicas()
        elif risk == "Riesgo de salud":
            riesgo_mortal()

with tab2:
    st.header("Futur-ista")
    col1, col2 = st.columns([1, 3], gap="small")
    with col1:
        opciones = ["Selecciona", "Inundación", "Temperatura"]
        risk = st.selectbox("¿Qué riesgo quieres ver?", opciones, index=0)  

    with col2:
        if risk == "Selecciona":
            show_map()
        elif risk == "Inundación":
            innundacion()
        elif risk == "Temperatura":
            temp_futuras()

with tab3:
    st.header("Actual-ista")
    col1, col2 = st.columns([1, 3], gap="small")
    with col1:
        opciones = ["Selecciona", "Temp Máxima", "Temp Mínima"]
        risk = st.selectbox("¿Qué quieres ver?", opciones, index=0)  

    with col2:
        if risk == "Selecciona":
            show_map()
        elif risk == "Temp Máxima":
            temp_actualista("Temperatura Máxima")
        elif risk == "Temp Mínima":
            temp_actualista("Temperatura Mínima")

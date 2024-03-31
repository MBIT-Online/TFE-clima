import branca.colormap as cm
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

localidades_coordenadas = {
    'ALACANT/ALICANTE': [38.3452, -0.4810],
    'VALÈNCIA': [39.4699, -0.3763]
}

@st.cache_data
def cargar_datos():
    df = pd.read_csv('data/combined_alicante_valencia.csv')
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['tmed'] = df['tmed'].apply(pd.to_numeric, errors='coerce')
    df['tmed'].fillna(0, inplace=True)
    return df

df = cargar_datos()

anio_minimo = df['fecha'].dt.year.min()
anio_maximo = df['fecha'].dt.year.max()

@st.cache_data
def filtrar_datos(fecha_seleccionada):
    return df[df['fecha'].dt.year == fecha_seleccionada]

def crear_mapa(df_filtrado, columna_valor, escala_colores):
    mapa = folium.Map(location=[39.46975, -0.37739], zoom_start=7)
    for _, fila in df_filtrado.iterrows():
        lat, lon = localidades_coordenadas.get(fila['nombre'], [None, None])
        val = fila[columna_valor]
        if lat and lon and not pd.isna(val):
            color = escala_colores(val)
            folium.Circle(
                location=[lat, lon],
                radius=50000,
                color=color,
                fill=True,
                fill_color=color,
                popup=f"{fila['nombre']}: {val}°C"
            ).add_to(mapa)
    return mapa


def show_map():
    anio_seleccionado = st.slider("Selecciona un año", value=anio_minimo, min_value=anio_minimo, max_value=anio_maximo)

    df_filtrado = filtrar_datos(anio_seleccionado)

    escala_colores = cm.linear.YlOrRd_09.scale(df['tmed'].min(), df['tmed'].max())

    mapa_temp = crear_mapa(df_filtrado, 'tmed', escala_colores)
    st_folium(mapa_temp, width=725, height=525)

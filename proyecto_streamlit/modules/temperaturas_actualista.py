import branca.colormap as cm
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

localidades_coordenadas = {
    'Alicante': [38.3452, -0.4810],
    'Javea': [38.7895, 0.1661],
    'Pinoso': [38.4017, -1.0422],
    'Castellfort': [40.4147, -0.4204],
    'Castelló de la Plana': [39.9864, -0.0515],
    'Vinaròs': [40.4706, 0.4750],
    'Valencia': [39.4699, -0.3763],
    'Oliva': [38.9191, -0.1210],
    'Utiel': [39.5667, -1.2005],
    'Xàtiva': [38.9893, -0.5153]
}

@st.cache_data
def cargar_datos():
    df = pd.read_parquet('data/Predicciones_completas_2024_03_31.parquet')
    df['datetime'] = pd.to_datetime(df['datetime'])
    df['app_max_temp'] = df['app_max_temp'].apply(pd.to_numeric, errors='coerce')
    df['app_max_temp'].fillna(0, inplace=True)
    return df

df = cargar_datos()

fecha_minima = df['datetime'].min().date()
fecha_maxima = df['datetime'].max().date()

@st.cache_data
def filtrar_datos_por_anio(anio_seleccionado):
    return df[df['datetime'].dt.date == anio_seleccionado]

def crear_mapa(df_filtrado, columna_valor, escala_colores):
    mapa = folium.Map(location=[39.46975, -0.37739], zoom_start=7)
    for _, fila in df_filtrado.iterrows():
        lat, lon = localidades_coordenadas.get(fila['city_name'], [None, None])
        val = fila[columna_valor]
        if lat and lon and not pd.isna(val):
            color = escala_colores(val)
            folium.Circle(
                location=[lat, lon],
                radius=10000,
                color=color,
                fill=True,
                fill_color=color,
                popup=f"{fila['city_name']}: {val}°C"
            ).add_to(mapa)
    return mapa

def show_map(temp):
    fecha_seleccionada = st.slider("Selecciona una fecha", value=fecha_minima, min_value=fecha_minima, max_value=fecha_maxima, format="YYYY-MM-DD")

    df_filtrado = filtrar_datos_por_anio(fecha_seleccionada)

    escala_colores = cm.linear.YlOrRd_09.scale(10, 30)

    if temp == 'Temperatura Máxima':
        t = 'app_max_temp'
    elif temp == 'Temperatura Mínima':
        t = 'app_min_temp'
    mapa_temp = crear_mapa(df_filtrado, t, escala_colores)
    st_folium(mapa_temp, width=725, height=525)

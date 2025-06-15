import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
header = st.header('Construcción de gráficos en una aplicación web')
hist_check = st.checkbox('Construir histograma') # crear un checkbox
disp_check = st.checkbox('Construir gráfico de dispersión')
exe_button = st.button('Crear gráficos') # crear un botón

if exe_button:
     if hist_check: # al hacer clic en el botón
     # escribir un mensaje
          st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
          # crear un histograma
          fig_hist = px.histogram(car_data, x="odometer")
     
          # mostrar un gráfico Plotly interactivo
          st.plotly_chart(fig_hist, use_container_width=True)

     if disp_check: # al hacer clic en el botón
     # escribir un mensaje
          st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
         
          # crear un histograma
          fig_disp = px.scatter(car_data, x="odometer", y="price")
     
          # mostrar un gráfico Plotly interactivo
          st.plotly_chart(fig_disp, use_container_width=True)
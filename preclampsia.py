#%% Fase 1. Librerias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# %%
df = pd.read_excel('registropacientes (5).xlsx')
# %%
pacientes_mme_1 = df[df['MME'] == 1]

# Contar cuántos de estos pacientes tienen Eclampsia en 1 y Mortalidad Materna Extrema en 1
num_pacientes_eclampsia = len(pacientes_mme_1[pacientes_mme_1['Eclampsia'] == 1])
num_pacientes_muerte_materna = len(pacientes_mme_1[pacientes_mme_1['Muerte materna'] == 1])

# Preparar los datos para el diagrama de torta
labels = ['Eclampsia', 'Muerte materna']
sizes = [num_pacientes_eclampsia, num_pacientes_muerte_materna]
colors = ['#ff9999', '#66b3ff']


# Contar el número de pacientes con MME=1 y MME=0
num_pacientes_mme_1 = len(df[df['MME'] == 1])
num_pacientes_mme_0 = len(df[df['MME'] == 0])

# Crear un DataFrame para los datos del gráfico de barras
data = {'MME': ['Pacientes con MME', 'Pacientes sin MME'], 'Número de Pacientes': [num_pacientes_mme_1, num_pacientes_mme_0]}
df_plot = pd.DataFrame(data)


# Filtrar los pacientes con MME igual a 1
pacientes_mme_1 = df[df['MME'] == 1]

# Filtrar los pacientes con MME igual a 1
pacientes_mme_1 = df[df['MME'] == 1]

# Filtrar los pacientes con MME igual a 1 que respondieron positivamente al medicamento 1
pacientes_mme_1_resp_L1 = df[(df['MME'] == 1) & (df['RecibioNifedipino'] == 1) & (df['RecibioLabetalol'] == 0) & (df['RecibioNitroprusiato'] == 0)]

# Contar cuántos pacientes requirieron cada medicamento
num_pacientes_med_1 = len(pacientes_mme_1_resp_L1)
num_pacientes_med_2 = len(df[(df['MME'] == 1) & (df['RecibioNifedipino'] == 1) & (df['RecibioLabetalol'] == 1) & (df['RecibioNitroprusiato'] == 0)])
num_pacientes_med_3 = len(df[(df['MME'] == 1) & (df['RecibioNifedipino'] == 1) & (df['RecibioLabetalol'] == 1) & (df['RecibioNitroprusiato'] == 1)])

# Preparar los datos para el diagrama de torta
labels = ['Nifedipino', 'Labetalol', 'Nitroprusiato']
sizes = [num_pacientes_med_1, num_pacientes_med_2, num_pacientes_med_3]
#%% Fase 4: Creación del Dashboard en Streamlit
# 4.1 Estructura básica
import streamlit as st

# Configuración de la página
st.set_page_config(layout="wide")
st.title('Análisis de datos- Registros de pacientes referente a Preclampsia')
st.title('Fundación Valle del Lili')
# %% Graficos
tab1, tab2, tab3, tab4, tab5= st.tabs(["Descenlace de pacientes con Morbilidad Materna Extrema", "Comparación del número de pacientes con Morbilidad Materna Extrema (MME)", "Distribución de edades de pacientes con Morbilidad Materna Extrema", "Distribución de frecuencia cardíaca en pacientes con Morbilidad Materna Extrema", "Distribución de frecuencia cardíaca en pacientes con Morbilidad Materna Extrema"])
with tab1:
    # Grafico 1: Estado de la útlima cita, porcentaje de asistencia e inasistencia en la base de datos
    st.write("## Descenlace de pacientes con Morbilidad Materna Extrema")
    # Crear el gráfico de torta
    colors = ['#ff9999', '#66b3ff', '#99ff99']  # Colores de cada porción
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops={'linewidth': 0.5, 'edgecolor': 'black'})
    ax.axis('equal')  # Aspecto igual para asegurar que el pastel se dibuje como un círculo

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)
with tab2:
# Crear el gráfico de barras con Seaborn
    st.write("## Comparación del número de pacientes con Morbilidad Materna Extrema (MME)")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(data=df_plot, x='MME', y='Número de Pacientes', palette='Set2')
    plt.ylabel('Número de Pacientes')

    # Agregar el número de pacientes en cada barra
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=12, color='black', xytext=(0, 5),
                    textcoords='offset points')

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)
with tab3:
    # Crear el gráfico de violín con Seaborn
    st.write("## Distribución de edades de pacientes con Morbilidad Materna Extrema")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.violinplot(data=pacientes_mme_1, y='Edad paciente', color='skyblue')
    plt.ylabel('Edad')
# Mostrar el gráfico en Streamlit
    st.pyplot(fig)
with tab4:
    st.write("## Distribución de frecuencia cardíaca en pacientes con Morbilidad Materna Extrema")
    # Crear el gráfico de densidad con Seaborn
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.kdeplot(data=pacientes_mme_1, x='Frecuencia Cardiaca', color='skyblue', fill=True)
    plt.xlabel('Frecuencia Cardíaca')
    plt.ylabel('Densidad')

# Mostrar el gráfico en Streamlit
    st.pyplot(fig)
with tab5:
    st.write("## ¿Qué medicamento requirieron los pacientes con Morbilidad Materna Extrema?")
    # Preparar los datos para el diagrama de torta
    labels = ['Nifedipino', 'Labetalol', 'Nitroprusiato']
    sizes = [num_pacientes_med_1, num_pacientes_med_2, num_pacientes_med_3]
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    # Crear el gráfico de torta
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90,wedgeprops={'linewidth': 0.5, 'edgecolor': 'black'})
    ax.axis('equal')  # Aspecto igual para asegurar que el pastel se dibuje como un círculo

# Mostrar el gráfico en Streamlit
    st.pyplot(fig)

# %%

"""
PROYECTO 2: "EL MURO DE LA LIGA" (ANÁLISIS DEFENSIVO)
Autor: Daniela Jimenez
Fecha: 9 de Noviembre 2026
Descripción: Este script analiza a los defensas de La Liga con más de 600 minutos jugados.
Calcula sus "Acciones Defensivas por 90 minutos" (entradas ganadas + intercepciones)
para identificar a los defensas más sólidos y generar un gráfico de barras horizontales.
Datos: Kaggle / FBref (La Liga 2026-2027).
"""

import pandas as pd
import matplotlib.pyplot as plt

# Datos
Ruta_Datos = 'Proyecto_2_Muro/data/players_data-2026_2027.csv'
df = pd.read_csv(Ruta_Datos)

#filto
df_defensas = df[
    (df['Pos'] == 'DF') &
    (df['Min'] > 600) &
    (df['Comp'] == 'es La Liga')
]

# Metricas
# Calcular cuantos partidos ha jugado cada jugador
df_defensas['Partidos_jugados'] = df_defensas['Min'] / 90

# Suma de entradas ganadas y intercepciones
df_defensas['Acciones_defensivas'] = df_defensas['TklW'] + df_defensas['Int']

# Divir las acciones defensivas por los partidos jugados para obtener la métrica por 90 minutos
df_defensas['Acciones_por_90'] = df_defensas['Acciones_defensivas'] / df_defensas['Partidos_jugados']

print("\n--- TOP 5 DEFENSAS MÁS SÓLIDOS ---")
print(df_defensas[['Player', 'Squad', 'TklW', 'Int', 'Acciones_por_90']].sort_values(by='Acciones_por_90', ascending=False).head(5))  

#Grafico
plt.figure(figsize=(10, 6))
top_defensas = df_defensas.sort_values(by='Acciones_por_90', ascending=False).head(5)
plt.barh(top_defensas['Player'], top_defensas['Acciones_por_90'], color='green')
plt.title('Top 5 Defensas Más Sólidos de La Liga (Acciones Defensivas por 90 minutos)')
plt.xlabel('Acciones Defensivas por 90 minutos')    
plt.gca().invert_yaxis() # Invierte el eje Y para que el Top 1 quede arriba


#resultados
plt.show()
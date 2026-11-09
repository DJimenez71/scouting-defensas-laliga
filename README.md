# 🛡️ Proyecto 2: El Muro de La Liga (Análisis Defensivo)

## 📌 Descripción del Proyecto
Este proyecto utiliza Python y Pandas para analizar el rendimiento defensivo de los jugadores de La Liga en la temporada 2026-2027. El objetivo principal es identificar a los defensas más sólidos, yendo más allá del total de acciones y calculando su rendimiento real por cada 90 minutos jugados.

"Nota metodológica: Los datos analizados corresponden a la fecha de descarga del dataset (Noviembre de 2026). Al ser una temporada en curso, las métricas son parciales y pueden variar a medida que avancen las jornadas."

## 🎯 Preguntas de Negocio (Insights)
Como analista de datos, busqué responder:
1. ¿Quiénes son los defensas más activos de la liga?
2. ¿Los mejores defensas juegan en los equipos grandes (Real Madrid, Barcelona, Atlético) o hay "gangas" en equipos de media tabla?
3. ¿Cómo afecta el tiempo de juego al rendimiento defensivo real?

## 🛠️ Tecnologías Utilizadas
*   **Python 3.x**
*   **Pandas:** Para el filtrado, agrupación y creación de nuevas métricas.
*   **Matplotlib:** Para la visualización de datos mediante gráficos de barras horizontales.
*   **VS Code** como entorno de desarrollo.

## ⚙️ Metodología (El Cálculo)
Para que el análisis sea justo, se aplicaron dos reglas:
1. **Filtro de minutos:** Se excluyeron a los jugadores con menos de 600 minutos jugados para evitar anomalías estadísticas (ej. un jugador que entra 5 minutos y hace 2 entradas).
2. **Métrica "Per 90":** En lugar de usar el total de acciones, se calculó la métrica dividiendo las acciones totales entre los partidos completos jugados `(Min / 90)`.
   * *Fórmula:* `(Entradas Ganadas [TklW] + Intercepciones [Int]) / (Minutos / 90)`

## 📊 Visualización Destacada
![Gráfico Defensas](images/grafico_defensas.png)


El gráfico muestra el Top 5 de defensas con mayor promedio de acciones defensivas por cada 90 minutos. 

## 🧠 Conclusiones Principales
*   **Jon Aramburu (Real Sociedad)** lidera la métrica con **4.42 acciones defensivas por partido**, demostrando una capacidad de recuperación excepcional.
*   **Manu Sánchez (Levante)** y **Gabriel Suazo (Sevilla)** completan el podio, confirmando que los defensas más sólidos en métricas "per 90" no necesariamente pertenecen a los equipos de élite.
*   Aunque **Marc Cucurella (Real Madrid)** aparece en el Top 3, el análisis revela que hay talento altamente eficiente en equipos de media tabla que representan una gran oportunidad de mercado (Value Betting) para el scouting.

## 🚀 Cómo ejecutar este proyecto
1. Clona este repositorio.
2. Instala las dependencias necesarias: `pip install pandas matplotlib`
3. Ejecuta el script principal: `python src/analisis_defensivo.py`

---
*Análisis realizado por Daniela Jimenez como parte de mi portafolio de análisis de datos deportivos.*
*9 de noviembre de 2026*
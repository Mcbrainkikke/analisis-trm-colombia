# 📊 Análisis de Series de Tiempo — TRM Colombia

Análisis estadístico de la Tasa de Cambio Representativa del Mercado (TRM) 
colombiana usando Python, aplicando regresión lineal e identificación de 
componentes de series de tiempo.

---

## 🗂️ Descripción del proyecto

Este proyecto analiza la serie histórica diaria de la TRM del Banco de la 
República de Colombia desde el 27 de noviembre de 1991 hasta el 30 de 
septiembre de 2021, un total de 10.901 registros.

El análisis se divide en tres partes:

- **Punto 2:** Regresión lineal de los últimos 50 días de la serie
- **Punto 3:** Análisis por año para el período 2011–2020
- **Punto 4:** Análisis por décadas (1991-2000, 2001-2010, 2010-2020)

---

## 🛠️ Tecnologías utilizadas

- Python 3.12
- pandas
- numpy
- matplotlib
- scipy

---

## 📁 Estructura del proyecto
analisis-trm-colombia/
│
├── analisis.py               # Punto 2: regresión lineal últimos 50 días
├── punto3.py                 # Punto 3: análisis por año 2011-2020
├── Punto4.py                 # Punto 4: análisis por décadas
├── TCM_Serie_historica_IQY.xlsx  # Datos fuente — Banco de la República
│
├── Figura punto 2.png        # Gráfica regresión lineal 50 días
├── Figura punto 3 2011.png   # Gráficas por año
├── ...
└── Figura punto 4 2010-2020.png  # Gráficas por década

---

## 📈 Principales hallazgos

| Período | Pearson (r) | Componente | Interpretación |
|---------|------------|-----------|---------------|
| Últimos 50 días | -0.3048 | Irregular | Leve tendencia bajista sin dirección clara |
| 2013 | 0.8849 | Tendencia alcista | Inicio de devaluación sostenida |
| 2015 | 0.9027 | Tendencia alcista | Choque petrolero, fuerte devaluación |
| 2020 | 0.1407 | Irregular | Volatilidad extrema por COVID-19 |
| Década 1991-2000 | 0.9408 | Tendencia alcista | Devaluación estructural fuerte |
| Década 2001-2010 | -0.6700 | Tendencia bajista | Boom de commodities fortaleció el peso |
| Década 2010-2020 | 0.9225 | Tendencia alcista | Nueva ola de devaluación estructural |

---

## 🚀 Cómo ejecutar el proyecto

1. Clone el repositorio
git clone https://github.com/Mcbrainkikke/analisis-trm-colombia.git

2. Instale las dependencias
pip install pandas numpy matplotlib scipy openpyxl

3. Ejecute cada archivo según el análisis que quiera ver
python analisis.py
python punto3.py
python Punto4.py

---

## 📂 Fuente de datos

Banco de la República de Colombia — Serie histórica TRM  
https://www.banrep.gov.co

---

## 👤 Autor

**Victor Wilches** — Estudiante de Ingeniería de sistemas 
GitHub: [@Mcbrainkikke](https://github.com/Mcbrainkikke)
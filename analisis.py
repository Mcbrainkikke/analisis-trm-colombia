import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_excel('TCM_Serie_historica_IQY.xlsx', header=7) #lee el archivo Excel. header=7 lee los datos apartir de la fila 8

df.columns = ['fecha', 'trm'] # se renombran las columnas

# Convierte la columna fecha a tipo de fecha real
# errors=coerce convierte lo que no sea fecha a en nulo
df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce') 

# Elimina las filas donde la fecha queda nula
df = df[df['fecha'].notna()]

# Ordena de la mas antigua a la mas reciente y pone la fecha como indice
df = df.sort_values('fecha').set_index('fecha')

print(df.head(5)) # muestra las primeros 5 filas
print(df.tail(5)) # muestra las ultimas 5
print(df.shape) # muestra la cantidad de filas y columnas del archivo
print(df.dtypes) # muestra el tipo de datos del archivo

# .tail(50) toma las ultimas 50 filas del archivo
df_50 = df.tail(50)
df_50 = df_50.copy()

# se crea la variable x con una secuencia de 1 a 50
# el día mas antiguo seria X=1 el que le sigue X=2 ...
df_50['x'] = np.arange(1, 51) 

print("Periodo de los ultimos 50 días:")
print("Desde:", df_50.index[0].date)
print("Hasta:", df_50.index[-1].date)
print()
print(df_50.head(5))
print(df_50.tail(5))

# linregress calcula la regresión lineal entre x y el TRM
# se pasa la columna x (1 al 50) y la columna del TRM
slope, intercept, r_value, p_value, std_err = stats.linregress(df_50['x'], df_50['trm'])

""" slope = la pendiente, es el valor a en y = ax + b
	intercept = el intercepto, es decir el valor de b
	r_value = el coeficiente de Pearson """

print("--- PUNTO 2 — Regresión Lineal de los ultimos 50 días --- \n")
print(f"Coeficiente de Pearson (r): {r_value:.4f}") # la F permite poner variables dentro de un texto
print(f"Ecuación: Y = {slope:.4f} x + ({intercept:.4f})") # :.4f muestra el valor con 4 decimales

# calcula los valores que predice la recta oara cada x
y_pred = slope * df_50['x'] + intercept

# se crea la figura con tamaño 12x5 pulgadas
plt.figure(figsize=(12, 5))

# puntos reales: cada día con un TRM real observada
plt.scatter(df_50.index, df_50['trm'], color='steelblue', s = 40, label='TRM Real')

# linea de progresión: los valores que predice el modelo
plt.plot(df_50.index, y_pred, color='red', linewidth=2,
		 label=f'y = {slope:.4f} x + {intercept:.4f} | r= {r_value:.4f}')

plt.title('Punto 2 - regresión lineal: Ultimos 50 días de TRM')
plt.xlabel('Fecha')
plt.ylabel('TRM')
plt.legend()
plt.tight_layout()
plt.show()
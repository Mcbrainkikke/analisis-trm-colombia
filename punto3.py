import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# carga y limpieza de datos
df = pd.read_excel('TCM_Serie_historica_IQY.xlsx', header=7)
df.columns = ['fecha', 'trm']
df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
df = df[df['fecha'].notna()]
df = df.sort_values('fecha').set_index('fecha')

# bucle para 10 años
anios = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

for anio in anios:
	df_anio = df[df.index.year == anio].copy()
	df_anio['x'] = np.arange(1, len(df_anio) + 1)

	slope_y, intercept_y, r_y, p_value, std_err = stats.linregress(df_anio['x'], df_anio['trm'])

	y_pred_y = slope_y * df_anio['x'] + intercept_y

	print(f"--- Año {anio} ---")
	print(f"Observaciones: {len(df_anio)}")
	print(f"Pearson (r): {r_y:.4f}")
	print(f"Ecuación: y = {slope_y:.4f} x + ({intercept_y:.4f})")
	print()

	# Identificamos el componente según el valor de r
	abs_r = abs(r_y)  # usamos el valor absoluto para no preocuparnos por el signo

	if abs_r >= 0.7:
		if r_y > 0:
			componente = "Tendencia alcista"
		else:
			componente = "Tendencia bajista"
	elif abs_r >= 0.5:
		componente = "Tendencia moderada"
	elif abs_r >= 0.3:
		componente = "Irregular"
	else:
		componente = "Irregular / Sin patrón claro"

	print(f"Componente: {componente}")
	print()

	# graficar
	plt.figure(figsize=(12, 5))
	plt.plot(df_anio.index, df_anio['trm'], color='steelblue', linewidth=1.2, label='TRM Real')
	plt.plot(df_anio.index, y_pred_y, color='red', linewidth=2, linestyle='--', label=f'y = {slope_y:.4f} x + {intercept_y:.4f} | r = {r_y:.4f}')
	plt.title(f'Año {anio} - Serie de tiempo TRM')
	plt.xlabel('Fecha')
	plt.ylabel('TRM')
	plt.legend()
	plt.tight_layout()
	plt.show()

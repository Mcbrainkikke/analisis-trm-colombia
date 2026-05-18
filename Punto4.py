import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# carga y limpieza de datos
df = pd.read_excel('TCM_Serie_historica_IQY.xlsx', header=7) # header=7 lee los datos apartir de la fila 8
df.columns = ['fecha', 'trm']
df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
df = df[df['fecha'].notna()]
df = df.sort_values('fecha').set_index('fecha')

# definicion de decadas
# cada decada es una tupla que contiene (nombre, año de inicio, año final)
decadas = [
	('1991-2000', 1991, 2000),
	('2001-2010', 2001, 2010),
	('2010-2020', 2010, 2020)
]

# bucle para tres decadas

for nombre, inicio, fin in decadas:
	df_decada = df[(df.index.year >= inicio) & (df.index.year <= fin)].copy()
	df_decada = df_decada.assign(x=np.arange(1, len(df_decada) + 1))

	slope_d, intercept_d, r_d, p_value, std_err = stats.linregress(df_decada['x'], df_decada['trm'])

	y_pred_d = slope_d * df_decada['x'] + intercept_d

	abs_r = abs(r_d)
	if abs_r >= 0.7:
		if r_d > 0:
			componente = "Tendencia alcista"
		else:
			componente = " Tendencia bajista"
	elif abs_r >= 0.5:
			componente = "Tendencia moderada"
	elif abs_r >= 0.3:
			componente = "Irregular "
	else:
		componente = "Irregular / Sin patron claro "

	print(f"---Decada {nombre} ---")
	print(f"Observaciones {len(df_decada)}")
	print(f"Pearsons (r): {r_d:.4f}")
	print(f"Ecuacion: Y = {slope_d:.4f} x + ({intercept_d:.4f})")
	print(f"Componente: {componente}")

	plt.figure(figsize=(12, 5))
	plt.plot(df_decada.index, df_decada['trm'], color='steelblue', linewidth=1, label='TRM Real')
	plt.plot(df_decada.index, y_pred_d, color='red', linewidth=2, linestyle='--', label=f'y = {slope_d:.4f} x + ({intercept_d:.4f} | r = {r_d:.4f}')
	plt.title(f'Decada {nombre} - Serie de tiempo TRM')
	plt.xlabel('Fecha')
	plt.ylabel('TRM')
	plt.legend()
	plt.tight_layout()
	plt.show()


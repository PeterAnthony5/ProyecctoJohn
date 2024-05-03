import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv('Demograficos.csv')

print("Base de datos original:")
print(data.head())

# Limpiar la columna 'Edad'
data['Edad'] = data['Edad'].replace(to_replace=r'[^\d]+', value='', regex=True)
data['Edad'] = pd.to_numeric(data['Edad'])

# Limpiar la columna 'Ingresos'
data['Ingresos'] = data['Ingresos'].replace(to_replace=r'[^\d.]+', value='', regex=True)
data['Ingresos'] = pd.to_numeric(data['Ingresos'])

# Manejar valores NA
data.dropna(inplace=True)

# Identificar y manejar valores atípicos en 'Ingresos'
Q1 = data['Ingresos'].quantile(0.25)
Q3 = data['Ingresos'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
data = data[(data['Ingresos'] >= lower_bound) & (data['Ingresos'] <= upper_bound)]

# Análisis exploratorio básico
print("Estadísticas descriptivas de ingresos:")
print(data['Ingresos'].describe())

# Distribución de ingresos por nivel de escolaridad
plt.figure(figsize=(10, 6))
data.groupby('Nivel_escolaridad')['Ingresos'].mean().plot(kind='bar')
plt.title('Ingresos promedio por nivel de escolaridad')
plt.xlabel('Nivel de escolaridad')
plt.ylabel('Ingresos promedio')
plt.show()

# Guardar los datos limpios
data.to_csv('Demograficos_limpios.csv', index=False)

print("\nBase de datos después de la limpieza:")
print(data.head())

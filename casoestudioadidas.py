import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# URL de los datos
url = 'https://raw.githubusercontent.com/Naren8520/Serie-de-tiempo-con-Machine-Learning/main/Data/Adidas%20US%20Sales%20Data.csv'

# Cargar los datos
data = pd.read_csv(url, delimiter=';')
data['Invoice Date'] = pd.to_datetime(data['Invoice Date'])
data['Total Sales'] = data['Total Sales'].replace('[\$,]', '', regex=True).astype(float)
data['Price per Unit'] = data['Price per Unit'].replace('[\$,]', '', regex=True).astype(float)

# Crear la figura y los ejes
fig, ax1 = plt.subplots(figsize=(14, 7))

# Configurar el primer eje y (ventas totales)
color = 'tab:blue'
ax1.set_xlabel('Fecha')
ax1.set_ylabel('Total de ventas', color=color)
ax1.plot(data['Invoice Date'], data['Total Sales'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Añadir el segundo eje y (precio por unidad)
ax2 = ax1.twinx()  # Crea un segundo eje y que comparte el mismo eje x
color = 'tab:red'
ax2.set_ylabel('Precio por unidad', color=color)
ax2.plot(data['Invoice Date'], data['Price per Unit'], color=color, linestyle='--')
ax2.tick_params(axis='y', labelcolor=color)

# Título y configuración adicional
plt.title('ventas y precios a lo largo del tiempo')
plt.grid(True)
plt.show()

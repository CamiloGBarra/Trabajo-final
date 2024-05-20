import rasterio
from rasterio.plot import show
import numpy as np
import matplotlib.pyplot as plt

ruta_GREEN = r'.\imagen_extraida\2023-03-11.SR_B3.tif'
ruta_SWIR = r'.\imagen_extraida\2023-03-11.SR_B6.tif'

with rasterio.open(ruta_GREEN) as banda_verde:
    b3 = banda_verde.read(1).astype('float32')

with rasterio.open(ruta_SWIR) as banda_swir:
    b6 = banda_swir.read(1).astype('float32')

mndwi = (b3 - b6) / (b3 + b6) # Cálculo del MNDWI

# Visualización
plt.figure(figsize=(10, 10))
plt.imshow(mndwi, cmap='RdBu')
plt.colorbar(label='MNDWI')
plt.title('MNDWI Landsat 8')
plt.xlabel('Número de Columna')
plt.ylabel('Número de Fila')
plt.show()
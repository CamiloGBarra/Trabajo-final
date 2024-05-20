import rasterio
import matplotlib.pyplot as plt

ruta_RED = r'.\imagen_extraida\2023-03-11.SR_B4.tif'
ruta_NIR = r'.\imagen_extraida\2023-03-11.SR_B5.tif'

with rasterio.open(ruta_RED) as banda_roja:
    b4 = banda_roja.read(1).astype('float32')

with rasterio.open(ruta_NIR) as banda_nir:
    b5 = banda_nir.read(1).astype('float32')

ndvi = (b5 - b4) / (b5 + b4) # Cálculo del NDVI

# Visualización
plt.figure(figsize=(10, 10))
plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar(label='NDVI')
plt.title('NDVI Landsat 8')
plt.xlabel('Número de Columna')
plt.ylabel('Número de Fila')
plt.show()

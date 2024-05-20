from ndvi import ndvi # se importa la imagen NDVI obtenida previamente
from mascara import agua # se importa la máscara de agua obtenida previamente

import numpy as np
import matplotlib.pyplot as plt

ndvi_con_mascara = agua * ndvi

ndvi_con_mascara[(ndvi_con_mascara == 0)] = np.nan

# Visualización
plt.figure(figsize=(10, 10))
plt.imshow(ndvi_con_mascara, cmap='RdYlGn', vmin = -0.03, vmax = 0.005)
plt.colorbar(label='NDVI')
plt.title('NDVI Landsat 8 - Embalse Los Molinos')
plt.xlabel('Número de Columna')
plt.ylabel('Número de Fila')
plt.show()
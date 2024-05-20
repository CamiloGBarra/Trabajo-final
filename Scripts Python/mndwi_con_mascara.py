from mndwi import mndwi # se importa la imagen MNDWI obtenida previamente
from mascara import agua # se importa la máscara de agua obtenida previamente

import numpy as np
import matplotlib.pyplot as plt

mndwi_con_mascara = agua * mndwi

mndwi_con_mascara[(mndwi_con_mascara == 0)] = np.nan

# Visualización
plt.figure(figsize=(10, 10))
plt.imshow(mndwi_con_mascara, cmap = 'RdBu', vmin = 0.01, vmax = 0.05)
plt.colorbar(label='MNDWI')
plt.title('MNDWI Landsat 8 - Embalse Los Molinos')
plt.xlabel('Número de Columna')
plt.ylabel('Número de Fila')
plt.show()
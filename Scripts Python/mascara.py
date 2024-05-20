from mndwi import mndwi # imagen MNDWI obtenido previamente

import numpy as np
import matplotlib.pyplot as plt

condicion = mndwi > 0
agua = np.where(condicion, 1, 0)

# Visualización
plt.imshow(agua, cmap='Greys')
plt.title('Agua (MNDWI > 0)')
plt.show()
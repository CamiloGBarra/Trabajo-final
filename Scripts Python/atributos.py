from funciones import atributos_imagen

ruta_imagen = r'.\imagen_extraida\2023-03-11.SR_B1.tif'
atributos = atributos_imagen(ruta_imagen)

for atributo, informacion in atributos.items():
    print(f"{atributo}: {informacion}")
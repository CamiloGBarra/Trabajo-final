from funciones import leer_metadata, exportar_metadata_txt

archivo_tif = r'.\imagen_extraida'
ruta_salida = r'.\metadata.txt'

metadata = leer_metadata(archivo_tif)

exportar_metadata_txt(metadata, ruta_salida)

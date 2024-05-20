import zipfile
import rasterio
import os

def extraer_zip(archivo_zip, carpeta_destino):
    with zipfile.ZipFile(archivo_zip, 'r') as extarccion:
        extarccion.extractall(carpeta_destino)

        
def atributos_imagen (ruta_imagen):
    atributos = {}
    with rasterio.open(ruta_imagen) as src:
        for atributo in dir(src):
            if not atributo.startswith('_'):
                try:
                    informacion = getattr(src, atributo)
                    atributos[atributo] = informacion
                except Exception as e:
                    atributos[atributo] = str(e)
                
    return atributos


def leer_metadata(carpeta):
    metadata = {}
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".tif"):
            ruta_archivo = os.path.join(carpeta, archivo)
            with rasterio.open(ruta_archivo) as src:
                metadata[archivo] = {
                    "formato_del_archivo": src.driver,
                    "tipo_de_dato": src.dtypes[0],
                    "ancho": src.width, # cantidad de columnas
                    "alto": src.height, # cantidad de filas
                    "cantidad_de_bandas": src.count,
                    "sistema_de_referencia": src.crs,
                    "límites": src.bounds, # (izquierda, abajo, derecha, arriba)
                    "resolución": src.res, # (resolución_x, resolución_y)
                    "no data": src.nodata # valor que representa los datos faltantes
                }
    return metadata


def exportar_metadata_txt(metadata, ruta_salida):
    with open(ruta_salida, 'w') as f:
        for archivo, datos in metadata.items():
            f.write(f"Archivo: {archivo}\n")
            for clave, valor in datos.items():
                f.write(f"{clave}: {valor}\n")
            f.write("\n")
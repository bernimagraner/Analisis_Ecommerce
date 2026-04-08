import pandas as pd


def recomendar_productos_varios(
    productos_ids,
    matriz_similitud_path="../datos/procesados/similitud_item_item.pickle",
    n=5,
):
    similitud_item_item = pd.read_pickle(matriz_similitud_path)
    productos_validos = [p for p in productos_ids if p in similitud_item_item.index]
    if not productos_validos:
        raise ValueError("Ninguno de los productos está en la matriz de similaridad")
    distancias_medias = similitud_item_item.loc[productos_validos].mean(axis=0)
    distancias_medias = distancias_medias.drop(productos_validos)
    similares = distancias_medias.sort_values().iloc[:n]
    return similares.index.tolist()

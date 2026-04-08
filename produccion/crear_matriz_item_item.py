import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances

# Carga el DataFrame
df = pd.read_pickle("../datos/intermedios/tablon_analitico.pickle")

# Filtra compras y productos más comprados
temp = df.loc[df.evento == "purchase", ["usuario", "producto"]]
top_productos = temp["producto"].value_counts().head(100).index.tolist()
temp_top = temp.loc[temp["producto"].isin(top_productos)]

# Matriz usuario-item
matriz_usuario_item = temp_top.pivot_table(
    index="usuario", columns="producto", aggfunc="size", fill_value=0
)

# Matriz item-item (distancia euclídea)
matriz_item_usuario = matriz_usuario_item.T
distancia_euclid = euclidean_distances(matriz_item_usuario)
similitud_item_item = pd.DataFrame(
    distancia_euclid, index=matriz_item_usuario.index, columns=matriz_item_usuario.index
)

# Guarda la matriz
similitud_item_item.to_pickle("../datos/procesados/similitud_item_item.pickle")

from recomendador import recomendar_productos_varios

if __name__ == "__main__":
    productos_vistos = [5815662, 5649219, 5622687]
    recomendaciones = recomendar_productos_varios(productos_vistos)
    print("Productos recomendados:", recomendaciones)

# Análisis de clientes — Ecommerce (cosmética)

- **Generado:** 2026-03-29 23:51
- **Fuente:** `tablon_analitico.pickle`, eventos `purchase`; periodo hasta `2020-02-29`. 
- **Clientes con al menos una compra:** 11,040

## 1. Concentración del valor (Pareto)
- El **20 %** de clientes con mayor gasto (aprox. **2,208** clientes) concentran el **58.9 %** del gasto total.

## 2. Compradores de una sola vez vs repetidores
- **Una sola compra:** 1,130 clientes (10.2 % del universo); aportan **4.2 %** del gasto.
- **Repetidores (más de una compra):** 9,910 (89.8 %); aportan **95.8 %** del gasto.

## 3. Distribución del gasto y ticket por cliente
```
              gasto  precio_medio       compras
count  11040.000000  11040.000000  11040.000000
mean      56.299783      7.857346     11.554710
std       81.730979     11.847390     18.116884
min        0.130000      0.130000      1.000000
25%       16.220000      3.270000      3.000000
50%       32.740000      4.856863      6.000000
75%       60.305000      7.933333     13.000000
max     1559.210000    236.510000    506.000000
```

## 4. Recencia (días hasta fin de periodo)
- Media: **68.8** días | Mediana: **69.0**

## 5. Ventana primera–última compra (solo con >1 compra)
- Clientes con >1 compra: **9,910**; media de días entre primera y última: **12.5**

## 6. Diversidad de categorías (compras)
- Media de categorías distintas compradas por cliente: **5.79** | mediana: **4**

## 7. Fricción (eventos de carrito vs compras)
- Media de `cart` / compra: **2.91** | media de `remove_from_cart` / compra: **2.06**
  - *Interpretación:* valores altos sugieren exploración o abandono frecuente antes de cerrar la compra.

## 8. Compras en días especiales (flags del calendario)
- **10.7 %** de clientes tienen al menos una línea de compra en un día marcado por algún flag (festivo / campañas).

## 9. Cohortes por mes de primera compra
```
  cohorte_mes  n_clientes  pct_repiten_otro_mes
0     2019-10        2524                 31.42
1     2019-11        2640                 20.49
2     2019-12        1933                 12.78
3     2020-01        2089                  9.14
4     2020-02        1854                  0.00
```

- **pct_repiten_otro_mes:** % de clientes de esa cohorte con compras en **más de un mes distinto** (proxy de repetición en el tiempo).

## 10. Segmentación RFM simplificada (terciles)
```
                                    n_clientes
segmento_rfm                                  
Leales / potencial                        3843
Otros                                     2324
En riesgo (compraban, hace tiempo)        2324
Perdidos / dormidos                       1356
Campeones                                 1193
```

## 11. Cruce cuartiles: nº de compras (fila) × gasto (columna)
```
q_gasto      Q1    Q2    Q3    Q4
q_compras                        
Q1         1534   766   303   157
Q2          960  1034   565   201
Q3          257   819  1213   471
Q4            9   141   679  1931
```

## 12. Resumen para marketing
- Priorizar **retención y frecuencia** si el gasto está muy concentrado y muchos clientes son de una sola compra.
- Segmentos **en riesgo / perdidos** con recencia alta: campañas de **win-back** y ofertas temporales.
- Clientes con **muchas categorías** ya compradas: bundles y recomendaciones; con **poca diversidad**: cross-sell por categoría.
- Calibrar **promos en días especiales** según el % de clientes que ya compran en esas fechas (evitar canibalización).

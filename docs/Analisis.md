# Análisis de Clientes
Fecha de análisis: 2026-03-29 23:58:07

---

## 1. Distribución del Gasto Total de los Clientes

**Estadísticas descriptivas del gasto:**

```
count   11,040.00
mean        56.30
std         81.73
min          0.13
25%         16.22
50%         32.74
75%         60.30
max      1,559.21
Name: gasto, dtype: float64
```

**Percentiles del gasto:**

- Percentil 50: 32.74€
- Percentil 75: 60.30€
- Percentil 90: 121.28€
- Percentil 95: 188.89€
- Percentil 99: 393.95€

**Análisis de concentración (Pareto):**

- El top 10% de clientes genera el **42.44%** de los ingresos
- El top 20% de clientes genera el **58.93%** de los ingresos

## 2. Distribución del Número de Compras por Cliente

**Distribución de compras:**

```
compras
1     8697
2     1420
3      469
4      204
5       96
6       67
7       25
8       20
9       20
10       5
Name: count, dtype: int64
```

**Clientes según frecuencia de compra:**

- Clientes con 1 sola compra: **8697 (78.78%)**
- Clientes con múltiples compras: **2343 (21.22%)**
- Promedio de compras por cliente: **1.40**
- Máximo de compras de un cliente: **24**

## 3. Productos por Compra

**Estadísticas de productos por compra:**

```
count   11,040.00
mean         7.79
std          9.49
min          1.00
25%          3.00
50%          5.00
75%         10.00
max        219.00
Name: productos_por_compra, dtype: float64
```

- Promedio de productos por compra: **7.79**
- Mediana de productos por compra: **5.00**

## 4. Top 10 Clientes por Gasto Total

```
  usuario  compras  productos    gasto  productos_por_compra
573823111        2        268 1,559.21                134.00
539751397       13        236 1,453.37                 18.15
556579890        4        506 1,392.45                126.50
442763940        8        195 1,241.53                 24.38
561592095        3         94 1,109.70                 31.33
527739278       13        244 1,071.00                 18.77
527806771       13        195   948.01                 15.00
430220205        6        190   947.30                 31.67
491009486        1        219   946.20                219.00
520501669       11         64   913.01                  5.82
```

- Gasto total de los top 10: **11581.78€**
- Porcentaje del total: **1.86%**

## 5. Top 10 Clientes por Número de Productos Comprados

```
  usuario  compras  productos    gasto  precio_medio
556579890        4        506 1,392.45          2.75
573823111        2        268 1,559.21          5.82
514908450        5        262   695.65          2.66
527739278       13        244 1,071.00          4.39
492650335       18        243   904.53          3.72
539751397       13        236 1,453.37          6.16
414659837        9        235   791.02          3.37
491009486        1        219   946.20          4.32
233280499       11        200   858.26          4.29
442763940        8        195 1,241.53          6.37
```

## 6. Ticket Medio por Cliente

**Estadísticas del ticket medio:**

```
count   11,040.00
mean        38.94
std         45.17
min          0.13
25%         15.06
50%         27.25
75%         47.08
max        946.20
Name: ticket_medio, dtype: float64
```

## 7. Análisis de Recencia (Última Compra)

**Estadísticas de recencia:**

```
count   11,040.00
mean        68.84
std         43.82
min          0.00
25%         30.00
50%         69.00
75%        104.00
max        151.00
Name: dias_desde_ultima_compra, dtype: float64
```

**Segmentación por recencia:**

- Clientes recientes (≤30 días): **2793 (25.30%)**
- Clientes medios (31-60 días): **2264 (20.51%)**
- Clientes antiguos (>60 días): **5983 (54.19%)**

## 8. Precio Medio por Producto

**Estadísticas del precio medio:**

```
count   11,040.00
mean         7.86
std         11.85
min          0.13
25%          3.27
50%          4.86
75%          7.93
max        236.51
Name: precio_medio, dtype: float64
```

**Top 10 clientes con mayor precio medio:**

```
  usuario  compras  productos  precio_medio  gasto
563937324        1          1        236.51 236.51
565425110        1          1        207.94 207.94
449277841        1          1        194.44 194.44
502570858        1          1        194.44 194.44
607099500        1          1        194.44 194.44
610912818        1          1        194.44 194.44
570639042        1          1        188.60 188.60
605032385        2          2        187.69 375.39
484947930        1          1        187.30 187.30
600055095        1          1        187.30 187.30
```

## 9. Correlaciones entre Variables

**Matriz de correlación:**

```
                      compras  productos  gasto  precio_medio  \
compras                  1.00       0.62   0.61         -0.07   
productos                0.62       1.00   0.84         -0.16   
gasto                    0.61       0.84   1.00          0.12   
precio_medio            -0.07      -0.16   0.12          1.00   
productos_por_compra     0.06       0.69   0.53         -0.20   

                      productos_por_compra  
compras                               0.06  
productos                             0.69  
gasto                                 0.53  
precio_medio                         -0.20  
productos_por_compra                  1.00  
```

**Correlación entre compras y gasto: 0.611**

## 10. Tasa de Retención de Clientes

- Tasa de retención (clientes con >1 compra): **21.22%**
- Clientes que NO volvieron a comprar: **78.78%**

---

## Resumen de Insights Clave

1. **Concentración de ingresos**: El top 10% de clientes genera el 42.44% de los ingresos
2. **Retención baja**: Solo el 21.22% de los clientes realizan más de una compra
3. **Ticket medio**: 38.94€ por compra
4. **Productos por compra**: 7.79 productos de media
5. **Recencia**: 25.30% de clientes compraron en los últimos 30 días

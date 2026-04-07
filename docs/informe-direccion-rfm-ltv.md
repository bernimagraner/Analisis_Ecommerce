# Informe ejecutivo: segmentación RFM, LTV y prioridades CRO

**Contexto:** ecommerce cosmética · análisis sobre datos transaccionales del notebook de trabajo  
**Audiencia:** Dirección  
**Objetivo del proyecto:** incrementar visitas, conversión y ticket medio mediante insights y activos analíticos (RFM, cohortes, LTV), alineado con [`proyecto-objetivos.md`](proyecto-objetivos.md).

---

## Resumen para dirección

| Indicador | Valor | Lectura |
|-----------|-------|---------|
| Clientes analizados | **11.040** | Base transaccional consolidada |
| Gasto medio por cliente | **56,30 €** | Alta dispersión (cola larga de VIP) |
| Mediana de gasto | **32,74 €** | Más representativo que la media para “cliente típico” |
| Clientes con una sola compra | **~78,8 %** (F=1) | Principal fuga de valor; prioridad recurrencia |
| Concentración ingresos (aprox.) | **~10 % clientes → ~42 % ingresos** | Dependencia de minoría de alto valor |
| LTV a 3 meses (referencia cohorte) | **Mediana ~31 €** | Techo razonable de CPA para adquisición |
| Retención cohorte (insight) | **~90 % no activos al mes 2** | Urgencia en onboarding post–1ª compra |

**Versión con gráficos interactivos y bloques HTML de conclusiones:** abrir en el navegador  
[`informe-direccion-rfm-ltv.html`](informe-direccion-rfm-ltv.html) (misma información, formato presentación).

---

## 1. Marco: las tres palancas de crecimiento

Alineado con el marco del proyecto, solo hay tres formas de crecer: más clientes, más frecuencia, mayor ticket medio. Los datos muestran que **la frecuencia es el cuello de botella principal** (mayoría one-shot), mientras que **el valor monetario está muy concentrado** en pocos segmentos.

---

## 2. Segmentación RFM (síntesis)

### Recency (R) — días desde última compra

| R | Clientes (%) | % ingresos | Lectura |
|---|--------------|------------|---------|
| 5 (0–24 d) | 20,63 | **30,62** | Más recientes arrastran el P&L |
| 4 | 19,57 | 20,77 | |
| 3 | 20,24 | 17,62 | |
| 2 | 19,95 | 16,64 | |
| 1 (114–151 d) | 19,61 | 14,35 | En riesgo; reactivación prioritaria |

**Conclusión:** ~40 % de ingresos proviene de clientes con compra en las últimas ~7 semanas (R 4–5). La mitad de la base está en R 1–3: hay margen de campañas de **reactivación** sin competir con la adquisición fría.

### Frequency (F) — número de compras

| F | Clientes (%) | % ingresos | Compras medias |
|---|--------------|------------|----------------|
| 1 | **78,78** | 53,28 | 1,00 |
| 3 | 17,11 | 28,22 | 2,25 |
| 5 | 4,11 | 18,50 | 5,52 |

**Conclusión:** Casi **4 de 5 clientes son “una sola compra”**. El crecimiento sostenible pasa por **segunda compra en 30–60 días** y programas de fidelización, no solo descuentos genéricos.

### Monetary (M) — gasto acumulado

| M | Clientes (%) | % ingresos | Gasto medio (€) |
|---|--------------|------------|-----------------|
| 5 | 19,99 | **58,92** | ~165,94 |
| 4 | 20,01 | 19,09 | ~53,70 |
| 3 | 19,98 | 11,71 | ~32,98 |
| 2 | 19,92 | 6,74 | ~19,04 |
| 1 | 20,10 | 3,55 | ~9,94 |

**Conclusión:** El quintil superior (M=5) concentra **casi 6 de cada 10 euros** con solo **1 de cada 5 clientes**. Políticas comerciales y CRM deben **diferenciar fuertemente** alto valor vs. cola.

### Valor RFM agregado (R+F+M, 3–15)

Agrupación usada en el análisis:

| Segmento | % clientes | % ingresos |
|----------|------------|------------|
| **Alto (valor ≥ 12)** | 9,87 | 31,91 |
| **Medio (8–11)** | 33,61 | **41,69** |
| **Bajo (< 8)** | 56,52 | 26,40 |

**Conclusión:** El “medio” concentra el mayor % de facturación con un tercio de la base: son el **objetivo principal de upsell y segunda compra**. Los de valor alto son pocos pero críticos para margen y advocacy. Los de valor bajo son volumen: **reactivación barata** o win-back por email.

---

## 3. LTV (3 meses) y reglas de inversión en marketing

- **LTV3M mediano ~31 €** (cohorte analizada en el notebook).  
- Variabilidad alta (medias ~49–51 € según cohorte): conviene planificar en **medianas y percentiles**, no solo en media.  
- **Implicación:** con LTV3M ~31 €, un **CPA sostenible** debería situarse con holgura por debajo (orden **10–15 €** como referencia prudente), salvo que se demuestre LTV a 6–12 meses mayor.  
- **Recomendación de datos:** ampliar histórico para **LTV6M / LTV12M** y calibrar presupuestos de paid media y retención.

---

## 4. Métricas complementarias sugeridas (tablero de dirección)

| Métrica | Para qué sirve |
|---------|----------------|
| **Segunda compra en 30/60/90 d** | Medir si las palancas de fidelización funcionan |
| **% ingresos de top 10 % / 1 %** | Vigilar concentración y riesgo |
| **Tiempo entre compras (IPT)** | Segmentar churn temprano |
| **AOV por segmento RFM** | Desacoplar estrategias de ticket vs. frecuencia (coherente con correlaciones del análisis) |
| **CAC por canal vs. LTV** | Evitar canibalizar margen en adquisición |

---

## 5. Plan de acciones priorizado (resumen)

1. **Fidelización post–1ª compra** (reduce el 78 % one-shot): flujos email/SMS, beneficio en 2ª compra, contenido de uso del producto.  
2. **Segmento “valor medio” (RFM 8–11):** motor de ingresos; pruebas A/B de bundles, cross-sell y recomendaciones.  
3. **VIP (alto M y alto valor RFM):** servicio preferente, early access, cohortes de margen.  
4. **R bajo (inactivos):** campañas de win-back con coste controlado; evitar descuentos agresivos a alto M histórico sin reglas.  
5. **Inversión en adquisición:** capar CPA según LTV3M y roadmap hacia LTV12M.  
6. **Datos:** unificar vista cliente + seguimiento cohortes mensual para decidir presupuesto.

---

*Fuentes: [`docs/proyecto-objetivos.md`](proyecto-objetivos.md), salidas del notebook `notebooks/02_AnalisisInsights.ipynb` (RFM, LTV3M, insights de clientes y cohortes).*

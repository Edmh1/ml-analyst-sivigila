# ml-analyst-sivigila

Análisis exploratorio y modelado de datos epidemiológicos del sistema SIVIGILA (Colombia), enfocado en detectar patrones, tendencias y posibles predicciones de enfermedades como el dengue en relación con variables ambientales y temporales.

---

## 📊 1. Objetivo del proyecto

Este proyecto busca aplicar técnicas de **análisis exploratorio de datos (EDA)** y **machine learning** sobre reportes del sistema **SIVIGILA**, con el fin de:

- Explorar la evolución temporal de enfermedades notificadas.  
- Probar modelos predictivos para anticipar comportamientos futuros.  
- Visualizar tendencias que apoyen la toma de decisiones en salud pública.  

---

## 🧱 2. Estructura del repositorio

```bash
ml-analyst-sivigila/
│
|-- data/                  # Conjuntos de datos
│   |-- raw/               # Datos originales (sin procesar)
│   |-- processed/         # Datos limpios o transformados
│   
│
|-- notebooks/             # Análisis paso a paso
│   |-- 01_EDA.ipynb
│   |-- 02_Limpieza.ipynb
│
|-- src/                   # Código fuente modular
│   |-- data_preprocessing.py
│   |-- visualization.py
│   |-- models/
│
|-- reports/               # Resultados, gráficos y reportes
│   |-- figures/
│   |-- summaries/
│
|-- requirements.txt       # Librerías necesarias
|-- README.md

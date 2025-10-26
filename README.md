# ml-analyst-sivigila (DENGUE 2022-2024)

Análisis exploratorio y modelado de datos epidemiológicos del sistema SIVIGILA (Colombia) centrado en la patologia DENGUE en el periodo de 2022-2024, enfocado en detectar patrones, tendencias y posibles predicciones de enfermedades como el dengue.

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
|
|-- data/                  # Conjuntos de datos
|   |-- raw/               # Datos originales (sin procesar)
|   |-- processed/         # Datos limpios o transformados
|   
|-- notebooks/             # Análisis paso a paso
|   |-- main_pipeline.ipynb
|
|-- src/                   # Código fuente modular
|   |-- data_utils.py
|   |-- visualization_utils.py
|
|-- reports/               # Articulos
|
|-- requirements.txt       # Librerías necesarias
|-- README.md

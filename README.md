# ml-analyst-sivigila (DENGUE 2022-2024)

Análisis exploratorio y modelado de datos epidemiológicos del sistema SIVIGILA (Colombia) centrado en la patologia DENGUE en el periodo de 2022-2024, enfocado en detectar patrones, tendencias y posibles predicciones de enfermedades como el dengue.

---

## 1. Objetivo del proyecto

Este proyecto busca aplicar técnicas de **análisis exploratorio de datos (EDA)** y **machine learning** sobre reportes del sistema **SIVIGILA**, con el fin de:

- Explorar la evolución temporal de enfermedades notificadas.  
- Probar modelos predictivos para anticipar comportamientos futuros.  
- Visualizar tendencias que apoyen la toma de decisiones en salud pública.  

---

## 2. Estructura del repositorio

```bash
ml-analyst-sivigila/
|
|-- data/                  # Conjuntos de datos
|   |-- raw/               # Datos originales (sin procesar)
|   |-- processed/         # Datos limpios o transformados
|   |-- parquet/           # Datos en formato parquet.
|   
|-- notebooks/             # Análisis paso a paso
|   |-- main_pipeline.ipynb
|
|-- src/                   # Código fuente modular
|   |-- data_utils.py
|   |-- visualization_utils.py
|
|-- references/            # Articulos y Referencias
|
|-- reports/               # Reportes
|
|-- requirements.txt       # Librerías necesarias
|-- README.md
```

## 3. Cómo replicar el proyecto

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

###  **3.0 Requisitos previos**

Asegúrate de tener instalado:

- **Python 3.10 o superior**
- **Git**
- Un gestor de entornos:
  - `venv` (incluido en Python)
---

### **3.1 Clonar el repositorio**

```bash
git clone https://github.com/tu_usuario/ml-analyst-sivigila.git
cd ml-analyst-sivigila
```

---

###  **3.2. Crear y activar el entorno virtual**

#### Windows (PowerShell)
```bash
python -m venv venv
.\venv\Scripts\activate
```

#### Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### **3.3 Instalar dependencias**

```bash
pip install -r requirements.txt
```

---


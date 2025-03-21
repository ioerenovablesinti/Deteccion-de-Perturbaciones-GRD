# Detección de Perturbaciones en RE-GRD

## Descripción
Este proyecto implementa un sistema para analizar, detectar y predecir perturbaciones en redes eléctricas de una PyME ubicada en AMBA.

## Estructura del Proyecto
Proyecto_Redes
│── src/                           # Código fuente principal
│   │── main.py                    # Orquestador del flujo principal
│   │── config.py                  # Configuración global
│   │── db/                         # Módulos para conexión a bases de datos
│   │   │── db_connector.py         # Conexión y consultas a InfluxDB
│   │── data_processing/            # Procesamiento y transformación de datos
│   │   │── data_cleaning.py        # Limpieza de datos y detección de outliers
│   │   │── data_merging.py         # Combinación y fusión de DataFrames
│   │   │── normalization.py        # Normalización y transformación de datos
│   │── models/                     # Modelos de predicción y análisis
│   │   │── modeling.py             # Modelos de predicción (RNN, Fourier, etc.)
│   │   │── trend_analysis.py       # Análisis de tendencias
│   │   │── event_detection.py      # Algoritmos de detección de eventos
│   │── visualization/              # Visualización de datos
│   │   │── visualization.py        # Gráficos con Matplotlib y Seaborn
│   │── utils.py                    # Funciones auxiliares reutilizables
│
│── data/                           # Almacenamiento de datos
│   │── raw/                        # Datos sin procesar
│   │── processed/                   # Datos limpios
│   │── models/                      # Modelos entrenados
│   │── reports/                     # Reportes generados
│
│── notebooks/                      # Pruebas en Jupyter Notebook
│── tests/                          # Pruebas unitarias
│── resources/                       # Bibliografía, manuales y normativas
│   │── papers/                      # Artículos científicos
│   │── manuals/                     # Manuales técnicos
│   │── standards/                   # Normativas (IEEE, ASTM, etc.)
│
│── requirements.txt                 # Dependencias
│── .gitignore                        # Archivos a ignorar en Git
│── README.md                         # Documentación general

## 🚀 Instalación
Clonar el repositorio:

```
git clone https://github.com/USUARIO/Deteccion-de-Perturbaciones-GRD.git
cd Deteccion-de-Perturbaciones-GRD`
```

## 🛠 Tecnologías Utilizadas
- Python 3.9+
- InfluxDB 1.8 & 2.7
- Grafana
- Bertual
- Machine Learning (RNN)
- Pandas, NumPy, Matplotlib

## 📚 Recursos y Bibliografía
Los manuales y papers relevantes están en la carpeta resources/.

---

📌 Autor: [Tu Nombre]
📅 Última actualización: [Fecha]


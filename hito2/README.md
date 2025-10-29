# Hito 2

**Integrantes:** Carlos Duarte, Fernando Castillo, Vicente Alves, Antonio Duque

## Avances realizados

- **Implementación de funciones:** Generación de señales de prueba (aplauso sintético, barrido senoidal), carga de audio y procesamiento de respuestas al impulso.
- **Convolución FFT:** Implementación funcional con normalización automática.
- **Librería de IRs:** Creación de respuestas al impulso sintéticas con `pyroomacoustics` (salas pequeña, mediana, grande y un modelo escalonado en desarrollo).
- **Análisis y visualización:** Espectrogramas y comparaciones visuales de señales procesadas.
- **Filtros básicos:** Implementación de filtros con `scipy.signal`.
- **Exportación:** Funcionalidad para poder guardar los resultados en formato WAV.

## Pendiente para el hito 3

- Validación del modelo escalonado vs. grabaciones reales del efecto Quetzal.
- Refinamiento de parámetros de las IRs sintéticas para mayor realismo y precisión.
- Visualización 3D.
- Documentación final y limpieza del código.

## Instrucciones para ejecutar el notebook

1. Crear el entorno conda:
   ```bash
   conda env create -f hito2/environment.yml
   conda activate acustica
   ```

2. Abrir jupyter y ejecutar el notebook (o alternativamente abrir el archivo en VS Code):
   ```bash
   jupyter lab
   ```

## Estructura de archivos
```
hito2/
├── data/
│   ├── inputs/               # Audio de entrada
│   └── outputs/              # Audio procesado
├── environment.yml           # Entorno conda para el hito 2
├── HITO2_INSTRUCCIONES.md
├── README.md
└── test.ipynb                # Notebook de avances del hito 2
```


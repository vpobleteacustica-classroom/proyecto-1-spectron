<p align="center">
  <img src="../data/uach.png" alt="UACh" width="180">
</p>

# Hito 3 - Entrega Final

**Integrantes:** 
- Vicente Alves
- Fernando Castillo
- Carlos Duarte
- Antonio Duque

## Descripción

Este hito corresponde a la entrega final del proyecto de ACUS220 - Acústica Computacional con Python. Se presenta un prototipo interactivo de convolución que permite explorar el fenómeno del "eco del quetzal" de la Pirámide de Kukulkán y otras configuraciones de salas acústicas.

## Funcionalidades implementadas

- **Interfaz interactiva con Gradio:** Demo visual para experimentar con distintas señales y respuestas al impulso.
- **Señales de entrada configurables:** Aplauso sintético, barrido senoidal, o audio personalizado (cargar un audio desde el computador).
- **Presets de respuestas al impulso (IR):**
  - Sala pequeña
  - Sala mediana
  - Sala grande / Hall
  - Pirámide (Quetzal)
- **Cargar IRs personalizadas:** Posibilidad de subir archivos de respuesta al impulso propios.
- **Filtros de post-procesamiento:** Pasa-bajos, pasa-altos y pasa-banda con frecuencias configurables.
- **Visualización:** Formas de onda y espectrogramas de la señal de salida.
- **Exportación:** Descarga de resultados en formato WAV.

## Instrucciones para ejecutar el notebook

1. Crear el entorno conda:
   ```bash
   conda env create -f hito3/environment.yml
   conda activate acustica
   ```

2. Abrir Jupyter y ejecutar el notebook:
   ```bash
   jupyter notebook
   ```

3. Ejecutar todas las celdas del notebook `Hito3.ipynb` para cargar la demo en Gradio.

4. Hacer clic en el link generado al ejecutar la ultima celda del notebook para poder ver la demo en una pestaña nueva del navegador y así tener una experiencia de usuario más cómoda.

## Estructura de archivos

```
hito3/
├── data/
│   ├── inputs/               # Audio de entrada
│   └── outputs/              # Audio procesado
├── environment.yml           # Entorno conda para el hito 3
├── Hito3.ipynb               # Notebook principal con la demo
└── README.md                 # Este archivo
```
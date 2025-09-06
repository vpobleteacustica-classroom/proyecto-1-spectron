[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/2v3aT_hm)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=20160252&assignment_repo_type=AssignmentRepo)

# Instalar 

conda env create -f environment.yml

# acus220_primavera_2025
Organización de proyectos a desarrollar en el semestre

acustica/
│── README.md                # Explicación del proyecto
│── environment.yml           # Tu archivo de entorno conda
│── docs/                     # Documentación y papers relacionados
│── notebooks/                # Jupyter Notebooks para prototipos
│── src/                      # Código fuente en Python
│   ├── __init__.py
│   ├── convolution.py        # Funciones para convolución de señales
│   ├── transform.py          # Función matemática para "mapear" un sonido en otro
│   ├── acoustics3d.py        # Modelado de materiales y geometría (pyroomacoustics)
│── data/
│   ├── inputs/               # Sonidos de entrada (ej. aplauso, lluvia, voz, etc.)
│   ├── responses/            # Impulse responses o kernels
│   ├── outputs/              # Resultados procesados
│── tests/                    # Pruebas unitarias

# Proyecto Acústica – Convolución y Modelado 3D

Este proyecto busca replicar fenómenos acústicos como el de la Pirámide de Chichén Itzá, donde un aplauso se transforma en el canto de un pájaro debido a la geometría y materiales de la estructura.

### Objetivos:
1. Resolver matemáticamente la función de transformación de un sonido en otro mediante convolución.
2. Modelar en 3D una estructura que reproduzca ese efecto acústico.

### Tecnologías:
- Python (numpy, scipy, matplotlib)
- Pyroomacoustics (simulación acústica)
- PyVista / Trimesh (modelado 3D)
- Soundfile (manejo de audio)

### Ejemplo de uso (prototipo):
```python
import soundfile as sf
from src.convolution import apply_convolution

# Cargar sonido de entrada y respuesta al impulso
x, fs = sf.read("data/inputs/aplauso.wav")
h, _ = sf.read("data/responses/piramide_ir.wav")

# Aplicar convolución
y = apply_convolution(x, h, fs)
sf.write("data/outputs/aplauso_pajaro.wav", y, fs)

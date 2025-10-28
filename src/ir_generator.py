"""
Generador de respuestas al impulso (IR)
ACUS 220 - Hito 2
"""

import numpy as np
import pyroomacoustics as pra



def simulate_room_ir(sr, room_dim, absorption, max_order, 
                     src_pos, mic_pos, ir_length_s=1.5):
    """
    Genera IR de una sala usando pyroomacoustics
    
    Parameters:
    -----------
    sr : int
        Frecuencia de muestreo
    room_dim : tuple
        Dimensiones de la sala (x, y, z) en metros
    absorption : float
        Coeficiente de absorción (0-1)
    max_order : int
        Orden máximo de reflexiones
    src_pos : tuple
        Posición de la fuente (x, y, z)
    mic_pos : tuple
        Posición del micrófono (x, y, z)
    ir_length_s : float
        Duración de la IR en segundos
    
    Returns:
    --------
    ir : array
        Respuesta al impulso normalizada
    """
    from audio_utils import normalize_audio

    
    # Crear sala con materiales
    materials = pra.Material(absorption)
    room = pra.ShoeBox(room_dim, fs=sr, materials=materials, max_order=max_order)
    
    # Agregar fuente y micrófono
    room.add_source(src_pos)
    mic_locs = np.array(mic_pos).reshape(3, 1)
    room.add_microphone_array(pra.MicrophoneArray(mic_locs, room.fs))
    
    # Calcular IR
    room.compute_rir()
    ir = np.asarray(room.rir[0][0], dtype=float)
    
    # Ajustar longitud
    N = int(sr * ir_length_s)
    if len(ir) < N:
        ir_padded = np.zeros(N)
        ir_padded[:len(ir)] = ir
        ir = ir_padded
    else:
        ir = ir[:N]
    
    return normalize_audio(ir)


def generate_preset_rooms(sr=48000):
    """
    Genera las 3 IRs de salas predefinidas
    
    Parameters:
    -----------
    sr : int
        Frecuencia de muestreo
    
    Returns:
    --------
    irs : dict
        Diccionario con las IRs de cada sala
    metadata : dict
        Información sobre cada sala
    """
    irs = {}
    metadata = {}
    
    # Sala Pequeña: 5×4×3 m
    print("Generando IR: Sala Pequeña...")
    irs['sala_pequena'] = simulate_room_ir(
        sr=sr,
        room_dim=(5.0, 4.0, 3.0),
        absorption=0.45,
        max_order=10,
        src_pos=(2.5, 2.0, 1.5),
        mic_pos=(1.0, 2.0, 1.5),
        ir_length_s=1.2
    )
    metadata['sala_pequena'] = {
        'nombre': 'Sala Pequeña',
        'dimensiones': '5×4×3 m',
        'volumen': 60,
        'absorcion': 0.45,
        'color': '#A23B72'
    }
    
    # Sala Mediana: 10×8×4 m
    print("Generando IR: Sala Mediana...")
    irs['sala_mediana'] = simulate_room_ir(
        sr=sr,
        room_dim=(10.0, 8.0, 4.0),
        absorption=0.25,
        max_order=15,
        src_pos=(5.0, 4.0, 2.0),
        mic_pos=(2.0, 4.0, 2.0),
        ir_length_s=1.5
    )
    metadata['sala_mediana'] = {
        'nombre': 'Sala Mediana',
        'dimensiones': '10×8×4 m',
        'volumen': 320,
        'absorcion': 0.25,
        'color': '#F18F01'
    }
    
    # Sala Grande / Hall: 20×15×8 m
    print("Generando IR: Sala Grande (Hall)...")
    irs['sala_grande'] = simulate_room_ir(
        sr=sr,
        room_dim=(20.0, 15.0, 8.0),
        absorption=0.12,
        max_order=20,
        src_pos=(10.0, 7.5, 2.5),
        mic_pos=(5.0, 7.5, 2.5),
        ir_length_s=2.0
    )
    metadata['sala_grande'] = {
        'nombre': 'Sala Grande / Hall',
        'dimensiones': '20×15×8 m',
        'volumen': 2400,
        'absorcion': 0.12,
        'color': '#C73E1D'
    }
    
    print("✓ IRs generadas correctamente\n")
    return irs, metadata


def calculate_rt60(ir, sr):
    """
    Calcula el tiempo de reverberación RT60
    
    Parameters:
    -----------
    ir : array
        Respuesta al impulso
    sr : int
        Frecuencia de muestreo
    
    Returns:
    --------
    rt60 : float
        Tiempo de reverberación en segundos
    """
    # Calcular energía
    energy = ir**2
    energy_db = 10 * np.log10(energy / np.max(energy) + 1e-10)
    
    try:
        # Buscar puntos -5dB y -35dB
        idx_5 = np.where(energy_db < -5)[0][0]
        idx_35 = np.where(energy_db < -35)[0][0]
        rt30 = (idx_35 - idx_5) / sr
        rt60 = 2 * rt30  # Extrapolación
        return rt60
    except:
        return 0.0
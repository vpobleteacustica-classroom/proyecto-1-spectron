"""
Funciones de visualización
ACUS 220 - Hito 2
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Configuración global de matplotlib
plt.rcParams['figure.figsize'] = (12, 5)
plt.rcParams['font.size'] = 10


def plot_waveform(x, sr, title='Forma de onda', color='#2E86AB'):
    """Grafica forma de onda temporal"""
    t = np.arange(len(x)) / sr
    plt.figure(figsize=(12, 4))
    plt.plot(t, x, color=color, linewidth=0.8)
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_spectrogram(x, sr, title='Espectrograma'):
    """Grafica espectrograma"""
    f, t, Sxx = signal.spectrogram(x, fs=sr, nperseg=1024, 
                                    noverlap=512, scaling='spectrum')
    Sxx_db = 10 * np.log10(Sxx + 1e-12)
    
    plt.figure(figsize=(12, 5))
    plt.pcolormesh(t, f, Sxx_db, shading='auto', cmap='magma')
    plt.ylabel('Frecuencia [Hz]')
    plt.xlabel('Tiempo [s]')
    plt.ylim(0, min(sr/2, 12000))
    plt.colorbar(label='Magnitud [dB]')
    plt.title(title)
    plt.tight_layout()
    plt.show()


def plot_spectrum(x, sr, title='Espectro de Magnitud', color='#2E86AB'):
    """Grafica espectro de magnitud"""
    n_fft = 4096
    freqs = np.fft.rfftfreq(n_fft, 1/sr)
    spectrum = np.abs(np.fft.rfft(x, n=n_fft))
    spectrum_db = 20 * np.log10(spectrum + 1e-10)
    
    plt.figure(figsize=(12, 4))
    plt.plot(freqs, spectrum_db, color=color, linewidth=1)
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Magnitud [dB]')
    plt.title(title)
    plt.xlim(20, min(sr/2, 20000))
    plt.xscale('log')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_comparison_waveforms(signals_dict, sr, colors_dict=None):
    """
    Grafica comparación de múltiples señales
    
    Parameters:
    -----------
    signals_dict : dict
        Diccionario {nombre: señal}
    sr : int
        Frecuencia de muestreo
    colors_dict : dict, optional
        Diccionario {nombre: color}
    """
    n_signals = len(signals_dict)
    fig, axes = plt.subplots(n_signals, 1, figsize=(14, 3*n_signals), sharex=True)
    
    if n_signals == 1:
        axes = [axes]
    
    for idx, (nombre, audio) in enumerate(signals_dict.items()):
        t = np.arange(len(audio)) / sr
        color = colors_dict.get(nombre, '#2E86AB') if colors_dict else '#2E86AB'
        
        axes[idx].plot(t, audio, color=color, linewidth=0.8)
        axes[idx].set_ylabel('Amplitud')
        axes[idx].set_title(nombre, fontweight='bold')
        axes[idx].grid(True, alpha=0.3)
    
    axes[-1].set_xlabel('Tiempo [s]')
    plt.tight_layout()
    plt.show()


def plot_comparison_spectrograms(signals_dict, sr):
    """Grafica comparación de espectrogramas"""
    n_signals = len(signals_dict)
    fig, axes = plt.subplots(n_signals, 1, figsize=(14, 3.5*n_signals))
    
    if n_signals == 1:
        axes = [axes]
    
    for idx, (nombre, audio) in enumerate(signals_dict.items()):
        f, t, Sxx = signal.spectrogram(audio, fs=sr, nperseg=1024, noverlap=512)
        Sxx_db = 10 * np.log10(Sxx + 1e-12)
        
        im = axes[idx].pcolormesh(t, f, Sxx_db, shading='auto', cmap='magma')
        axes[idx].set_ylabel('Frecuencia [Hz]')
        axes[idx].set_title(nombre, fontweight='bold')
        axes[idx].set_ylim(0, 12000)
        plt.colorbar(im, ax=axes[idx], label='dB')
    
    axes[-1].set_xlabel('Tiempo [s]')
    plt.tight_layout()
    plt.show()


def plot_edc(ir, sr, title='Energy Decay Curve'):
    """Grafica la curva de decaimiento de energía"""
    energy = ir**2
    edc = np.cumsum(energy[::-1])[::-1]
    edc_db = 10 * np.log10(edc / np.max(edc) + 1e-10)
    tiempo = np.arange(len(ir)) / sr
    
    plt.figure(figsize=(12, 5))
    plt.plot(tiempo, edc_db, linewidth=2, color='#2E86AB')
    plt.axhline(y=-60, color='red', linestyle='--', alpha=0.5, label='RT60 (-60dB)')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Energía [dB]')
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.ylim(-80, 5)
    plt.tight_layout()
    plt.show()
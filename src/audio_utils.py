"""
Utilidades de procesamiento de audio
ACUS 220 - Hito 2
"""

import numpy as np
from scipy import signal
import soundfile as sf
from IPython.display import Audio, display

def normalize_audio(x, peak=0.98):
    x = np.asarray(x, dtype=float)
    max_val = np.max(np.abs(x)) + 1e-12
    return (x / max_val) * peak


def make_synthetic_clap(sr=48000, duration=0.3, decay=10.0):
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)
    clap = np.random.randn(len(t)) * np.exp(-decay * t)
    return normalize_audio(clap)


def convolve_fft(x, ir, normalize=True):
    y = signal.fftconvolve(x, ir, mode='full')
    if normalize:
        y = normalize_audio(y, peak=0.98)
    return y


def play_audio(x, sr):
    display(Audio(x, rate=sr))


def save_audio(filepath, x, sr):
    sf.write(filepath, x, sr)
    print(f"✓ Guardado: {filepath}")


def load_audio(filepath, sr=None):
    x, sr_original = sf.read(filepath)
    if sr is not None and sr != sr_original:
        # Resamplear si es necesario
        from scipy.signal import resample_poly
        gcd = np.gcd(sr, sr_original)
        x = resample_poly(x, sr // gcd, sr_original // gcd)
        return x, sr
    return x, sr_original


def calculate_rms(x):
    return np.sqrt(np.mean(x**2))


def calculate_peak(x):
    return np.max(np.abs(x))
"""
Paquete de utilidades para ACUS 220 - Hito 2
"""

from .audio_utils import (
    normalize_audio,
    make_synthetic_clap,
    convolve_fft,
    play_audio,
    save_audio,
    load_audio,
    calculate_rms,
    calculate_peak
)

from .ir_generator import (
    simulate_room_ir,
    generate_preset_rooms,
    calculate_rt60
)

from .visualization import (
    plot_waveform,
    plot_spectrogram,
    plot_spectrum,
    plot_comparison_waveforms,
    plot_comparison_spectrograms,
    plot_edc
)

__all__ = [
    'normalize_audio',
    'make_synthetic_clap',
    'convolve_fft',
    'play_audio',
    'save_audio',
    'load_audio',
    'calculate_rms',
    'calculate_peak',
    'simulate_room_ir',
    'generate_preset_rooms',
    'calculate_rt60',
    'plot_waveform',
    'plot_spectrogram',
    'plot_spectrum',
    'plot_comparison_waveforms',
    'plot_comparison_spectrograms',
    'plot_edc'
]
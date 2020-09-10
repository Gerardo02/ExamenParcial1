import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

#697Hz + 1477Hz
frecuencia3 = SinSignal(freq=697, amp=1, offset=0)
frecuencia32 = SinSignal(freq=1477, amp=1, offset=0)
#852Hz + 1209Hz
frecuencia7 = SinSignal(freq=852, amp=1, offset=0)
frecuencia72 = SinSignal(freq=1209, amp=1, offset=0)

wave_prueba = frecuencia3.make_wave(duration=0.5, start=0, framerate=44100)
wave_prueba2 = frecuencia32.make_wave(duration=0.5, start=0, framerate=44100)

sonido3 = wave_prueba + wave_prueba2

wave_prueba3 = frecuencia7.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_prueba4 = frecuencia72.make_wave(duration=0.5, start=0.5, framerate=44100)

wave_prueba5 = frecuencia3.make_wave(duration=0.5, start=1.0, framerate=44100)
wave_prueba6 = frecuencia32.make_wave(duration=0.5, start=1.0, framerate=44100)

wave_prueba7 = frecuencia3.make_wave(duration=0.5, start=1.5, framerate=44100)
wave_prueba8 = frecuencia32.make_wave(duration=0.5, start=1.5, framerate=44100)

sonido7 = wave_prueba3 + wave_prueba4

sonido32 = wave_prueba5 + wave_prueba6
sonido33 = wave_prueba7 + wave_prueba8

sonido4 = sonido3 + sonido7 + sonido32 + sonido33

sonido4.write("output.wav")

import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate


frecuencia3 = SinSignal(freq=697, amp=1, offset=0)
frecuencia7 = SinSignal(freq=852, amp=1, offset=0)
frecuencia32 = SinSignal(freq=697, amp=1, offset=0)
frecuencia33 = SinSignal(freq=697, amp=1, offset=0)

wave_697 = frecuencia3.make_wave(duration=0.5, start=0, framerate=44100)
wave_852 = frecuencia7.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_697_2 = frecuencia32.make_wave(duration=0.5, start=1.0, framerate=44100)
wave_697_3 = frecuencia33.make_wave(duration=0.5, start=1.5, framerate=44100)

wave_sonido = wave_697 + wave_852 + wave_697_2 + wave_697_3

wave_sonido.write("output.wav")
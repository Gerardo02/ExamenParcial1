import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

#697Hz + 1477Hz
frecuencia3 = SinSignal(freq=2174, amp=1, offset=0)

#852Hz + 1209Hz
frecuencia7 = SinSignal(freq=2061, amp=1, offset=0)



wave_2174 = frecuencia3.make_wave(duration=0.5, start=0, framerate=44100)
wave_2061 = frecuencia7.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_2174_2 = frecuencia3.make_wave(duration=0.5, start=1.0, framerate=44100)
wave_2174_3 = frecuencia3.make_wave(duration=0.5, start=1.5, framerate=44100)

wave_sonido = wave_2174 + wave_2061 + wave_2174_2 + wave_2174_3

wave_sonido.write("output.wav")
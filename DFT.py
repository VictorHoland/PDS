import numpy as np
import matplotlib.pyplot as plt
from numpy import  pi
import time
from scipy import signal

def e(n):
    return complex(np.cos(n),np.sin(n))

def dft(x_n):
    fourier = []
    N = len(x_n)
    for k in range(N):
        aux = 0
        for n in range(N):
            aux += x_n[n] * e(-2*np.pi * k * n/N)
        fourier.append(aux)
    return fourier

Fs= 1000         # Frequência de amostragem em Hz
Ts=1/Fs              # Intervalo de amostragem em Hz
duration = 500      # Duração do gráfico em ms
t=np.arange(0, duration/1000,Ts)
#t = np.linspace(0,0.5,duration)

#print('duration{}'. format(duration))
f=40                  # Frequência de sinal
A=1                   # Amplitude
f2=90                 
A2=0.5

#x_t = (1,2,3,4)
x_t = A*np.sin(2*pi*f*t) + A2*np.sin(2*pi*f2*t)

x_f = dft(x_t)

N = x_t.size

#print(N)

amplitudes = np.abs(x_f)[:N//2]*1/N
frequencias = t[:N//2]*2
#print(frequencias)
#print(amplitudes)

# PLotting 

fig, axs = plt.subplots(2)
axs[0].plot(t,x_t)
axs[1].plot(frequencias,amplitudes)
axs[0].set(xlabel='Tempo (s)',ylabel='Amplitude')
axs[1].set(xlabel='Frequência (Hz)',ylabel='Amplitude')
plt.show()

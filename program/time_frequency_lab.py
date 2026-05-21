import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider 
from signals import Signal, SineWave, CosineWave

# Generating sine wave


t = np.linspace(0,10,10000)

A_0 = 1
phi_0 = 0
f_0 = 5

sine = SineWave(A_0,f_0,phi_0)
sine_signal = sine.generate(t)

fig , ax = plt.subplots(2,1,figsize=(10,10))
plt.subplots_adjust(bottom=0.35)
time_line, = ax[0].plot(t,np.zeros_like(t))

ax[0].set_xlim(0,1)
ax[0].set_ylim(-3.5,3.5)

ax[0].set_title("Interactive sine wave")
ax[0].grid()


y0 = np.fft.fft(sine_signal)
magnitude = np.abs(y0)/len(t)
freq = np.fft.fftfreq(len(t),d=t[1]-t[0])

freq_line, = ax[1].plot(freq,magnitude)
ax[1].set_xlim(-20, 20)
ax[1].set_ylim(0, 2)

ax[1].set_title("Frequency Domain")
ax[1].grid()

## Slider 
ax_amp=plt.axes([0.2,0.15,0.65,0.03])
ax_freq=plt.axes([0.2,0.10,0.65,0.03])
ax_phase=plt.axes([0.2,0.05,0.65,0.03])

s_amp=Slider(ax_amp,"Amp",1.0,3.0,valinit=A_0)
s_freq= Slider(ax_freq,"freq",1,20,valinit=f_0)
s_phase=Slider(ax_phase,"Phase",0,2*np.pi,valinit=phi_0)

def update(frame):
    A = s_amp.val
    f = s_freq.val
    phi = s_phase.val

    sine.A = A 
    sine.f = f
    sine.phi = phi 
    y = sine.generate(t)
    time_line.set_ydata(y)

    fft_vals = np.fft.fft(y)
    freq_line.set_ydata(np.abs(fft_vals)/len(t))
    return time_line,freq_line


ani=FuncAnimation(
    fig,
    update,
    frames=200,
    interval=30,
    blit=False  
)

plt.show()
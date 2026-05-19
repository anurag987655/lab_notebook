## Todays objective : 
# able to draw an interactive sine wave and observe as user changes its amplitude frequency and phase.
# able to pause and resume


import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider,Button


A_0 = 1
f_0= 5
phi_0 = 0

t = np.linspace(0,1,500)

# sine wave 

fig, ax = plt.subplots(figsize=(8,4))
plt.subplots_adjust(bottom=0.35)

line, = ax.plot(t, A_0 * np.sin(2 * np.pi * f_0 * t +  phi_0))

ax.set_xlim(0,1)
ax.set_ylim(-3,3)
ax.set_title("Interactive sine wave")

## Sliders : 

ax_amp = plt.axes([0.2,0.20,0.65,0.03])
ax_freq = plt.axes([0.2,0.15,0.65,0.03])
ax_phase = plt.axes([0.2,0.10,0.65,0.03])

s_amp = Slider(ax_amp,"Amp",0.1,3.0,valinit=A_0)
s_freq = Slider(ax_freq,"Freq",1,20,valinit=f_0)
s_phase = Slider(ax_phase,"Phase",0,2*np.pi,valinit=phi_0)

## Pause bottom

paused = False

ax_button = plt.axes([0.4,0.02,0.2,0.05])
button = Button(ax_button,"Pause/Resume")


def toggle(event):
    global paused
    paused = not paused

button.on_clicked(toggle)

frame = 0 

def update(_):

    global frame
    

    if not paused:  
        frame += 1

    A = s_amp.val
    f = s_freq.val
    phi = s_phase.val

    y = A * np.sin(2 * np.pi * f * t + phi + frame * 0.05)

    line.set_ydata(y)
    return line, 


ani=FuncAnimation(fig,update,frames=200,interval=30,blit=False)

plt.grid()
plt.show()
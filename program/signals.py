import numpy as np


class Signal:
    def __init__(self,A,f,phi):
        self.A = A 
        self.f = f
        self.phi = phi 

    def generate(self,t):
        raise NotImplementedError


class SineWave(Signal):
     def generate(self,t):
         return self.A * np.sin(2 * np.pi * self.f * t + self.phi)
     

class CosineWave(Signal):
    def generate(self, t):
        return self.A * np.cos(2 * np.pi * self.f * t + self.phi)

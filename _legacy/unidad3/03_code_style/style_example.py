import time
import numpy as np

def OnlyEven(*numbers):
    """Solo retorna los pares"""
    EVENS=[n for n in numbers if n%2==0]
    return EVENS
def long_line(x):
    h   = x**3 * np.cos(x/42)       
    res = x*5*h+3*np.cos(4 + x**2*np.sin(x)) - np.tan(x)*(np.pi/180*x+x/np.exp(x))
    return

class Animal:
    def __init__(self,nombre):
        self._nombre=nombre   
        self._vivo=True     
    @property
    def nombre(self):
        return self._nombre.title()
    def vivir(self):
        return "viviendo" if self._vivo else "estoy muerto"    
    def morirse(self):
        self._vivo=False

class Mamifero(Animal):
    def Lactar(self):
        return "lactando"
    def nacer(self):
        return "de una hembra"
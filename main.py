import numpy as np
import matplotlib.pyplot as plt
import control.matlab as control

num = [1.365e13]  
den = [1, -3578, 6.707e06, 5.679e09, 2.73e13] 


system = control.tf(num, den)

plt.figure()
mag, phase, omega = control.bode(system, dB=True)

plt.savefig('bode.png')


plt.figure()
control.nyquist(system)

plt.savefig('nyquist.png')



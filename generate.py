import numpy as np
import control
import control.matlab as matlab
import matplotlib.pyplot as plt

R1 = 21
R2 = 60
C1 = 22e-6
C2 = 28e-6

R3 = 21
R4 = 60
C3 = 22e-6
C4 = 28e-6

s = control.TransferFunction.s

G1 = (1/(R1*R2*C1*C2)) / (s**2 + (1/C2)*((1/R1) - (1/R2))*s + 1/(R1*R2*C1*C2))
G2 = (1/(R3*R4*C3*C4)) / (s**2 + (1/C4)*((1/R3) - (1/R4))*s + 1/(R3*R4*C3*C4))

L = G1 * G2

T = control.feedback(L, 1)
#print (T)

control.bode(T, dB=True)
plt.savefig('bode.png')


poles = control.pole(T)

if np.all(np.real(poles) < 0):
    print('The system is stable.')
else:
    print('The system is unstable or has limited stability margin.')


control.pzmap(T, title='Pole-zero map of the closed-loop system')

plt.savefig('pole-zero.png')

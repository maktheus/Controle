import control
import matplotlib.pyplot as plt

num = [1.365e13]  
den = [1, -3578, 6.707e06, 5.679e09, 2.73e13]  

G_s = control.tf(num, den)

Kp = 1 / den[-1] 
Ki = Kp / 10 

C_s = control.tf([Kp, Ki], [1, 0])

sys_open_loop = control.series(C_s, G_s)

plt.figure()
control.root_locus(sys_open_loop)
plt.title('Root Locus of System with PI Controller')


sys_closed_loop = control.feedback(sys_open_loop, 1)

time, response = control.step_response(sys_closed_loop)

plt.figure()
plt.plot(time, response)
plt.title('Step Response of Closed-Loop System with PI Controller')
plt.xlabel('Time (seconds)')
plt.ylabel('Response')

plt.savefig('step_response.png')

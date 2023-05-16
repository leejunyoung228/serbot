#%%
import time
import ipywidgets as widgets
from threading import Thread
#%%
delay = widgets.IntSlider(max=1000, value=1, description='delay')
gyro = [widgets.FloatSlider(min=-90, max=90, description='gyro_'+s) for s in ('x', 'y', 'z')] #degree/s
accel = [widgets.FloatSlider(min=-12, max=12, step=0.01, description='accel_'+s) for s in ('x', 'y', 'z')] #m/s^2
display(delay)
for i in range(3):
    display(gyro[i])
for i in range(3):   
    display(accel[i])
#%%
is_imu_thread = True

from pop.Pilot import IMU
imu = IMU()

def onReadIMU():
    while is_imu_thread:
        gyro[0].value, gyro[1].value, gyro[2].value = imu.getGyro().values()
        accel[0].value, accel[1].value, accel[2].value = imu.getAccel().values()

        time.sleep(delay.value/1000)

Thread(target=onReadIMU).start()
#%%
is_imu_thread = False
# %%

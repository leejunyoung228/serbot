from pop.Pilot import SerBot
from pop.Pilot import IMU
from pop.AI import Linear_Regression

import numpy as np
import time

bot = SerBot()
imu = IMU()
linear = Linear_Regression(ckpt_name='ktd')

dataset = {'gyro':[], 'steer':[]}
bot.setSpeed(50)

for n in np.arange(-1.0, 1.0+0.1, 0.2):
    n = round(n, 1)
    bot.steering = n
    bot.forward()
    time.sleep(0.5)
    gy = imu.getGyro('z')
    time.sleep(0.5)
    bot.backward()
    time.sleep(1)
    bot.stop()
    n = -n #Is this correct ???

    dataset['gyro'].append([gy])
    dataset['steer'].append([n]) 

    print({'gyro':gy, 'steer':n}) 
    # for _ in range(5):
    #     time.sleep(0.2)
    #     gy = imu.getGyro('z')
    #     dataset['gyro'].append([gy])
    #     dataset['steer'].append([n])
    #     print({'gyro':gy, 'steer':n})
    # bot.stop()
    # time.sleep(0.1)
    # bot.backward()
    # time.sleep(1)
    # bot.stop()
    # time.sleep(0.5)



linear.X_data = dataset['gyro']
linear.Y_data = dataset['steer']

linear.train(times=150, print_every=10)
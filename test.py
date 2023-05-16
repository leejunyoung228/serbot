#%%
from pop.Pilot import SerBot
from pop.Pilot import IMU
import timeit 
import time

#%%
bot = SerBot()
imu = IMU()

#%%
# tuple(imu.getGyro().values())[2]

t0 = timeit.default_timer()
t1 = timeit.default_timer()

print(t0 -t1)


#%%
bot.setSpeed(50)
bot.forward()
time.sleep(1)
bot.stop()
print(tuple(imu.getGyro().values())[0])

#%%
bot.stop()

#%%

#%%
t0_10 = timeit.default_timer()
t2 = timeit.default_timer()

count = 0
bot.steering = 0.0

bot.forward(50)
while True:
    
    t1= timeit.default_timer()
    if ((t1 - t0_10) * 10000) > 100:
        t0_10 = t1
        print("10 msecond")
        print(tuple(imu.getGyro().values())[2])
        if (tuple(imu.getGyro().values())[2]) > 0.1:
            bot.steering = -0.1
            t2 = t1
        elif (tuple(imu.getGyro().values())[2]) < -0.1:
            bot.steering = 0.1
            t2 = t1
        count += 1
    if ((t2 - t1) * 10000) > 200:
        bot.steering = 0
    if count >= 100:
        break
print("after 5 second")
bot.stop()

# %%

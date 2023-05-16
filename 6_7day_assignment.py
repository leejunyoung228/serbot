from pop.Pilot import SerBot
from pop.Pilot import IMU
from pop.LiDAR import Rplidar
import timeit
import time

DEST2TIME_MS = 10500
DETECT_LANGE_MM = 480
DEFAULT_SPEED = 60
H_RANGE = 45 // 2

bot = None
imu = None
lidar = None

def init():
    global bot, imu, lidar

    bot = SerBot()
    imu = IMU()
    lidar = Rplidar()

    lidar.connect()
    lidar.startMotor()

    bot.steering = 0
    bot.setSpeed(DEFAULT_SPEED)
    bot.forward()

def destroy():
    bot.stop()
    lidar.stopMotor()

def forward_detect(point_frame):
    for p in point_frame:
        if p[0] > (360-H_RANGE) or p[0] < (0+H_RANGE):
            if p[1] <= DETECT_LANGE_MM:
                return True
        else:
            return False

def turn_180():
    curr_speed = bot.getSpeed()
    n = 185
    bot.turnLeft()
    if curr_speed <= 20:
        d = n/90 - (n/90)*0.0
    elif curr_speed <= 40:
        d = n/90 - (n/90)*0.4
    elif curr_speed <= 60:
        d = n/90 - (n/90)*0.6
    elif curr_speed <= 80:
        d = n/90 - (n/90)*0.7
    elif curr_speed <= 100:
        d = n/90 - (n/90)*0.76
    time.sleep(d)
    bot.forward()

def stablilizer(yaw):
    if yaw < -1:
        bot.steering = 0.2
    elif yaw < -0.7:
        bot.steering = 0.15
    elif yaw < -0.5:
        bot.steering = 0.1
    elif yaw < -0.3:
        bot.steering = 0.05
    elif yaw < -0.05:
        bot.steering = 0.01
    if yaw > 1:
        bot.steering = -0.2
    elif yaw > 0.7:
        bot.steering = -0.15
    elif yaw > 0.5:
        bot.steering = -0.1
    elif yaw > 0.3:
        bot.steering = -0.05
    elif yaw > 0.05:
        bot.steering = -0.01

def main():
    check_trun = False

    init()

    t0_ms = timeit.default_timer()

    while True:
        t1_ms = timeit.default_timer()
        if (t1_ms - t0_ms) * 1000 >= DEST2TIME_MS:
            if not check_trun:
                check_trun = True
                turn_180()
                t0_ms = timeit.default_timer()
                print("turn")
            else:
                break

        yaw = tuple(imu.getGyro().values())[2]
        point_frame = lidar.getVectors()

        stablilizer(yaw)
        detect = forward_detect(point_frame)

        if detect:
            bot.stop()
        else:
            bot.forward()
    
        print(yaw, detect, bot.steering)

    destroy()

if __name__ == "__main__":
    main()
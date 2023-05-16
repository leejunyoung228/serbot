from pop.Pilot import IMU
from third_angle import SerBotEx
from lidar import Lidar
import timeit 
def main():
    bot = SerBotEx()
    imu = IMU()

    t0_10 = timeit.default_timer()
    t2 = timeit.default_timer()
    serbot_width = 500
    direction_count = 8
    lidar = Lidar(serbot_width, direction_count)
    current_direction = 0

    count = 0
    bot.steering = 0.0
    check = False
    # bot.forward(60)
    print("Start SerBot!!!")
    while True:
        try:
            if lidar.collisonDetect(500)[current_direction]:
                bot.stop()
                continue
            else:
                bot.forward(60)
            t1= timeit.default_timer()
            if ((t1 - t0_10) * 10000) > 100:
                t0_10 = t1
                print("10 msecond")
                print(tuple(imu.getGyro().values())[2])
                if (tuple(imu.getGyro().values())[2]) < -0.60:
                    bot.steering = -0.1
                    t2 = t1
                elif (tuple(imu.getGyro().values())[2]) > 0.60:
                    bot.steering = 0.1
                    t2 = t1
                count += 1
            if ((t2 - t1) * 10000) > 40:
                bot.steering = 0
            if count >= 500 and not check:
                bot.turnAngleLeft(198)
                check = True
                count = 0
                # bot.forward(60)
            elif count >= 500:
                break
        except (KeyboardInterrupt, SystemError):
            break
    bot.stop()
    print('Stopped Serbot!')

if __name__ == '__main__':
    main()
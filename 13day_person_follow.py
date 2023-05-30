import time
from pop import Camera
from pop.Pilot import Object_Follow
from pop.Pilot import SerBot
from pop.LiDAR import Rplidar

bot = None
of = None
lidar = None
person_not_found = False
person_not_found_cnt = 0
DETECT_LANGE_MM = 500
H_RANGE = 90 // 2

def setup():
    global bot, of, lidar

    cam = Camera()
    of = Object_Follow(cam)
    bot = SerBot()
    lidar = Rplidar()
    lidar.connect()
    lidar.startMotor()
    

    of.load_model()
    print("="*50)
    print("Model load ok!")
    print("It starts in about 10 seconds.")

def loop():
    global person_not_found_cnt, pre_rate, person_not_found
    point_frame = lidar.getVectors()
    detect = forward_detect(point_frame)
    if detect:
        print("stop")
        bot.stop()
    else:
        person = of.detect(index='person')
        if person:
            person_not_found_cnt = 0
            person_not_found = False
            x = round(person['x'] * 4, 1)
            rate = round(person['size_rate'], 1)

            bot.steering =  1.0 if x > 1.0 else -1.0 if x < -1.0 else x

            if rate > 0.4:
                person_not_found = True
                bot.stop()
            elif rate > 0.3:
                bot.forward(40)
            elif rate > 0.2:
                bot.forward(60)
            elif rate > 0.1:
                bot.forward(70)
            else:
                bot.forward(80)

            print(f"{rate}, {bot.steering}")
        else:
            if person_not_found == False:
                person_not_found_cnt += 1
                if person_not_found_cnt > 5:
                    bot.setSpeed(50)
                    if bot.steering < 0:
                        bot.turnLeft()
                        time.sleep(0.3)
                    elif bot.steering > 0:
                        bot.turnRight()
                        time.sleep(0.3)
                    else:
                        bot.stop()
                    person_not_found = True
            bot.stop()
            print("person not dectected...")  
 
def forward_detect(point_frame):
    for p in point_frame:
        if p[0] > (360-H_RANGE) or p[0] < (0+H_RANGE):
            if p[1] <= DETECT_LANGE_MM:
                return True
        else:
            return False

def main():
    setup()
    while True:
        try:
            loop()
        except KeyboardInterrupt:
            break
    
    bot.stop()
    lidar.stopMotor()

if __name__ == '__main__':
    main()
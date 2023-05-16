from pop.Pilot import SerBot
from lidar import Lidar
import random
from third_angle import SerBotEx

def main():
    serbot_width = 500
    direction_count = 8
    speed = 50
    

    bot = SerBotEx()
    lidar = Lidar(serbot_width, direction_count)
    current_direction = 0
    flag = True
    bot.steering = 0
    
    print("Start SerBot!!!")

    while flag:
        try:
            if lidar.collisonDetect(300)[current_direction]:
                # bot.stop()
                # bot.turnAngleRight(45)
                continue

            detect = lidar.collisonDetect(800)

            if sum(detect) == direction_count:
                # bot.stop()
                # bot.turnAngleRight(45)
                continue
            
            if detect[current_direction]:
                # open_directions = [i for i, val in enumerate(detect) if not val]
                # current_direction = random.choice(open_directions)
                if detect[0]:
                    if detect[1]:
                        bot.steering = -1
                    elif detect[2]:
                        bot.steering = 1
                else:
                    bot.steering = 0
                    

            # bot.move(lidar.degrees[current_direction], speed)
            # bot.forward()
            print(detect)

        except (KeyboardInterrupt, SystemError):
            flag = False
    
    bot.stop()
    print('Stopped Serbot!')

if __name__ == '__main__':
    main()
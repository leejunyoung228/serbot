import time
from pop import Camera
from pop.Pilot import Object_Follow
from pop.Pilot import SerBot

bot = None
of = None
person_not_found = None

def setup():
    global bot, of, person_not_found

    cam = Camera()
    of = Object_Follow(cam)
    bot = SerBot()

    person_not_found = 0

    of.load_model()
    print("="*50)
    print("Model load ok!")
    print("It starts in about 10 seconds.")

def loop():
    global person_not_found

    person = of.detect(index='person')
    if person:
        person_not_found = 0
        x = round(person['x'] * 4, 1)
        rate = round(person['size_rate'], 1)

        # bot.steering =  1.0 if x > 1.0 else -1.0 if x < -1.0 else x

        # if rate < 0.2:
        #     bot.forward(80)
        # elif rate < 0.4:
        #     bot.forward(60)
        # # elif rate < 0.6:
        # #     bot.forward(40)
        # else:
        #     bot.steering = 0
        #     bot.stop()
        
        if rate > 0.2:
            bot.stop()
        else:
            bot.forward(60)
            bot.steering =  1.0 if x > 1.0 else -1.0 if x < -1.0 else x
 
        print(f"{rate}, {bot.steering}")            
    else:
        if person_not_found == 0:
            bot.setSpeed(50)
            if bot.steering < 0:
                bot.turnLeft()
                time.sleep(0.3)
            elif bot.steering > 0:
                bot.turnRight()
                time.sleep(0.3)
            person_not_found = 1
        bot.stop()
        print("person not dectected...")  
 
def main():
    setup()
    while True:
        try:
            loop()
        except KeyboardInterrupt:
            break
    
    bot.stop()

if __name__ == '__main__':
    main()
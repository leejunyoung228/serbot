from pop import Camera
from pop.Pilot import Object_Follow
from pop.Pilot import SerBot

cam = Camera()
of = Object_Follow(cam)
bot = SerBot()

of.load_model()
print("="*50)
print("Model load ok!")
print("It starts in about 10 seconds.")
print("="*50)

while True:
    person = of.detect(index="person")
    if person:
        print(round(person['x'],1), round(person['size_rate'],1))
        steer = round(person['x'],1) * 3.5
        limit = round(person['size_rate'],1)
        bot.steering = -1.0 if steer < -1.0 else 1.0 if steer > 1.0 else steer
        if limit < 0.2:
            bot.stop()
    else:
        bot.stop()
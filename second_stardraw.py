#%%
from pop.Pilot import SerBot
from third_angle import SerBotEx
import time

#%%
bot = SerBotEx()

#%%
bot.setSpeed(60)

#%%
bot.turnRight()
time.sleep(0.282)
bot.stop()

# %%
SerBotEx.turnAngleRight(90)

# %%
SerBotEx.turnAngleLeft(90)

# %%
n=0.5
bot.turnAngleLeft(60)
for i in range(6):
    bot.forward()
    time.sleep(n)
    bot.turnAngleLeft(120)
    bot.forward()
    time.sleep(n)
    if i < 5:
        bot.turnAngleRight(60)
    else:
        bot.turnAngleLeft(15)
bot.forward()
time.sleep(n)
bot.stop()

# %%

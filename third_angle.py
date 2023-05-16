from pop.Pilot import SerBot
import time

class SerBotEx(SerBot):
    def __calc_delay(self, n):
        speed = self.getSpeed()
        if speed <= 20:
            d = n/90 - (n/90)*0.0
        elif speed <= 40:
            d = n/90 - (n/90)*0.4
        elif speed <= 60:
            d = n/90 - (n/90)*0.6
        elif speed <= 80:
            d = n/90 - (n/90)*0.7
        elif speed <= 100:
            d = n/90 - (n/90)*0.76
        return d
    def turnAngleLeft(self, n):
        d = self.__calc_delay(n)
        self.turnLeft()
        time.sleep(d)
        self.stop()
    def turnAngleRight(self, n):
        d = self.__calc_delay(n)
        self.turnRight()
        time.sleep(d)
        self.stop()
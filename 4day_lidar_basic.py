from pop.LiDAR import Rplidar

lidar = Rplidar()
lidar.connect()
lidar.startMotor()

for _ in range(5):
    V = lidar.getVectors()
    for item in V:
        print("Angle: %.1f, Dist: %dmm"%(item[0], item[1]))
    print("-"*60)
    input("press <Enter>")

lidar.stopMotor() 
# from pop.LiDAR import Rplidar
# import numpy as np

# lidar = Rplidar()
# lidar.connect()
# lidar.startMotor()

# FR_ANGLE = 30
# LR_ANGLE = 20
# MG_ANGLE = 5


# while True:
#     V = np.array(lidar.getVectors())

#     front_center = V[np.where((V[:, 0:1] >= 360-(FR_ANGLE//2)) | (V[:, 0:1] < (FR_ANGLE//2)))[0], 1:2]
#     front_left = V[np.where((V[:, 0:1] >= 360-(FR_ANGLE//2)-MG_ANGLE-FR_ANGLE) & (V[:, 0:1] < (FR_ANGLE//2)))[0], 1:2]
#     front_right = V[np.where((V[:, 0:1] >= (FR_ANGLE//2)+MG_ANGLE) & (V[:, 0:1] < (FR_ANGLE//2)+MG_ANGLE))[0], 1:2]

#     rear_center = V[np.where((V[:, 0:1] >= 180-(FR_ANGLE//2)) | (V[:, 0:1] < 180+(FR_ANGLE//2)))[0], 1:2]
#     rear_left = V[np.where((V[:, 0:1] >= 180-(FR_ANGLE//2)+MG_ANGLE) & (V[:,0:1] < 180 +(FR_ANGLE//2)+))]
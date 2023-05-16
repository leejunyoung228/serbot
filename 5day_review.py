#%%
direction = 8
degrees = list(range(0,360,360//direction))
print(degrees)

#%%
import math
serbot_width = 500
length = 800
tan = (serbot_width / 2) / length
angle = math.atan(tan) * (180 / math.pi)
print(angle)

# %%
detect = [0] * len(degrees)
detect_direction = 45
degree = 70
min_degree = (detect_direction - angle) % 360
max_degree = (detect_direction + angle) % 360
t = (degree + (360 - min_degree)) % 360 
print(min_degree, max_degree, t)

# %%

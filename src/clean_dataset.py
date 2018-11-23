import os, random
from shutil import copyfile

birds = os.listdir("birds/")
drones = os.listdir("drones/")

for x in drones:
    images = os.listdir(x)
    for y in images:
        copyfile("drones/" + x + y, "drones/" + x + "_" + y)

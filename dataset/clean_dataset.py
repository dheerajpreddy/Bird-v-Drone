import os, random
from shutil import copyfile

birds = os.listdir("birds/")
drones = os.listdir("drones/")

for x in birds:
    # print(x)
    if os.path.isdir("birds/" + x):
        print(x)
        images = os.listdir("birds/" + x)
        for y in images:
            copyfile("birds/" + x + "/"+ y, "birds/" + x + "_" + y)

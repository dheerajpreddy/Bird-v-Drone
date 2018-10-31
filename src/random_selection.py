import os, random
from shutil import copyfile

birds = os.listdir("birds/")
drones = os.listdir("Drones/positive/")
actual = "actual/"

drone_images = []
for x in drones:
    if '.jpg' in x:
        drone_images.append(x)
# drone_images = [x if '.jpg' in x for x in drones]
random.shuffle(drone_images)
drones = drone_images[0:200]
for x in drones:
    copyfile("Drones/positive/" + x, actual + "drones/" + x)


for bird in birds:
    if os.path.isdir("birds/" + bird):
        files = os.listdir("birds/" + bird)
        file1 = random.choice(files)
        # files.remove(file1)
        # file2 = random.choice(files)
        copyfile("birds/" + bird + "/" + file1, actual + "birds/" + file1)
        # copyfile("birds/" + bird + "/" + file2, actual + "birds/" + file2)

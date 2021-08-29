import os
from PIL import Image, ImageTk
object_name = '2_Object'
path = 'images/Objekt_2'
image_number = 1
for f in os.listdir(path):
    old_file = os.path.join(path, f)
    if old_file != path + '/.DS_Store':
        new_name = object_name + '_' + str(image_number) + '.JPG'
        new_file = os.path.join(path, new_name)
        os.rename(old_file, new_file)
        image_number += 1


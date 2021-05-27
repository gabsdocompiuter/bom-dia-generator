import pathlib
import os

def read_dir(dir):
    with os.scandir(dir) as entries:
        image_counter = 0

        for entry in entries:
            if entry.is_dir():
                read_dir(entry.path)
            else:
                _, extension = os.path.splitext(entry.path)
                os.rename(entry.path, f"{dir}/{image_counter}{extension}")
                
                image_counter += 1

path = pathlib.Path().absolute()
assets_dir = f"{path}/../assets/"


read_dir(assets_dir)

import sys
import os
from PIL import Image


def convert_images(source_dir, target_dir):
    # check if folders new/exists, if not create the second one
    if not os.path.exists(source_dir) or not os.path.isdir(source_dir):
        print(f'Source dir {source_dir} is invalid or does not exist')
        return

    # loop through the Pokedex
    files = os.listdir(source_dir)

    if len(files) <= 0:
        print(f"No jpg images found in {source_dir}")
        return

    if not os.path.exists(target_dir) or not os.path.isdir(target_dir):
        os.makedirs(target_dir)

    # loop through the Pokedex
    for file in files:
        if file.endswith('jpg'):
            # convert images to png and save to the new folder
            img = Image.open(f'{source_dir}/{file}')
            clean_name = os.path.splitext(file)[0]
            img.save(f'{target_dir}/{clean_name}.png', 'png')
            #img.save(f'{target_dir}/{file[0:-3]}png', 'png')


convert_images(sys.argv[1], sys.argv[2])

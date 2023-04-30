# @shyzu
# https://github.com/lucky5isuru


import os
import ctypes
import time
import random

# Define the folder where the images are located
IMAGE_FOLDER = r'/path/to/folder/with/images'

# Define the list of image file extensions to look for
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png']

# Find all image files in the folder and its subfolders
def find_images_in_folder(folder):
    images = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if os.path.splitext(file)[1].lower() in IMAGE_EXTENSIONS:
                images.append(os.path.join(root, file))
    return images

# Define the list of images
images = find_images_in_folder(IMAGE_FOLDER)

# Randomize the order of the images
random.shuffle(images)

# Define the time interval between wallpaper changes (in seconds)
INTERVAL = 3600

# Set the Windows desktop wallpaper
def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 1
    
    try:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE)
    except ctypes.WinError:
        print('Failed to set wallpaper:', image_path)

# Main loop to update the wallpaper
if __name__ == '__main__':
    while True:
        # Select the next image in the shuffled list
        image_path = random.choice(images)
        # Set the wallpaper
        set_wallpaper(image_path)
        # Wait for the specified interval before changing again
        time.sleep(INTERVAL)

# image_folder = 'F:\Site Build\Wallpaper Changer Py\wallpapers'



import os
import ctypes
import time
import random

# Define the folder where the images are located
image_folder = 'F:\Site Build\Wallpaper Changer Py\wallpapers'

# Define the list of image file extensions to look for
image_extensions = ['.jpg', '.jpeg', '.png']

# Find all image files in the folder and its subfolders
def find_images_in_folder(folder):
    images = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if os.path.splitext(file)[1].lower() in image_extensions:
                images.append(os.path.join(root, file))
    return images

# Define the list of images
images = find_images_in_folder(image_folder)

# Randomize the order of the images
random.shuffle(images)

# Define the time interval between wallpaper changes (in seconds)
interval = 30

# Set the Windows desktop wallpaper
def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 1
    
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE)

# Main loop to update the wallpaper
if __name__ == '__main__':
    while True:
        # Select the next image in the shuffled list
        image_path = random.choice(images)
        # Set the wallpaper
        set_wallpaper(image_path)
        # Wait for the specified interval before changing again
        time.sleep(interval)

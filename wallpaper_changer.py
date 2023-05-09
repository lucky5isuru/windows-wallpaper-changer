import os
import ctypes
import time
import random
import configparser

# Initialize configparser object to read and write configuration file
config = configparser.ConfigParser()

# Check if the config file exists
if not os.path.exists('config.ini'):
    # Ask for the image folder path and time interval and save them in config file
    image_folder = input("Enter the path to the folder containing the images: ")
    interval = int(input("Enter the time interval (in seconds) between wallpaper changes: "))
    config['DEFAULT'] = {'image_folder': image_folder, 'interval': str(interval)}
    with open('config.ini', 'w') as config_file:
        config.write(config_file)
else:
    # Read the image folder path and time interval from the config file
    config.read('config.ini')
    image_folder = config['DEFAULT']['image_folder']
    interval = int(config['DEFAULT']['interval'])

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
images = find_images_in_folder(image_folder)

# Randomize the order of the images
random.shuffle(images)

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
        time.sleep(interval)

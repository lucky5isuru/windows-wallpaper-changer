# Change Windows Desktop Wallpaper

This is a simple Python script to change the Windows desktop wallpaper using given wallpapers in a specified folder. This script enables you to set your wallpaper to change at specified intervals and provides the option to select different wallpapers from a given folder.

## Prerequisites

- **Python 3**: This script requires Python 3 to be installed on your machine. If you don't already have Python 3 installed, you can download it from the [official website](https://www.python.org/downloads/).
- **Windows**: This script is designed to only work on Windows operating systems.

## Usage

1. Clone the repository or download the source code files.
2. Ensure that Python 3 is installed on your machine.
3. Install the required packages by running the following command in your terminal: 

pip install -r requirements.txt

4. Open the `wallpaper.py` file in your favourite Python editor or IDE
5. Edit the code at the top of the script to include the folder location of the images you want to use:

DIR_PATH = '/path/to/folder/with/images'

6. You can customize the time interval between each wallpaper change by editing the following line of code:

INTERVAL = 3600 # specify the interval in seconds

In the above example, the wallpaper will change every hour (3600 seconds). You can change this to your desired interval.

7. Save the file and run the script using the following command:

python wallpaper.py

This will run the script and start changing your Windows desktop wallpaper using images from the specified folder.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- [Your Name](https://github.com/lucky5isuru)

# -*- coding: utf-8 -*-
"""
Screenshot_1

One click screenshot of a region for multiple monitors and saved to JPEG 
and/or PDF.

Directions-
1. Determine the region of the screen you want to capture.
2. Fill in the variable sections
3. Click run script to capture the screen as needed.

"""

import os
import datetime as dt
import pyautogui as pag
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

# this def is a tool to find pixel positions. To use just put
# "find_mounse_pixel_coordinates()" in your console, point the mouse to the 
# point on the screen and push enter.
def find_mounse_pixel_coordinates():
    p = pag.position()
    x, y = p[0], p[1]
    return print(x, ",", y)

# VARIABLES ------------------------------------------------------------------

# What part of the screen to capture. (left, top, right, bottom)
screen_region = (0, 0, 1600 , 800) 

# Folder where evidence will be saved 
output_folder = r"C:\Users\erikw\Documents\tester"

# Name of the output files (pdf and jpeg will be created).  time will be appended
#      and sample number will be attached.
output_file = 'Screenshot_'

# Whether of not to save PDFs ("Y" or "N")
save_pdf_files = 'Y'

# END VARIABLES ---------------------------------------------------------------

# Counts the number of screenshots in the ouput_file.  This is the smaple number
sample_files = [f for f in os.listdir(output_folder) if f != 'Thumbs.db']
sample_number = round((len(sample_files) + 1.001)/2, ndigits=0) if save_pdf_files == 'Y'  \
                    else round(len(sample_files) + 1, ndigits=0)

# Take the screenshot
screenshot = pag.screenshot(region=screen_region)

# Save the files
file_name_pdf = f'Sample_screenshot - {sample_number} - ' + str(dt.datetime.now()) + '.pdf'
file_name_jpg = f'Sample_screenshot - {sample_number} - ' + str(dt.datetime.now()) + '.jpg'

file_name_pdf = file_name_pdf.replace(':','-')
file_name_jpg = file_name_jpg.replace(':','-')

path_name_pdf = os.path.join(output_folder, file_name_pdf)
path_name_jpg = os.path.join(output_folder, file_name_jpg)

if save_pdf_files == 'Y':
    screenshot.save(path_name_pdf)
screenshot.save(path_name_jpg)
print(sample_number)
print(file_name_jpg)
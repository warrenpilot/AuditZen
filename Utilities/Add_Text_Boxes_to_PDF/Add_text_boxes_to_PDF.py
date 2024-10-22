# -*- coding: utf-8 -*-
"""
Add_text_boxes_to_PDF

The script places a customized set of text boxes (or annotations) into an
existing PDF.

Instructions-
1. Create list of text boxes either as a dict(see below) or in Excel template.
2. Input other variables
        - path to the PDF
        - path to the output pdf (choose diff name to keep the original intact).
        - use_df to 'Y' or 'N' (Y if you want to use Excel)
        - excel_path if you use_df = 'Y'
3. You can change the size, font, color of the boxes if you want.
4. Run script.
"""


# Imports
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import AnnotationBuilder
import pandas as pd


# VARIABLES ------------------------------------------------------------------

input_pdf = r"Path/to/PDF.pdf"
output_pdf = r"Path/for/output/PDF.pdf"


# Text Variables

# Edit the dictionary below to put in the information you want.  Text & Page.
text_dict = {
    'box1': 
        {'txt_str': "Text for box 1", 
         'page_no': 1},
    'box2': 
        {'txt_str': "Text for box 2", 
         'page_no': 1},
    'box3': 
        {'txt_str': "Text for box 3", 
         'page_no': 3},
    }
    
# Alternative dict construction from pandas df read from an Excel file. 
# Excel column names must be box, txt_str, page_no. Template if folder.

use_df = 'N'  # Type 'Y' if you want to use an excel template.

excel_path = r"Path/to/Excel/Template.xlsx"

if use_df == 'Y':
    text_df = pd.read_excel(excel_path)
    text_dict = text_df.set_index('box').to_dict(orient='index')

# Base size and location of boxes
base_size = (20, 550, 300, 675)
# Font
font_size = "10pt"

# END VARIABLES --------------------------------------------------------------



# Pull in the PDF

reader = PdfReader(input_pdf)
writer = PdfWriter()
for page_num in range(len(reader.pages)):
    page = reader.pages[page_num]
    writer.add_page(page)

# # Annotation For Loop

keys_list = list(text_dict.keys())

for k in keys_list:
    text_box = AnnotationBuilder.free_text(
        text_dict[k]['txt_str'],
        rect=base_size,
        font='Arial',
        bold=True,
        font_size=font_size,
        font_color="EC3A06",
        border_color="EC3A06")

    writer.add_annotation(page_number=text_dict[k]['page_no']-1, annotation=text_box)


# Save the file
with open(output_pdf, "wb") as fp:
    writer.write(fp)
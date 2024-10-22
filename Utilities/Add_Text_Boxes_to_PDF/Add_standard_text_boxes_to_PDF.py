# -*- coding: utf-8 -*-
"""
Creates a set of three standard text boxes on first page of PDF.
This is a standard audit practice for evidence.

Instructions
1. Input the variables you want (path to input and output pdfs, title, review 
                                 and psc_review).
2. You can also change some of the size, font, etc. if you want.
2. Run Script.
"""


# Imports
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import AnnotationBuilder


# VARIABLES

input_pdf = r"Path/to/PDF"
output_pdf = r"Path/to/PDF/_boxes.pdf"


# Text Variables
title1 = "Document Title"
review1 = "Preparer/Review\n\nPreparer - XXXX  :  Date - mm/dd/yy\n\nReviewer - XXX  :  DATE - mm/dd/yy"
psc1 = "(P) Purpose\n\n(S) Source\n\n(C) Conclusion"
# Sizes
title_size = (200, 750, 500, 775)
review_size = (400, 550, 600, 675)
psc_size = (20, 550, 300, 675)
# Font
font_list = ["16pt", "10pt", "10pt"]


# List Creation
text_list = [title1, review1, psc1]
size_list = [title_size, review_size, psc_size]


# Pull in the PDF

reader = PdfReader(input_pdf)
writer = PdfWriter()
for page_num in range(len(reader.pages)):
    page = reader.pages[page_num]
    writer.add_page(page)

# # Annotation For Loop

for txt, sz, fnt in zip(text_list, size_list, font_list):
    text_box = AnnotationBuilder.free_text(
        txt,
        rect=sz,
        font='Arial',
        bold=True,
        font_size=fnt,
        font_color="EC3A06",
        border_color="EC3A06")

    writer.add_annotation(page_number=0, annotation=text_box)


# Save the file
with open(output_pdf, "wb") as fp:
    writer.write(fp)
# -*- coding: utf-8 -*-
"""
Merge_All_Files_in_Folder_into_one_PDF

Identifies all the PDFs in a folder and merges them into one PDF file.

Instructions-
1. Paste the folder path in the "folder_path" variable below.
2. Run the script
3. Change the file name of "merged_pdf.pdf" which while be saved to the same
    folder.
"""

from PyPDF2 import PdfMerger
import os


def merge_pdfs(input_files, output_folder):
    file_name = 'merged_pdf.pdf'
    output_file = os.path.join(output_folder, file_name)
    merger = PdfMerger()
    for pdf in input_files:
        merger.append(pdf)
    merger.write(output_file)
    merger.close()
    

folder_path = r"PATH/TO/FOLDER"
folder_files = os.listdir(folder_path)

input_files = []

for f in folder_files:
    if f[-4:] == '.pdf' or f[-4:] == '.PDF':
        fp = os.path.join(folder_path, f)
        input_files.append(fp)
        
merge_pdfs(input_files, folder_path)

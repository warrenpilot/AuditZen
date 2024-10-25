# -*- coding: utf-8 -*-
"""
Convert_Files_to_PDF

Converts all .docx (Word), .pptx (PowerPoint) and .jepg (Jepg images) to PDF
which are placed in the same folder.

Instructions
1. Input FOLDER path on line 43 (or folder_path variable wherever it is)
2. Run script
"""


import os
from win32com.client import Dispatch
from PIL import Image
from pptxtopdf import convert


def convert_to_pdf(file_path):
  """Converts a given file to PDF using Word or Outlook.

  Args:
    file_path: The path to the file to be converted.

  Returns:
    The path to the converted PDF file.
  """

  if file_path.endswith('.docx'):
    word = Dispatch('Word.Application')
    doc = word.Documents.Open(file_path)
    doc.SaveAs(file_path[:-5] + '.pdf', FileFormat=17)  # FileFormat=17 for PDF
    doc.Close()
    word.Quit()
  elif file_path.endswith('.jpeg') or file_path.endswith('.jpg') \
      or file_path.endswith('.JPEG') or file_path.endswith('.JPG'):
    image = Image.open(file_path)
    output_file = file_path[:-4] + '.pdf'
    image.save(output_file, 'PDF')


def main():
    
    folder_path = r"PATH/TO/FOLDER"  # Replace with your desired folder path
    
    # Convert PDFs
    convert(folder_path, folder_path)
    
    for root, _, files in os.walk(folder_path):
      for file in files:
        if file.endswith('.docx')  or file.endswith('.jpg') or file.endswith('.jepg')\
            or file.endswith('.JPG') or file.endswith('.JEPG'):
          file_path = os.path.join(root, file)
          print("--->", file_path)
          pdf_file = convert_to_pdf(file_path)
          print(f"Converted {file_path} to {pdf_file}")

if __name__ == "__main__":
    main()
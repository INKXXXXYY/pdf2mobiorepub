# PDF to MOBI GUI Converter

## Introduction
This is a simple Python script that creates a graphical user interface (GUI) application for converting PDF files to MOBI format using the ebook-convert command line tool from Calibre. The script uses tkinter for the GUI, PyMuPDF or PyPDF2 for handling PDF files, and the ebook-convert utility from Calibre.

## Prerequisites
Before running this script, make sure you have the following software installed on your computer:

1. Python
2. tkinter (usually installed with Python)
3. PyMuPDF or PyPDF2
4. Calibre (especially the ebook-convert tool)

## Usage
To use this script, simply run it from a terminal or command prompt. The script will create a window where you can drag and drop a PDF file. It will then open and validate the PDF file, convert it to MOBI format using ebook-convert, and allow you to save the MOBI file to the location of your choice.

## Limitations
Please note that this script does not handle potential formatting issues when converting PDF to MOBI, such as text reflow or image adjustments, which may require additional processing.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
Thanks to the developers of tkinter, PyMuPDF, PyPDF2, and Calibre for their great work.

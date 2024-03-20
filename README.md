# PDF to Excel Converter

This Python script converts text from PDF files into an Excel spreadsheet format. It utilizes the `pdf2image` library to extract images from PDF pages and the `pytesseract` library for Optical Character Recognition (OCR) to recognize text from the images.

## Features
- Extracts text from PDF files, including scanned documents and images containing text.
- Supports multiple languages for OCR.
- Outputs the extracted text into an Excel spreadsheet with page numbers.
- Provides terminal feedback during OCR process.

## How it Works
The script first converts each page of the input PDF file into an image format using the `pdf2image` library. It then performs OCR on each image using the `pytesseract` library to extract text. If no text is detected, the script retries the OCR process to ensure accurate extraction.

The extracted text along with the corresponding page numbers is stored in a DataFrame using the `pandas` library. Finally, the DataFrame is saved to an Excel spreadsheet.

## Usage
1. Install required Python libraries:
pip install pdf2image pytesseract pandas

2. Ensure that Tesseract OCR is installed and its directory is added to the system PATH.
- For Windows: [Download Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and set up the PATH.
- For Linux: Install Tesseract OCR using package manager (e.g., `apt-get install tesseract-ocr`).

3. Run the script with the input PDF file path and desired output Excel file path:
python PDF2EXCEL.py input.pdf output.xlsx


## Requirements
- Python 3.x
- Tesseract OCR
- pdf2image
- pytesseract
- pandas

## License
This project is licensed under the [MIT License](LICENSE), allowing for open-source contributions and reuse with proper attribution.

## Contributions
Contributions are welcome! Feel free to open issues for bug fixes, feature requests, or submit pull requests with improvements.

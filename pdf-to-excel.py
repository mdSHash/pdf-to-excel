import os
import pytesseract
from pdf2image import convert_from_path
import pandas as pd

def pdf_to_excel(pdf_path, excel_path, lang='eng'):
    # Convert PDF to images
    images = convert_from_path(pdf_path)

    # Initialize empty lists to store page numbers and text
    page_numbers = []
    page_texts = []

    # Loop through each image
    for i, img in enumerate(images):
        # Perform OCR on the image
        text = pytesseract.image_to_string(img, lang=lang)

        # If no text detected, process OCR again
        if not text.strip():
            print(f"No text or image detected on page {i+1}, processing OCR again...")
            # Perform OCR on the image again
            text = pytesseract.image_to_string(img, lang=lang)

        # Append page number and text to the lists
        page_numbers.append(i + 1)
        page_texts.append(text)

    # Create a DataFrame from the lists
    df = pd.DataFrame({"Page Number": page_numbers, "Text": page_texts})

    # Save DataFrame to Excel file
    df.to_excel(excel_path, index=False)
    print(f"Excel file saved to: {excel_path}")

# Example usage:
pdf_path = "input.pdf"
excel_path = "output.xlsx"
pdf_to_excel(pdf_path, excel_path)

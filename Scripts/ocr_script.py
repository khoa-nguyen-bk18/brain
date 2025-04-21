import easyocr
import sys

# Initialize the OCR reader
reader = easyocr.Reader(['en'])  # Specify language(s)

# Path to the image
image_path = '/home/khoa/PKM/pkm/content/attachments/IMG_20250416_065708.jpg'

# Perform OCR
results = reader.readtext(image_path)

# Save results to a file
with open('../.temp/easyocr_results.txt', 'w') as f:
    for (bbox, text, prob) in results:
        f.write(f"{text}\n")

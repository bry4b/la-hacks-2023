import pytesseract
from PIL import Image
import re

# Load image using PIL library
def imagetotext(name):
    img = Image.open(name)

    # Convert image to grayscale
    img = img.convert('L')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # Use Tesseract OCR to convert image to text
    text = pytesseract.image_to_string(img)

    # Print the extracted text
    #print(text)
    #print(type(text))

    #convert from string to text
    words = text.split()
    #print(words)
    text = re.sub(r"[^a-zA-Z,'?.\s-]", "", text)

    # Remove extra spaces and convert to lowercase
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text

#text = imagetotext('historyclass.png')
#print(text)
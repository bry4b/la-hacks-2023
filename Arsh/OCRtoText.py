import pytesseract
from PIL import Image

# Load image using PIL library
def imagetotext(name):
    img = Image.open(name)

    # Convert image to grayscale
    img = img.convert('L')

    # Use Tesseract OCR to convert image to text
    text = pytesseract.image_to_string(img)

    # Print the extracted text
    #print(text)
    #print(type(text))

    #convert from string to text
    words = text.split()
    print(words)
    return text

#imagetotext('test.png')
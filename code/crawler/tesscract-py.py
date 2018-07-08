#conding=utf-8

import pytesseract
from PIL import Image

image = Image.open('./mayday.jpg')

text = pytesseract.image_to_string(image)

print(text)

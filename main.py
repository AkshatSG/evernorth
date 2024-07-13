from ocr import *
from llm import *

#Provide your image_path here (this is just to test if the ocr program works as expected):
path = './testocr.png'

#Extracting text (will be printed automatically by method) & displaying findings on the image.
#You will need to close the initial popup display of the image in order to proceed with the program:
text = extract_text(path)

#Now that this has worked, will test on sample medical prior authorization request

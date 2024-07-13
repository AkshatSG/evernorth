#Packages Required; using easyOCR for its light weight compared to some other complex OCR systems like tesseract
import easyocr
import cv2
import matplotlib.pyplot as plt

# For visualizing the image with text that we want to perform OCR on:
def display_image(image, title='Image'):
    plt.figure(figsize=(10,10)) # Can adjust this
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

# Where the OCR proces happens
def extract_text(path):
    image_path=path
    image=cv2.imread(path)
    display_image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), 'Original Image')
    reader = easyocr.Reader(['en'])
    results = reader.readtext(image_path)

    #Results are presented as a list, will convert to string to feed to LLM:
    extracted = ' '.join([result[1] for result in results])
    print("Extracted Text:")
    print(extracted)

    #This part is used for displaying the location of findings on the image (OPTIONAL):

    # Currently has some bugs; this part is NOT necessary for OCR method to work


    for(bbox, text, prob) in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))

        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(image, text, (top_left[0], top_left[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        
        display_image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), 'Annotated Image')

    return extracted
import cv2
import re
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt

def process_image(filename):
    img = cv2.imread(filename)
    # Convert the image to grayscale and then to black and white
    bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # rescale the image to be smaller
    bw = cv2.resize(bw, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

    blur = cv2.GaussianBlur(bw, (3,3), 0)
    thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)
    return thresh

def process_text(text):
    text = text.encode("ascii", errors="ignore").decode()
    text = re.sub(r'\n+|\t+', ' ', text)
    text = ' '.join(word for word in text.split() if not all(letter.isupper() for letter in word))
    text = re.sub(' +', ' ', text)
    return text or ''

def create_bbox(tmp):
    '''
    Still need to implement this function. At the moment, it was not possible to accurately separate images from text.
    the idea is to use dilatation to join the text as a unified section in the iage and then create a bounding box using contour detection.
    '''
    # Dilate to combine adjacent text contours
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
    dilate = cv2.dilate(tmp, kernel, iterations=4)

    contours, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    text_boxes = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 50 and h > 50:
            text_boxes.append((x, y, w, h))
    # get the target crop fro the image
    crops = []
    for box in text_boxes:
        x, y, w, h = box
        crops.append(tmp[y:y+h, x:x+w])
    return crops

def add_delimiter(doc):
    paragraph = doc.add_paragraph()
    run = paragraph.add_run("---------------")
    font = run.font
    font.bold = True
    font.size = Pt(12)
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
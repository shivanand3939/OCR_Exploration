
from google.cloud import vision
import io

class OCR_v1 :
    def __init__(self):
        self.client = vision.ImageAnnotatorClient()

    def run(self):
        with io.open('images/OCR.v1.jpg', 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = self.client.text_detection(image=image)
        texts = response.text_annotations

        print(texts)

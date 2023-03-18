from .celery import app
from PIL import Image


@app.task
def process_image(image_path):
    img = Image.open(image_path)
    img = img.convert('L')
    img.save(image_path)
    print("YES")

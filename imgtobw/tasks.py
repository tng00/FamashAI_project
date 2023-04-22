import shutil
from .celery import app
from PIL import Image

n = 2023

@app.task
def process_image(image_path):
    global n
    n += 1
    save_path = "C:\\Users\\Hoang Nguyen\\Desktop\\img\\" + str(n) + ".png"
    shutil.copy(image_path, save_path)
    img = Image.open(image_path)
    img = img.convert('L')
    img.save(image_path)
    print(n)
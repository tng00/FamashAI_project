import os
import base64
from .celery import app
from .models import UploadImage
import shutil
import subprocess
from send2trash import send2trash

n = 2023

@app.task
def process_image(image_path):
    global n
    n += 1  # счетчик
    save_path = "C:\\Users\\Hoang Nguyen\\Desktop\\img\\" + str(n) + ".png"  # свой путь к сохр фото
    shutil.copy(image_path, save_path)
    # subprocess.call(r'') вставь путь к баш скрипту

    obj_name = str(n) + ".obj"
    # obj_name = "2023.obj"
    obj_path = r"C:\Users\Hoang Nguyen\Desktop\Папка обж и мат\\"  # меняешь путь на свой
    obj_path += obj_name
    with open(obj_path, 'rb') as file:
        obj_content = file.read()
    encoded_file_content = base64.b64encode(obj_content).decode('utf-8')
    obj_url = f"data:application/octet-stream;base64,{encoded_file_content}"

    mat_name = str(n) + ".mat"
    # mat_name = "2023.mat"
    mat_path = r"C:\Users\Hoang Nguyen\Desktop\Папка обж и мат\\"  # меняешь путь на свой
    mat_path += mat_name
    with open(mat_path, 'rb') as file:
        mat_content = file.read()
    encoded_file_content = base64.b64encode(mat_content).decode('utf-8')
    mat_url = f"data:application/octet-stream;base64,{encoded_file_content}"

    print(n)
    prod = UploadImage.objects.last()
    if prod.image:
        print(prod.image.url)
        os.remove(prod.image.path)
    send2trash(save_path)
    return [obj_url, obj_name, mat_url, mat_name]

from django.shortcuts import render
from .forms import ImageForm
from .tasks import process_image
import base64

def index(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            result = process_image.delay(img_obj.image.path)

            obj_name = "2023.obj" # сделай счетчик чтоб динамически менять название файла
            obj_path = r"C:\Users\Hoang Nguyen\Desktop\Папка обж и мат\\" # меняешь путь на свой
            obj_path += obj_name
            with open(obj_path, 'rb') as file:
                obj_content = file.read()
            encoded_file_content = base64.b64encode(obj_content).decode('utf-8')
            obj_url = f"data:application/octet-stream;base64,{encoded_file_content}"

            mat_name = "2023.mat" # сделай счетчик чтоб динамически менять название файла
            mat_path = r"C:\Users\Hoang Nguyen\Desktop\Папка обж и мат\\" # меняешь путь на свой
            mat_path += mat_name
            with open(mat_path, 'rb') as file:
                mat_content = file.read()
            encoded_file_content = base64.b64encode(mat_content).decode('utf-8')
            mat_url = f"data:application/octet-stream;base64,{encoded_file_content}"

            while not result.ready():
                continue
            return render(request, 'index.html',
                          {'form': form, 'img_obj': img_obj, 'obj_url': obj_url, 'obj_name': obj_name, 'mat_url': mat_url, 'mat_name': mat_name})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})
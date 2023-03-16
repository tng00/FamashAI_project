from django.shortcuts import render
from .forms import ImageForm
from PIL import Image


def index(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            original_image_url = img_obj.image.url
            img = Image.open(img_obj.image.path)
            img = img.convert('L')
            img.save(img_obj.image.path)
            return render(request, 'index.html',
                          {'form': form, 'img_obj': img_obj, 'original_image_url': original_image_url})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})

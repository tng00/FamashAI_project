from django.shortcuts import render
from .forms import ImageForm
from .tasks import process_image
from celery.result import AsyncResult



def index(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            result = process_image.delay(form.instance.image.path)
            while not result.ready():
                continue
            data = AsyncResult(result.id).get()
            return render(request, 'index.html',
                          {'form': form, 'done': True, 'obj_url': data[0], 'obj_name': data[1],
                           'mat_url': data[2], 'mat_name': data[3]})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})

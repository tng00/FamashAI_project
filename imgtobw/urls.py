from django.urls import path
from .views import index
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', index, name='index'),
    path('assetts/main_v2.png', RedirectView.as_view(url='/static/assetts/main_v2.png')),
]

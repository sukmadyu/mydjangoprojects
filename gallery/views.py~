from django.shortcuts import render
from .models import Gallery

# Create your views here.
def home_view(request):
    galleries = Gallery.objects.all()
    return render(request, 'gallery/home.html', {'galleries':galleries})

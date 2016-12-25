from django.shortcuts import render
from .models import Portfolio
from gallery.models import Gallery
from blog.models import Post

# Create your views here.
def home_view(request):
    portfolios = Portfolio.objects.all()[:10]
    galleries = Gallery.objects.all()[:10]
    posts = Post.objects.all()[:10]
    return render(request, 'index.html', {'portfolios':portfolios, 'galleries':galleries, 'posts':posts})

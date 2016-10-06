from django.shortcuts import render
from .models import Portfolio

# Create your views here.
def home_view(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio/home.html', {'portfolios':portfolios})

from django.shortcuts import render

from .models import Category, Book

# Create your views here.
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'library/category_list.html', {'categories': categories})


def book_list(request,  category_slug):
    category = Category.objects.get(slug=category_slug)
    books = Book.objects.filter(category=category)
    return render(request, 'library/book_list.html', {'books': books, 'category': category})

def book_detail(request, category_slug,  book_slug):
    book = Book.objects.get(slug=book_slug)
    return render(request, 'library/book_detail.html', {'book': book})


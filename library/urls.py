from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.category_list, name='category_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.book_list, name='book_list'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<book_slug>[-\w]+)/$', views.book_detail, name='book_detail'),


]

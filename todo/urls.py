from django.conf.urls import url
from . import home, todo

app_name = 'todo'
#urlpatterns += patterns(r'^$', views.main_page, name='index'),

urlpatterns = [
    url(r'^$', home.main_page, name='index'),
    url(r'^signup$', home.signup, name='signup'),
    url(r'^login$', home.login, name='login'),
    url(r'^logout$', home.logout, name='logout'),
    url(r'^add-todo$', todo.add_todo, name='add_todo'),
    url(r'^edit-todo/(?P<todo_id>\d+)$', todo.edit_todo, name='edit_todo'),
    url(r'^delete-todo/(?P<todo_id>\d+)$', todo.delete_todo, name='delete_todo'),
]

from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home),
    path('article', views.articlelist, name='articlelist'),
    path('article/<int:pk>', views.articledetail, name='articledetail'),
    path('articlecreate', views.articlecreate, name='articlecreate'),
]
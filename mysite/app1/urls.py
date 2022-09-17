
from django.urls import path, include
from . import views

app_name = 'app1'
urlpatterns = [
    path('', views.show_page, name='show_page')
]
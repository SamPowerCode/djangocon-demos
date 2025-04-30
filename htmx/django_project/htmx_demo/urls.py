from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-time/', views.get_time, name='get_time'),
    path('toggle/<int:id>', views.toggle_todo, name='toggle_todo'),
    path('add/', views.add_todo, name='add_todo'),
]

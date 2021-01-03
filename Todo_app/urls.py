from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:filter>/', views.index, name="index"),
    path('delete/<int:id>', views.delete_task, name="delete_task"),
    path('change/<int:id>', views.change_line, name="change_line"),
    
    
]

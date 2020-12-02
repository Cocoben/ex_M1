from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.edit, name='edit'),
    path('vote/', views.new, name='new'),
    path('<int:task_id>/delete/', views.delete, name='delete'),
    path('<int:task_id>/done/', views.done, name='done'),
]
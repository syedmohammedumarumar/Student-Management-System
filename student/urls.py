from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('view_all_students/', views.view_all_students, name='view_all_students'),
    path('add_students/', views.add_students, name='add_students'),
    path('remove_students/', views.remove_students, name='remove_students'),
    path('delete/<int:student_id>', views.delete, name='delete'),
    path('filter_students/', views.filter_students, name='filter_students'),
]

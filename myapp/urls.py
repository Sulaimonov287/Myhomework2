from django.urls import path
from .views import *

urlpatterns = [
    path('students/', show_students, name='students'),
    path('students/create/', create_students, name='students_create'),
    path('students/update/<int:pk>/', update_students, name='students_update'),
    path('students/delete/<int:pk>/', delete_students, name='students_delete')
]

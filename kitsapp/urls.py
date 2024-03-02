from django.urls import path
from . import views

urlpatterns=[
    path('',views.read,name='read'),
    path('delete',views.delete,name='delete'),
    path('add_student',views.add_student,name="add_student"),
    path('editstudent/<str:uname>/', views.editstudent, name="editstudent"),
    path('delete/<str:uname>/', views.delete, name="delete"),
]
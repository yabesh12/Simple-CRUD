from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('students/',views.student_list,name='students'),
    path('delete/',views.delete,name='delete')
]

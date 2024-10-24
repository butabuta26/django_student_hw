from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main_page_view, name = 'main_page'),
    path('students/', views.students_page_view, name = 'students_page')
]

from django.urls import path

from . import views

urlpatterns = [
    path('course/', views.course_view, name = 'course_form'),
    path('course_description/', views.course_description, name = 'course_description'),
    path('course_list', views.course_name_list, name = 'course_list'),
    path('single_course_description/<str:course_name>', views.single_course_description, name = 'single_course_description'),
    
]


from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('student_form', views.student_form, name = 'student-form'),
    path('course_form', views.course_form, name = 'course-form'),
    path('dashboard', views.dashboard, name = 'dashboard'),
]

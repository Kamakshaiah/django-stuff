from django.conf.urls import url
from . import views

urlpatterns = [
    url('home/', views.home, name = 'tables_home'),
    url('about/', views.about, name = 'tables_about'),
]

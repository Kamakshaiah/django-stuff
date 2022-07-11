
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('show/', views.show, name='show'),
    path('add/', views.add, name='add'),
    path('<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('approve/<int:id>', views.authenticate, name='approve'),
    
]
